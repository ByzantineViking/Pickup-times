

from setuptools import setup

setup(
    name='delivery',
    version='1.0',
    py_modules=[''],
    install_requires=['Click', 'numpy', 'pandas', 'colorama'],
    entry_points='''
        [console_scripts]
        delivery=delivery:cli
    ''',
)