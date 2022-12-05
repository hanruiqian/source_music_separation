from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

setup(
    name='ruiqian',
    version='0.1.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Topic :: Artistic Software',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Editors',
        'Topic :: Software Development :: Libraries',
    ],
    description='Utilities for the course work of ruiqian_han.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ruiqian Han',
    author_email='ruiqian_han@hhu.edu.com',
    license='MIT',
    packages=find_packages(),
    keywords=['audio', 'source', 'separation', 'music', 'sound', 'source separation'],
    install_requires=[
        REQUIREMENTS
    ],
)
