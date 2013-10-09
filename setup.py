from setuptools import setup, find_packages

version = '0.0.1'

setup(name="helga-norris",
      version=version,
      description=('norris plugin for helga'),
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: IRC',
                   'Intended Audience :: Twisted Developers, IRC Bot Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: IRC Bots'],
      keywords='irc bot norris',
      author='alfredo deza',
      author_email='contact@deza.pe',
      url='https://github.com/alfredodeza/helga-norris',
      license='MIT',
      packages=find_packages(),
      entry_points = dict(
          helga_handlers = [
              'norris = helga_norris.norris:NorrisExtension',
          ],
      ),
)
