import click

from jock.git import Git


@click.group()
def main():
    pass


@main.command()
@click.argument('repositories', type=str, nargs=-1)
def clone(repositories):
    git = Git(repositories)
    git.clone()


@main.command()
@click.argument('repositories', type=str, nargs=-1)
def pull(repositories):
    git = Git(repositories)
    git.pull()


@main.command()
@click.argument('repositories', type=str, nargs=-1)
def fetch(repositories):
    git = Git(repositories)
    git.fetch()


@main.command()
@click.argument('repositories', type=str, nargs=-1)
def push(repositories):
    git = Git(repositories)
    git.push()


if __name__ == '__main__':
    main()
