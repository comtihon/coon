from walrus.pac_cache import CacheType
from walrus.pac_cache import cache_factory
from walrus.pac_cache.local_cache import LocalCache
from walrus.packages.package import Package


class CacheMan:
    local_cache: LocalCache = None
    caches = []

    def __init__(self, conf: dict):
        super().__init__()
        for cache_type in conf.keys():
            cache = cache_factory.get_cache(cache_type, conf[cache_type])
            if cache_type == CacheType.LOCAL:
                self.local_cache = cache
            self.caches.append(cache)

    # TODO add ability to customise search policy (build instead of fetching from remote etc...).
    def exists(self, package: Package):
        for cache in self.caches:
            if cache.exists(package):
                return True
        return False

    def link_package(self, package: Package, path: str):
        if self.local_cache:
            self.local_cache.link_package(package, path)

    def add_package(self, package: Package):
        if self.local_cache:
            self.local_cache.add_package(package)