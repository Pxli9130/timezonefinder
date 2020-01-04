# -*- coding:utf-8 -*-
from setuptools import setup

from timezonefinder.global_settings import DATA_FILE_NAMES

setup(
    name='timezonefinder',
    packages=['timezonefinder'],
    package_data={'timezonefinder': DATA_FILE_NAMES},
    description='fast python package for finding the timezone of any point on earth (coordinates) offline',
    author='J. Michelfeit',
    author_email='python@michelfe.it',
    license='MIT licence',
    license_file='LICENSE',
    url='https://github.com/MrMinimal64/timezonefinder',  # use the URL to the github repo
    project_urls={
        "Source Code": "https://github.com/MrMinimal64/timezonefinder",
        "Documentation": "https://timezonefinder.readthedocs.io/en/latest/",
        "Changelog": "https://github.com/MrMinimal64/timezonefinder/blob/master/CHANGELOG.rst",
    },
    keywords='timezone coordinates latitude longitude location pytzwhere tzwhere',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language:: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Localization',
    ],
    install_requires=['numpy>=1.16'],
    python_requires='>=3.6',
    zip_safe=False,
    # TODO data extras, oceans, test
    extras_require={'numba': ["numba>=0.42"]},
)
