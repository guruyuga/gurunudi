#!/usr/bin/env python

from setuptools import setup

setup(name='gurunudi',
      version='0.1',
      description='The official Python client for Gurunudi AI API',
      url='http://github.com/gurulaghu/gurunudi',
      author='GuruLaghu Technologies',
      author_email='gurulaghu@use.startmail.com',
      license='MIT',
      packages=['gurunudi'],
      install_requires=['requests>=2.13.0'],
      classifiers=[
                'Development Status :: 4 - Beta',
                'Environment :: Console',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: MIT License',
                'Operating System :: POSIX :: Linux',
                'Operating System :: MacOS :: MacOS X',
                'Operating System :: Microsoft :: Windows',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
'Topic :: Scientific/Engineering :: Artificial Intelligence'],)
