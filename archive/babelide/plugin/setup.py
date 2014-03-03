from setuptools import setup, find_packages

setup(
    name = 'BabelIDE',
    version = 'dev',
    packages = find_packages(),

    install_requires = [
        'requests',
        'jinja2',
        'websocket-client',
        'tornado',
        'cython',
        'lxml'
        ]
)

