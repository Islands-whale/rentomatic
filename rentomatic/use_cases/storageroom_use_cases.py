from rentomatic.shared import use_case as uc
from rentomatic.shared import response_object as res
from rentomatic.repository.memrepo import MemRepo
from rentomatic.use_cases.request_objects import StorageRoomListRequestObject


class StorageRoomListUseCase(uc.UseCase):

    def __init__(self, repo: MemRepo):
        self.repo = repo

    def process_request(self, request_object: StorageRoomListRequestObject) -> res.ResponseSuccess:
        domain_storageroom = self.repo.list(filters=request_object.filters)
        return res.ResponseSuccess(domain_storageroom)
