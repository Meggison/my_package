from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    author='Meggison',
    url='github.com/Meggison/my_package',
    author_email='meggisonoritsemisan@gmail.com'

)