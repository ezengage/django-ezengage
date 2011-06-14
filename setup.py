import os

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES')).read()

setup(name='django-ezengage',
      version='0.1.1',
      description='django app works with ezengage service',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Framework :: Django",
        ],
      author='ftao',
      author_email='ftao@ezengage.com',
      url='',
      keywords='ezengage,django',
      download_url='https://github.com/ezengage/django-ezengage/zipball/v0.1.1',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'Django',
            'simplejson',
            ],
      tests_require=[
            'Django',
            'simplejson',
            ],
      )

