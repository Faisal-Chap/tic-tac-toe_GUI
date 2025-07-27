from setuptools import setup, find_packages

setup(
    name="tictactoe",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "tictactoe = tic_tac_toe.main:main"
        ],
    },
)
