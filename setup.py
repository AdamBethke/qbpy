from setuptools import setup

setup(
    name='qbpy',
    version='0.9.0',
    description='Python Quick Base API Wrapper',
    long_description='',
    url='https://gitlab.com/abethke/qbpy.git',
    author='Adam Bethke',
    author_email='abethke@dcpcsb.org',
    license='MIT',
    packages=['qbpy'],
    install_requires=[
        'lxml',
        'requests',
        'pandas',
        'xmltodict',
    ]
)
