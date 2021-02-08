import os

from setuptools import setup


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    with open(path) as f:
        return f.read()


setup(
    name='free-book-bot',
    version='1.0.0',
    description=('Free book bot'),
    long_description=read('README.md'),
    author='Marília Muraro Janizelli Campos de Morais',
    author_email='mmjanizelli@gmail.com',
    url='https://github.com/MariliaMJ/Free-Book-Bot',
    keywords='cron bot',
    packages=['cron', 'script'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    extras_require={
        'httplib2': ['httplib2==0.19.0'],
        'python-crontab': ['python-crontab==2.5.1'],
    },
)
