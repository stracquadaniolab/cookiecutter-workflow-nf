#!/usr/bin/env python3

"""
    plots.py

    Usage:
        plots.py (scatter|line) <filename>


"""


from docopt import docopt

def scatter(filename: str):
    '''
        plot points
    '''
    print("plotting points from: ", filename)


def line(filename: str):
    '''
        plot a line
    '''
    print("plotting lines from: ", filename)


if __name__ == "__main__":
    arguments = docopt(__doc__, version='plots')
    if arguments['line']:
        line(arguments["<filename>"])
    else:
        scatter(arguments["<filename>"])

