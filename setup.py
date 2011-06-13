import os

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()
CHANGES = open(os.path.join(here, 'CHANGES')).read()

setup(name='django-ezengage',
      version='0.1',
      description='',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        ],
      author='ftao',
      author_email='ftao@ezengage.com',
      url='',
      keywords='ezengage',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'Django',
            ],
      tests_require=[
            'Django',
            ],
      )

