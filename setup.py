from setuptools import setup

setup(
    name="csv-bsplit",
    version="0.1.0",
    py_modules=["csv_bsplit"],
    entry_points={
        "console_scripts": [
            "csv-bsplit=csv_bsplit:main"
        ]
    }
)
