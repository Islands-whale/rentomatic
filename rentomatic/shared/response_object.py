from typing import List, Dict, Optional
from rentomatic.shared.request_object import InvalidRequestObject
from rentomatic.domain.storageroom import StorageRoom


class ResponseObject:
    pass


class ResponseSuccess(ResponseObject):
    SUCCESS = 'SUCCESS'

    def __init__(self, value: List[StorageRoom] = None):
        self.type = self.SUCCESS
        self.value = value

    def __nonzero__(self) -> bool:
        return True

    __bool__ = __nonzero__


class ResponseFailure(ResponseObject):
    RESOURCE_ERROR = 'RESOURCE_ERROR'
    PARAMETERS_ERROR = 'PARAMETERS_ERROR'
    SYSTEM_ERROR = 'SYSTEM_ERROR'

    def __init__(self, type_: str, message: Optional[str]):
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, msg: Optional[str]) -> Optional[str]:
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg

    @property
    def value(self) -> Dict[str, Optional[str]]:
        return {'type': self.type, 'message': self.message}

    def __bool__(self) -> bool:
        return False

    @classmethod
    def build_resource_error(cls, message: str = None):
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_system_error(cls, message: str = None):
        return cls(cls.SYSTEM_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message: str = None):
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_from_invalid_request_object(cls, invalid_request_object: InvalidRequestObject):
        message = "\n".join([
            "{}: {}".format(err['parameter'], err['message'])
            for err in invalid_request_object.errors
        ])
        return cls.build_parameters_error(message)
