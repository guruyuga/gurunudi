#!/usr/bin/env python

from setuptools import setup, PEP420PackageFinder

pep420_package_finder = PEP420PackageFinder()
readme=open('README.rst',encoding='utf8').read()

setup(name='gurunudi',
      version='1.4.0',	
      description='The official Python client for Gurunudi AI API',
      long_description=readme,
      url='http://github.com/guruyuga/gurunudi',
      author='GuruYuga',
      author_email='contact@gurunudi.com',
      license='Apache-2.0',
      packages=pep420_package_finder.find('.', include=['gurunudi*']),
      keywords=["guruyuga","gurunudi","artificial-intelligence","chatbot","nlp","nlg","nli","machine-learning","sentiment-analysis","natural-language-processing","natural-language-generation","natural-language-inference","machine-translation","autocomplete","autocorrect","spell-check","coreference-resolution","knowledge-graph","expert-system","context-qa","topic-modeling"],
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
