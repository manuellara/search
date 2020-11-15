import click
import os
import fnmatch

class Search:
    def __init__(self, mask, dir, key):
        self.__mask = mask
        self.__dir = dir
        self.__key = key

    # TODO: function to search files in directory
    def searchForKey(self):
        try:
            # if dir exists, iterate through files directory
            for file in os.listdir(self.__dir):
                # if file that matches pattern
                if fnmatch.fnmatch(file, '*' + self.__mask + '*.md'):
                    click.secho((f"FOUND: {file}"), fg='red')
                    # if file is truely a file
                    if os.path.isfile(file):
                        try:
                            click.secho((f"IS A FILE: {file}"), fg='green')
                        except Exception as e:
                            pass
        except Exception as e:
            # throws exception
            click.secho((f"PATH DOES NOT EXIST: {self.__dir}"), fg='red')
        
    
    def output(self):
        click.echo(f"Filemask: {self.__mask}")
        click.echo(f"Directory: {self.__dir}")
        click.secho((f"ID: {self.__key}"), fg='blue')