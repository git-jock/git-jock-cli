import click

from jock import __version__
from jock.config import get_selected_repositories
from jock.git import git_command

CONFIG_REPOSITORIES = 'config_repositories'
SELECTED_REPOSITORIES = 'selected_repositories'
GIT_ARGS = 'git_args'
CONTEXT_SETTINGS = dict(ignore_unknown_options=True, )


@click.group()
@click.version_option(__version__)
@click.option('--repository', '-r', type=str, multiple=True,
              help='Repository, specified in ~/.jockrc, '
                   'you wish to run commands on. Multiple '
                   'repositories can be specified using '
                   'multiple flags.')
@click.option('--group', '-g', type=str, multiple=True,
              help='Group of repositories, specified in '
                   '~/.jockrc, you wish to run commands on.'
                   'Multiple  groups can be specified using '
                   'multiple flags.')
@click.pass_context
def main(ctx, repository, group):
    ctx.ensure_object(dict)

    repositories = tuple(map(lambda x: x.lstrip(" ="), repository))
    groups = tuple(map(lambda x: x.lstrip(" ="), group))

    ctx.obj[SELECTED_REPOSITORIES] = get_selected_repositories(repositories, groups)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def clone(ctx, git_args):
    git_command('clone', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def add(ctx, git_args):
    git_command('add', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def restore(ctx, git_args):
    git_command('restore', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def rm(ctx, git_args):
    git_command('rm', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def branch(ctx, git_args):
    git_command('branch', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def commit(ctx, git_args):
    git_command('commit', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def reset(ctx, git_args):
    git_command('reset', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def switch(ctx, git_args):
    git_command('switch', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def tag(ctx, git_args):
    git_command('tag', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def fetch(ctx, git_args):
    git_command('fetch', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def pull(ctx, git_args):
    git_command('pull', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def push(ctx, git_args):
    git_command('push', ctx.obj[SELECTED_REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def checkout(ctx, git_args):
    git_command('checkout', ctx.obj[SELECTED_REPOSITORIES], git_args)


if __name__ == '__main__':
    main(prog_name='jock')
