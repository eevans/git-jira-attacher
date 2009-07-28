#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(name='git-jira-attacher',
      version='0.1',
      description='Utility for integrating Git and JIRA workflows',
      long_description=open('README.rst').read(),
      author='David Reiss',
      url='http://github.com/dreiss/git-jira-attacher/tree',
      license='MIT License',
      scripts=['jira-am', 'jira-apply'],
      py_modules=['common', 'git-jira-attacher'],
      install_requires=['suds >= 0.3.6'],
)
