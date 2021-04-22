from setuptools import setup, find_packages

setup(
    name='tira-cli',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'rich',
    ],
    entry_points='''
        [console_scripts]
        tira=tira.command:cli
    ''',
)