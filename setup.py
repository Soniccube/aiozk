from setuptools import setup, find_packages

from aiozk import __version__


setup(
    name='aiozk',
    version=__version__,
    description='Asyncio client for Zookeeper.',
    author='Kirill Pinchuk',
    author_email='cybergrind@gmail.com',
    maintainer='Kirill Pinchuk',
    maintainer_email='cybergrind@gmail.com',
    url='http://github.com/tipsi/aiozk',
    license='MIT',
    keywords=['zookeeper', 'asyncio', 'async'],
    packages=find_packages(exclude=['tests', 'tests.*', 'docker']),
    install_requires=[
        'tipsi_tools>=0.9.0',
    ],
    entry_points={
    },
    tests_require=[
        'coverage',
        'flake8',
        'nose2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
    ],
)
