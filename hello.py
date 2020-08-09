#!/usr/bin/env python
import click

def api(key,phrase):
    buslogic = "%s is great %s" % (key, phrase) #pretend api call
    return buslogic

#print(api("1234", "John"))

@click.command()
@click.option('--key')
@click.option('--phrase')
def callapi(key, phrase):
    results = api(key,phrase)
    print(results)
    
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    callapi()

