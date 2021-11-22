#!/usr/bin/env python3

import click

@click.group()
def do_something():
    """Simple program to do something"""

    # this will only executed (fired) if any of the commands below
    # are executed as well
    click.echo('I am doing something...')
    
    
@do_something.command()
def sing():
    
    click.echo('I am singing!')
    
    
@do_something.command()
def dance():
    
    click.echo('I am dancing!')
    
    
    
if __name__ == '__main__':
    do_something()
