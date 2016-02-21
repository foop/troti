try:
    from setuptools import setup
except ImportError:
    from disutlis.core import setup

config = {
        'description' : 'Linz AG Linien Monitor',
        'author' : 'Dominik Danter',
        'url' : 'https://github.com/foop/troti',
        'download_url' : '', #TODO
        'author_email' : 'dominik@foop.at',
        'version' : '0.1',
        'install_requieres' : ['nose'],
        'packages' : ['troti'],
        'scripts' : [],
        'name' : 'troti'
}

setup(**config)
