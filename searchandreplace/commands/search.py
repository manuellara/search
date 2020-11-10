import click



class Context:
    def __init__(self, mask, dir):
        self.mask = mask
        self.dir = dir



@click.group(chain=True)
@click.option("-m", "--mask", type=str, default="*.txt", help="File mask or pattern (e.g. *.txt)")
@click.option("-d", "--dir", type=str, default=".", help="Directory to search (e.g. C:\\Users\\Public\\Desktop)")
@click.pass_context
def cli(ctx, mask, dir):
    """Search a directory for specific word/string"""
    ctx.obj = Context(mask, dir)




@cli.command('filemask')
@click.pass_context
def fileMask(ctx):
    click.echo(f"Default filemask: {ctx.obj.mask}")


@cli.command('dir')
@click.pass_context
def directory(ctx):
    click.echo(f"Default directory: {ctx.obj.dir}")


@cli.command()
@click.pass_context
def find(ctx):
    click.echo("finding string...")
