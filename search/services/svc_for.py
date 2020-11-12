import click


class Search:
    def __init__(self, mask, dir, key):
        self.__mask = mask
        self.__dir = dir
        self.__key = key

    # TODO: function to search files in directory
    def searchDir(self):
        pass
    
    def output(self):
        click.echo(f"Default filemask: {self.__mask}")
        click.echo(f"Default directory: {self.__dir}")
        click.secho((f"ID: {self.__key}"), fg='blue')