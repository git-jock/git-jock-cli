import click

from jock.git import Git

REPOSITORIES = 'repositories'


@click.group()
@click.option('--repository', '-r', type=str, multiple=True,
              help='Repository you wish to run commands on. '
                   'Multiple repositories can be specified '
                   'using multiple flags.')
@click.pass_context
def main(ctx, repository):
    ctx.ensure_object(dict)
    ctx.obj[REPOSITORIES] = repository


@main.command()
@click.pass_context
def clone(ctx):
    git = Git(ctx.obj[REPOSITORIES])
    git.clone()


@main.command()
@click.pass_context
def pull(ctx):
    git = Git(ctx.obj[REPOSITORIES])
    git.pull()


@main.command()
@click.pass_context
def fetch(ctx):
    git = Git(ctx.obj[REPOSITORIES])
    git.fetch()


if __name__ == '__main__':
    main(prog_name='jock')
