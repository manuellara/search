import click
import os
import fnmatch

class Search:
    def __init__(self, mask, dir, key):
        self.__mask = mask
        self.__dir = dir
        self.__key = key

    # TODO: function to search files in directory
    # TODO: verify path exists
    def searchForKey(self):
        for file in os.listdir(self.__dir):
            if fnmatch.fnmatch(file, '*' + self.__key + '*.py'):
                print(file)
    
    def output(self):
        click.echo(f"Filemask: {self.__mask}")
        click.echo(f"Directory: {self.__dir}")
        click.secho((f"ID: {self.__key}"), fg='blue')