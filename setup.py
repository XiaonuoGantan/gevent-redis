#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools import setup


def run_setup():
    setup(
         name='gevent-redis',
         version='0.0.1',
         description='Asynchronous Redis client that works within Gevent.',
         author='Phus Lu',
         author_email='phus.lu@gmail.com',
         license='Apache 2.0',
         url='https://github.com/phus/gevent-redis',
         packages=['geventredis',],
         zip_safe=False,

    install_requires = [
        "gevent",
        ],
    )

if __name__ == "__main__":
    run_setup()
