#!/usr/bin/env python3

import typer

def linear(filename: str = "data.txt"):
    print("fitting a linear model from: ", filename)

if __name__ == "__main__":
    typer.run(linear)
