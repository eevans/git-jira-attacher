#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup


setup(name='git-jira-attacher',
      version='0.1',
      description='Utility for integrating Git and JIRA workflows',
      long_description=open('README.rst').read(),
      url='http://github.com/dreiss/git-jira-attacher/tree',
      author='David Reiss',
      maintainer='Michael Greene',
      maintainer_email='michael.greene@gmail.com',
      license='MIT License',
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Topic :: Software Development :: Bug Tracking",
        "Topic :: Software Development :: Version Control",
      ],
      scripts=['jira-am', 'jira-apply'],
      py_modules=['common', 'git-jira-attacher'],
      install_requires=['suds >= 0.3.6'],
)
