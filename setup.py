#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0']

extra_requirements = {
    'healthcheck': ['aiohttp', 'aio-tiny-healthcheck'],
}
test_requirements = ['pytest>=3']

setup(
    author='Ryan Anguiano',
    author_email='ryan.anguiano@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description='CLI commands utility with ASGI lifespan and healthcheck support.',
    extras_require=extra_requirements,
    install_requires=requirements,
    license='MIT license',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='app_commands',
    name='app_commands',
    packages=find_packages(include=['app_commands', 'app_commands.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ryananguiano/app-commands',
    version='0.1.0',
    zip_safe=False,
)
