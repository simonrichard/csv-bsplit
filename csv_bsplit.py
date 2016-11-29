#!/usr/bin/python3
import argparse
import csv
import humanfriendly as hf
import os

from io import StringIO


def read(infile, headers):
    f = open(infile)
    reader = csv.reader(f)
    if headers:
        headers = next(reader)
    return f, headers, reader


def file(outfile, headers, i):
    f = os.open(outfile.format(i), os.O_WRONLY | os.O_CREAT | os.O_EXCL)
    f = os.fdopen(f, "w")
    writer = csv.writer(f)
    if headers:
        writer.writerow(headers)
    return f, writer


def write(data, outfile, limit):
    infile, headers, docs = data
    i = 1
    f, writer = file(outfile, headers, i)

    for doc in docs:
        with StringIO() as mock:
            csv.writer(mock).writerow(doc)
            size = len(bytes(mock.getvalue(), "utf-8"))
        if f.tell() + size > limit:
            f.close()
            i += 1
            f, writer = file(outfile, headers, i)
        writer.writerow(doc)

    infile.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outfile", required=True)
    parser.add_argument("-l", "--limit", required=True)
    parser.add_argument("infile")

    h = parser.add_mutually_exclusive_group()
    h.add_argument("--headers", dest="headers", action="store_true")
    h.add_argument("--no-headers", dest="headers", action="store_false")
    parser.set_defaults(headers=False)

    args = parser.parse_args()
    try:
        limit = float(args.limit)
    except ValueError:
        limit = hf.parse_size(args.limit)
    data = read(args.infile, args.headers)
    write(data, args.outfile, limit)


if __name__ == "__main__":
    main()
