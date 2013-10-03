class BucketRepository(object):
    def find_by_slug(self, slug):
        return Bucket(slug)


class Bucket(object):
    def __init__(self, slug):
        self.slug = slug
