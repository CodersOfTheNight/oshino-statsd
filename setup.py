#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup

from oshino_statsd.version import get_version


setup(name="oshino_statsd",
      version=get_version(),
      description="...",
      author="zaibacu",
      packages=["oshino_statsd"],
      install_requires=["oshino"],
      test_suite="pytest",
      tests_require=["pytest", "pytest-cov"],
      setup_requires=["pytest-runner"]
      )
