import click
from git import Git


@click.group()
def cli():
    pass


@cli.command()
@click.argument('repositories', type=str, nargs=-1)
def clone(repositories):
    git = Git(repositories)
    git.clone()


if __name__ == '__main__':
    cli()
