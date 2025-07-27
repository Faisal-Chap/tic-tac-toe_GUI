from setuptools import setup, find_packages

setup(
    name='tictactoe',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # You don't need 'tk' — it's system installed
    ],
    entry_points={
        'console_scripts': [
            'tictactoe = game.gui:main',
        ],
    },
    package_data={
        '': ['*.desktop', 'assets/*.png']
    },
)
