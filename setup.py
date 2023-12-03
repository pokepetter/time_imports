from setuptools import find_packages, setup

setup(
    name='time_imports',
    version='1',
    py_modules=['time_imports'],
    entry_points='''
    [time_imports]
    time_imports=time_imports:time_imports
    ''',
    author='Petter Amland',
    author_email='pokepetter@gmail.com',

)
