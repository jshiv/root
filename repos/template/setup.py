import os
import setuptools

# Set __version__ in this space
execfile('%s/version.py' % os.path.dirname(os.path.realpath(__file__)))

setuptools.setup(
    name='template',
    version=__version__,  # NOQA
    description='template package',
    author='Jason Shiverick',
    author_email='jshiv00@gmail.com',
    url='',
    install_requires=([
        'matplotlib',
        'scipy',
        'numpy',
        'pandas',
        'seaborn'
    ]),
    packages=['template']
)
