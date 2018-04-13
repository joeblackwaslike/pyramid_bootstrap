from pyramid.settings import asbool

from .library import LibraryFactory


__version__ = '4.1.0'

VERSIONS = {
    'twitter-bootstrap': '4.1.0',
    'jquery': '3.2.1',
    'popper.js': '1.12.9',
    'font-awesome': '4.7.0'
}


def includeme(config):
    DEFAULT = {
        'bootstrap_version': VERSIONS['twitter-bootstrap'],
        'jquery_version': VERSIONS['jquery'],
        'popper_version': VERSIONS['popper.js'],
        'fontawesome_version': VERSIONS['font-awesome'],
        'use_min': True,
        'use_cdn': False,
        'static_path': {
            'cdn': "//cdnjs.cloudflare.com/ajax/libs",
            'local': 'static/bs4'
        },
        'cache_max_age': 3600,
    }

    settings = config.get_settings()
    setting_prefix = "bootstrap."

    def get_setting(attr, default=None):
        return settings.get(setting_prefix + attr, default)

    bootstrap_version = get_setting('version', DEFAULT['bootstrap_version'])
    jquery_version = get_setting('jquery_version', DEFAULT['jquery_version'])
    popper_version = get_setting('popper_version', DEFAULT['popper_version'])
    fontawesome_version = get_setting(
        'fontawesome_version', DEFAULT['fontawesome_version'])

    use_min = asbool(get_setting("use_min", DEFAULT['use_min']))
    use_cdn = asbool(get_setting("use_cdn"))

    if use_cdn:
        static_path = DEFAULT['static_path']['cdn']
    else:
        static_path = get_setting(
            'static_path', DEFAULT['static_path']['local'])

    cache_max_age = get_setting('cache_max_age', DEFAULT['cache_max_age'])

    libraries = LibraryFactory.build_libraries(VERSIONS, use_min)
    for name, lib in libraries.items():
        config.add_static_view(
            '/'.join([static_path, lib.library, lib.version]),
            "pyramid_bootstrap:{}/{}/".format(static_path, lib.library),
            cache_max_age=cache_max_age)

    config.override_asset(
        to_override='{}:templates/bs4/'.format(config.root_package.__name__),
        override_with='pyramid_bootstrap:templates/bs4/')

    config.scan('pyramid_bootstrap.event_subscribers')
