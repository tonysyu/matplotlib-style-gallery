from os.path import join

from pip.req import parse_requirements
from setuptools import setup, find_packages


package_name = 'mpl_style_gallery'

install_reqs = list(parse_requirements('requirements.txt'))
requirements = [str(ir.req) for ir in install_reqs]

info = {}
execfile(join(package_name, '__init__.py'), info)


setup(
    name=package_name,
    version=info['__version__'],
    author='Tony S. Yu',
    author_email='tsyu80@gmail.com',
    maintainer='Tony S. Yu',
    maintainer_email='tsyu80@gmail.com',
    description='Gallery for Matplotlib stylesheets',
    url='https://github.com/tonysyu/matplotlib-style-gallery',
    include_package_data=True,
    install_requires=requirements,
    license='Modified BSD',
    packages=find_packages(),
)
