import click
from search.services import search



class Context:
    def __init__(self, mask, dir, ssid):
        self.mask = mask
        self.dir = dir
        self.ssid = ssid



@click.group()
@click.argument('ssid')
@click.option("-m", "--mask", type=str, default="*.txt", help="File mask or pattern (e.g. *SELA*.txt)")
@click.option("-d", "--dir", type=str, default=".", help="Directory to search (e.g. C:\\Users\\Public\\Desktop)")
@click.pass_context
def cli(ctx, mask, dir, ssid):
    """
    Search a directory for specific word/string
    
    e.g. searchandreplace search -m SELA -d . 1234567 studentid  
    """
    
    ctx.obj = Context(mask, dir, ssid)



@cli.command()
@click.pass_context
def fileMask(ctx):
    click.echo(f"Default filemask: {ctx.obj.mask}")

@cli.command()
@click.pass_context
def directory(ctx):
    click.echo(f"Default directory: {ctx.obj.dir}")

@cli.command()
@click.pass_context
def studentssid(ctx):
    click.secho((f"ID: {ctx.obj.ssid}"), fg='blue')