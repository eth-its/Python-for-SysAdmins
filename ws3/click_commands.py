#!/usr/bin/env python3

import click

@click.group()
def hello():
    """Simple program that shows the subcommands"""

    print('here in hello')
    
    
@hello.command()
def sub():
    
    print('here in sub')
    
    
@hello.command()
def sub2():
    
    print('here in sub2')
    
    
    
if __name__ == '__main__':
    hello()
