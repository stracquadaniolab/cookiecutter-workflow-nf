#!/usr/bin/env python

"""
    fit.py 

    Usage:
        fit.py <inputfile>
"""

from docopt import docopt

def linear(filename: str = "data.txt"):
    print("fitting a linear model from: ", filename)

if __name__ == "__main__":
    arguments = docopt(__doc__, version='fit')
    linear(arguments['<inputfile>'])
