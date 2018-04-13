from copy import deepcopy

from .spec import ASSET_SPECS


class LibraryFactory(object):
    """
    Design:
     * Each library version has its own Library class.
     * Static assets of each library are prepared in build process.
    """

    libraries = []

    @classmethod
    def build(clso, library, version, use_min=True):
        assets = deepcopy(ASSET_SPECS[library])
        if use_min:
            for type, items in assets.items():
                for name, path in items.items():
                    assets[type][name] = '.min.'.join(path.rsplit('.', 1))
        assets['_prefix'] = 'pyramid_bootstrap:static/bs4/{}/'.format(library)

        class Library(object):
            def __init__(self, request):
                self.request = request

            def static_path(self, path):
                if '.min.' not in path:
                    path = '.min.'.join(path.rsplit('.', 1))
                return self.request.static_path(self.assets['_prefix'] + path)

            def static_path_not_min(self, path):
                return self.static_path(path.replace(".min.", "."))

            def static_url(self, path):
                if '.min.' not in path:
                    path = '.min.'.join(path.rsplit('.', 1))
                return self.request.static_url(self.assets['_prefix'] + path)

            def static_url_not_min(self, path):
                return self.static_url(path.replace(".min.", "."))

        Library.library = library
        Library.version = version
        Library.assets = assets
        return Library

    @classmethod
    def build_libraries(clso, versions, use_min):
        clso.versions = versions
        clso.libraries = {
            library: clso.build(library, version.strip(), use_min=use_min)
            for library, version in clso.versions.items()}
        return clso.libraries

    @classmethod
    def build_loader(clso, request):
        if not clso.libraries:
            raise Exception(("{cls}.libraries not built. See {cls}."
                             "build_libraries").format(cls=clso.__name__))

        def load_library(library=None):
            if library is None:
                return list(clso.libraries.values())[0](request)
            else:
                try:
                    return clso.libraries[library](request)
                except KeyError:
                    raise KeyError(
                        'Library {} not found'.format(library))
        return load_library
