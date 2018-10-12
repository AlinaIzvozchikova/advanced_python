import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__),
                             fname)).read()

setup(
    name='MetaclassProperty',
    version='1.0',
    description='Create metaclass that generates properties automatically',
    author='Alina Izvozchikova',
    author_email='alina_iz@mail.ru',
    url='http://www.epam.com',
    scripts=['start_app.py',],
    packages=['metaclass_property',],
    long_description=read('README.md'),
)
