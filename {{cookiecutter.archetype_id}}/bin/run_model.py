#!/usr/bin/env python3

"""
    run_model.py 

    Usage:
        run_model.py <inputfile>
"""

from docopt import docopt

def linear(filename: str = "data.txt"):
    print("fitting a linear model from: ", filename)

if __name__ == "__main__":
    arguments = docopt(__doc__, version='fit')
    linear(arguments['<inputfile>'])
