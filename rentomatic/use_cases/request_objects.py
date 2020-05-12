import collections
from typing import Dict, Any
from rentomatic.shared import request_object as req


class StorageRoomListRequestObject(req.ValidRequestObject):

    def __init__(self, filters: Dict[str, Any] = None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict: Dict[str, Dict[str, Any]]) -> req.RequestObject:
        invalid_req = req.InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return StorageRoomListRequestObject(filters=adict.get('filters', None))
