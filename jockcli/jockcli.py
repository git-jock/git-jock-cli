import click

from jockcli.git import Git


@click.group()
def jock_cli():
    pass


@jock_cli.command()
@click.argument('repositories', type=str, nargs=-1)
def clone(repositories):
    git = Git(repositories)
    git.clone()


@jock_cli.command()
@click.argument('repositories', type=str, nargs=-1)
def pull(repositories):
    git = Git(repositories)
    git.pull()

@jock_cli.command()
@click.argument('repositories', type=str, nargs=-1)
def fetch(repositories):
    git = Git(repositories)
    git.pull()

if __name__ == '__main__':
    jock_cli()
