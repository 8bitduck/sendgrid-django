from setuptools import setup, find_packages

from sgbackend.version import __version__

setup(
    name='sendgrid-django',
    version=str(__version__),
    author='Yamil Asusta',
    author_email='yamil@sendgrid.com',
    url='https://github.com/elbuo8/sendgrid-django',
    packages=find_packages(),
    license='MIT',
    description='SendGrid Backend for Django',
    long_description=open('./README.rst').read(),
    install_requires=["sendgrid==0.5.1"],
)
