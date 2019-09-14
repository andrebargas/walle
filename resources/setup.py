from setuptools import setup, find_packages

setup(
    name='buscador',
    version='1.0.0',
    description='Arquitetura padrão Microservice módulo.',
    url='-',
    author='Stefanini',

    classifiers=[
        'Development Status :: Developer/Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='Flasgger documentation Stefanini',

    packages=find_packages(),

    install_requires=['flask-restplus==0.9.2', 'Flask-SQLAlchemy==2.1'],
)
