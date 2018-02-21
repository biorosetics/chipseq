from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='chipseq',  # Required
    version='1.1.0',  # Required
    description='Canidhub chipseq tools chain',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/pypa/sampleproject',  # Optional
    author='Charles Hebert',  # Optional
    author_email='charles@biorosetics.com',  # Optional
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='candihub chipseq',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['peppercorn'],  # Optional
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    package_data={  # Optional
        'sample': ['package_data.dat'],
    },
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('my_data', ['data/data_file'])],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)