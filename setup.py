import re
from pip.req import parse_requirements
from setuptools import setup, find_packages


def requirements(filename):
    reqs = parse_requirements(filename, session=False)
    return [str(r.req) for r in reqs]


def get_version():
    with open('sqlalchemy_paginate/__init__.py', 'r') as f:
        version_regex = r'^__version__\s*=\s*[\'"](.+)[\'"]'
        return re.search(version_regex, f.read(), re.MULTILINE).group(1)

setup(
    name='SqlAlchemy-Paginate',
    version=get_version(),
    url='https://github.com/wizeline/sqlalchemy-paginate',
    author='Wizeline',
    author_email='engineering@wizeline.com',
    description='A small utility to paginate SqlAlchemy queries.',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python 3',
        'Topic :: Utilities'
    ],
    tests_require=requirements('requirements-dev.txt'),
    install_requires=requirements('requirements.txt'),
    extras_require={
        'dev': requirements('requirements-dev.txt')
    }
)
