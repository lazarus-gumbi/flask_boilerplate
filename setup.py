from setuptools import setup, find_packages

setup(
    name='flask_boilerplate',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click','flask'
        ],
    entry_points='''
    [console_scripts]
    flask_boilerplate=flask_boilerplate:flask_boilerplate
    '''
        )
