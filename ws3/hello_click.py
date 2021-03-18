#!/usr/bin/env python3

import click

@click.command()
@click.option('--count',  '-c', default=1, help='Number of greetings.')
@click.option('--polite', '-p', is_flag=True)
@click.option('--name',   '-n', prompt='Your name', help='The person to greet.')
def hello(count, polite, name):
    """Simple program that greets NAME for a total of COUNT times."""

    if polite:
        greeting = 'Your Serene Highness'
    else:
        greeting = 'Hello'

    for x in range(count):
        click.echo(f'{greeting} {name}!')

if __name__ == '__main__':
    hello()
