#!/usr/bin/env python
from setuptools import setup, find_packages
import platform

#TEST_REQUIRES = [
#    'flexmock>=0.9.7',
#    'nose',
#    'coverage',
#    'unittest2'
#]

INSTALL_REQUIRES = [
    'urllib',
    'urllib2',
]


setup(
    name='Base CRM Client',
    version='1.0.0',
    url='http://claytondaley/base-crm-api-client',
    description='Python client for Base CRM',
    long_description=__doc__,
    packages=find_packages(exclude=("tests", "tests.*",)),
    zip_safe=False,
    extras_require={
        'tests': TEST_REQUIRES,
    },
    license='BSD',
    tests_require=TEST_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    test_suite='tests',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)