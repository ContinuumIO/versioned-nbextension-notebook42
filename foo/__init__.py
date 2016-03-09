from os.path import join

from ._version import __version__


def _jupyter_nbextension_paths():
    return [{
        'section': 'tree',
        'src': join('static', 'tree'),
        'dest': join('foo-tree', __version__),
        'require': 'index'
    }, {
        'section': 'notebook',
        'src': join('static', 'notebook'),
        'dest': join('foo-notebook', __version__),
        'require': 'index'
    }]


def _jupyter_server_extension_paths():
    return [{
        "module": "foo-baz"
    }]


def load_jupyter_server_extension(nbapp):
    print("foo", __version__, "started")
