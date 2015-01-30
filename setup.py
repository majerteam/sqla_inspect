# -*- coding: utf-8 -*-
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='sqla_inspect',
    version='0.1',
    packages=['sqla_inspect'],
    include_package_data=True,
    license='BSD License',  # example license
    description='Usefull tools for setting/getting datas from SQLAlchemy models',
    long_description=README,
    url='',
    author='Majerti',
    author_email='tech@majerti.fr',
    install_requires=['SQLAlchemy', 'py3o', 'openpyxl', 'colanderalchemy'],
    extra_requires={'docs': ['sphinx'], 'test': ['pytest']},
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Sqlalchemy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
