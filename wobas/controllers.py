import zuice

from .templating import Templates
from .repos import BucketRepository
from .web import PathArguments, Responder


class ViewBucketController(zuice.Base):
    _responder = zuice.dependency(Responder)
    _bucket_repository = zuice.dependency(BucketRepository)
    
    request = dict(
        path_args = PathArguments
    )
    
    def respond(self, path_args):
        bucket_slug = path_args["bucket_slug"]
        bucket = self._bucket_repository.find_by_slug(bucket_slug)
        if bucket is None:
            return self._responder.not_found()
        else:
            return self._responder.html("view-bucket", {"bucket": bucket})
