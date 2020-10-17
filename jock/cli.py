import click

from jock.git import Git

REPOSITORIES = 'repositories'
GIT_ARGS = 'git_args'


@click.group()
@click.option('--repository', '-r', type=str, multiple=True,
              help='Repository you wish to run commands on. '
                   'Multiple repositories can be specified '
                   'using multiple flags.')
@click.pass_context
def main(ctx, repository):
    ctx.ensure_object(dict)
    ctx.obj[REPOSITORIES] = tuple(map(lambda x: x.lstrip(" ="), repository))


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


@main.command()
@click.pass_context
@click.argument('git_args', nargs=-1, required=False)
def add(ctx, git_args):
    git = Git(ctx.obj[REPOSITORIES])
    git.add(git_args)


if __name__ == '__main__':
    main(prog_name='jock')
