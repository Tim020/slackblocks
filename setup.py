#!/usr/bin/env python
import setuptools


setuptools.setup(
    name='slackblocks',
    version='0.0.1',
    description='Modular Slack Blocks in code',
    long_description=open('README.md').read(),
    author='Tim Bradgate',
    url='https://github.com/Tim020/slackblocks',
    scripts=[],
    packages=setuptools.find_packages(exclude=['tests*']),
    include_package_data=True,
    extras_require={},
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)

