import click

from search.services.svc_for import Search

@click.command()
@click.argument('key')
@click.option("-m", "--mask", type=str, default="*", help="File mask or pattern (e.g. KEY => *KEY*.txt)")
@click.option("-d", "--dir", type=str, default=".", help="Directory to search (e.g. C:\\Users\\Public\\Desktop)")
@click.option("-f", "--ftype", type=str, default="txt", help="File type (e.g. csv => *.csv)")

def cli(mask, dir, key, ftype):
    """
    Search a directory for specific word/string
    
    e.g. search for -f csv -m testMask -d C:\\Users\\Public\\Desktop 1234567
    """

    result = Search(mask, dir, key, ftype)

    result.searchForKey()