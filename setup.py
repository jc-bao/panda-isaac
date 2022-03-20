'''Setup script for panda_isaac'''

from setuptools import setup

requirements = [
  'numpy'
]

setup(name='panda_isaac',
  version='0.1.0',
  author='Chaoyi Pan',
  author_email='pcy19@mails.tsinghua.edu.cn',
  package_dir = {'': '.'},
  packages=['panda_isaac'],
  install_requires=requirements,
  )
