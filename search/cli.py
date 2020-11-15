import os
import click 


# Complex CLI class

class ComplexCLI(click.MultiCommand):
    # lists commands avaialble in /commands
    def list_commands(self, ctx):
        commands = []
        commandsFolder = os.path.join(os.path.dirname(__file__), "commands")
        for filename in os.listdir(commandsFolder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename.replace('cmd_', '').replace('.py', ''))
        commands.sort()
        return commands
        
    # returns service based on command name
    def get_command(self, ctx, name):
        try:
            mod = __import__(f"search.commands.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli



@click.command(cls=ComplexCLI)
@click.version_option(version='1.1.0', prog_name='Search by Manuel Lara')
def cli():
    """Search by Manuel Lara"""
    pass