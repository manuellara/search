import click

from search.services.svc_for import Search



@click.command()
@click.argument('key')
@click.option("-m", "--mask", type=str, default="*", help="File mask or pattern (e.g. SELA => *SELA*.txt)")
@click.option("-d", "--dir", type=str, default=".", help="Directory to search (e.g. C:\\Users\\Public\\Desktop)")
def cli(mask, dir, key):
    """
    Search a directory for specific word/string
    
    e.g. search for -m SELA -d C:\\Users\\Public\\Desktop 1234567
    """

    result = Search(mask, dir, key)

    result.output()

    result.searchForKey()