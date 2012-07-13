from distutils.core import setup
from setuptools import find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_packages_in(where, **kwargs):
    return [where] + ['%s.%s' % (where, package) for package in find_packages(where=where, **kwargs)]

setup(
    name = 'django-logmein',
    version = '0.1.0',
    author = 'Allan Lei',
    author_email = 'allanlei@helveticode.com',
    description = 'Authentication via third party services for Django',
    license=open('LICENSE.txt').read(),
    keywords = 'django authentication',
    url = 'https://github.com/allanlei/django-logmein',
    packages=find_packages_in('logmein'),
    install_requires=[
    ],
)
