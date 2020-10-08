#!/usr/bin/env python3
import typer

app = typer.Typer()

@app.command()
def scatter(filename: str):
    '''
        plot points
    '''
    print("plotting points from: ", filename)

@app.command()
def line(filename: str):
    '''
        plot a line
    '''
    print("plotting lines from: ", filename)


if __name__ == "__main__":
    app()