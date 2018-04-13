from pyramid.renderers import get_renderer
from pyramid.events import subscriber
from pyramid.events import BeforeRender
from . import LibraryFactory


@subscriber(BeforeRender)
def add_bootstrap_renderer(event):
    try:
        event['master'] = get_renderer(
            'templates/bs4/master.pt').implementation()
    except ValueError:
        pass
    event['bs4_resource'] = LibraryFactory.build_loader(event['request'])
