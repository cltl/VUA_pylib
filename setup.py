from distutils.core import setup


setup(name='VUA_pylib',
      version='1.3',
      description = 'Various KAF / NAF python helpers',
      author = 'Ruben Izquierdo',
      url = 'https://github.com/cltl/VUA_pylib',
      author_email = 'r.izquierdobevia@vu.nl',
      packages = ['VUA_pylib','VUA_pylib.lexicon','VUA_pylib.common','VUA_pylib.io_utils','VUA_pylib.corpus_reader'],
      )
