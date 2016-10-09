from setuptools import setup

required = []

setup(name='mock_decorator',
      version="1.0",
      author="Francisco Huertas",
      author_email="fhuertas@gmail.com",
      license="Apache2",
      packages=["mock_decorators"],
      description='Mock decorator for python tests',
      url='https://github.com/fhuertas/mock_decorator',
      install_requires=required,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Topic :: Utilities",
          "License :: OSI Approved :: Apache 2",
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ])
