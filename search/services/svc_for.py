import click
import os
import fnmatch

class Search:
    def __init__(self, mask, dir, key, ftype):
        self.__mask = mask
        self.__dir = dir
        self.__key = key
        self.__ftype = ftype

    # TODO: function to search files in directory
    def searchForKey(self):
        try:
            # if dir exists, iterate through files directory
            for file in os.listdir(self.__dir):
                # if file that matches pattern
                if fnmatch.fnmatch(file, '*' + self.__mask + '*.' + self.__ftype):
                    # if file is truely a file
                    if os.path.isfile(file):
                        # open file and read lines
                        with open (file) as lines:
                            for line in lines:
                                # if the key is in the line, print the line
                                if self.__key in line:
                                    # prints filename 
                                    click.secho((f"FOUND: {file}"), fg='red')
                                    # prints line containing key 
                                    print(line.rstrip())
        except Exception as e:
            # throws exception
            click.secho((f"PATH DOES NOT EXIST: {self.__dir}"), fg='red')
        
    def output(self):
        click.echo(f"Filemask: {self.__mask}")
        click.echo(f"Directory: {self.__dir}")
        click.echo(f"Directory: {self.__ftype}")
        click.secho((f"ID: {self.__key}"), fg='blue')