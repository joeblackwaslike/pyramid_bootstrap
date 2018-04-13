import re
from setuptools import setup, find_packages


with open('pyramid_bootstrap/__init__.py', 'rt') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

try:
    from m2r import parse_from_file
    long_description = parse_from_file('README.md')
except ImportError:
    with open('README.md') as fd:
        long_description = fd.read()

setup(
    name='pyramid_bootstrap4',
    version=version,
    description='Bootstrap 4.0 for Pyramid',
    long_description=long_description,
    keywords=[
        'pyramid',
        'bootstrap',
        'reponsive',
        'framework'
    ],
    author='Joe Black',
    author_email='me@joeblack.nyc',
    maintainer='Joe Black',
    maintainer_email='me@joeblack.nyc',
    url='https://github.com/joeblackwaslike/pyramid_bootstrap',
    download_url=(
        'https://github.com/joeblackwaslike/pyramid_bootstrap/tarball/v%s'
        % version),
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['LICENSE']},
    install_requires=[
        "Pyramid>=1.9.1",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
