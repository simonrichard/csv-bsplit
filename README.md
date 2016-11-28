csv-bsplit
==========

csv-bsplit is a command-line script that splits a CSV file into smaller files that don't exceed a certain size in bytes.
It's written in Python 3 and is not currently backward compatible with Python 2.7.

Installation
------------

csv-bsplit is not currently available on the Python Package Index. It can be installed with:

    $ git clone https://github.com/simonrichard/csv-bsplit.git
    $ cd csv-bsplit
    $ python setup.py install

Example usage
-------------

    $ csv-bsplit --headers --outfile=myfile_{}.csv --limit=2e+7 myfile.csv

This example splits `myfile.csv` into files that don't exceed 2e+7 bytes or 20 megabytes.
These files are named by inserting a number in the replacement field in curly braces (`{}`).
The first row is added to every file because of the `--headers` flag.
The script assumes there are no headers when the flag is absent.
