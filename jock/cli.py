import click

from jock.git import git_command

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
@click.argument('git_args', nargs=-1, required=False)
def clone(ctx, git_args):
    git_command('clone', ctx.obj[REPOSITORIES], git_args)


@main.command()
@click.pass_context
@click.argument('git_args', nargs=-1, required=False)
def pull(ctx, git_args):
    git_command('pull', ctx.obj[REPOSITORIES], git_args)


@main.command()
@click.pass_context
@click.argument('git_args', nargs=-1, required=False)
def fetch(ctx, git_args):
    git_command('fetch', ctx.obj[REPOSITORIES], git_args)


@main.command()
@click.pass_context
@click.argument('git_args', nargs=-1, required=False)
def push(ctx, git_args):
    git_command('push', ctx.obj[REPOSITORIES], git_args)


@main.command()
@click.pass_context
@click.argument('git_args', nargs=-1, required=False)
def add(ctx, git_args):
    git_command('add', ctx.obj[REPOSITORIES], git_args)


if __name__ == '__main__':
    main(prog_name='jock')
