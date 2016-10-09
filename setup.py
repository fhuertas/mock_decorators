import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


required = []

setup(name='mock_decorators',
      version=read('VERSION'),
      author="Francisco Huertas",
      author_email="pacohuertas@gmail.com",
      license="Apache2",
      packages=["mock_decorators"],
      long_description=read('README.md'),
      url='https://github.com/fhuertas/mock_decorators',
      install_requires=required,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Utilities",
          "License :: OSI Approved :: Apache Software License",
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ])
