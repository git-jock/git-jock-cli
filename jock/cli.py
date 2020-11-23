import click
from jock import __version__
from jock.git import git_command

REPOSITORIES = 'repositories'
GIT_ARGS = 'git_args'
CONTEXT_SETTINGS = dict(ignore_unknown_options=True, )


@click.group()
@click.version_option(__version__)
@click.option('--repository', '-r', type=str, multiple=True,
              help='Repository you wish to run commands on. '
                   'Multiple repositories can be specified '
                   'using multiple flags.')
@click.pass_context
def main(ctx, repository):
    ctx.ensure_object(dict)
    ctx.obj[REPOSITORIES] = tuple(map(lambda x: x.lstrip(" ="), repository))


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def clone(ctx, git_args):
    git_command('clone', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def add(ctx, git_args):
    git_command('add', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def restore(ctx, git_args):
    git_command('restore', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def rm(ctx, git_args):
    git_command('rm', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def branch(ctx, git_args):
    git_command('branch', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def commit(ctx, git_args):
    git_command('commit', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def reset(ctx, git_args):
    git_command('reset', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def switch(ctx, git_args):
    git_command('switch', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def tag(ctx, git_args):
    git_command('tag', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def fetch(ctx, git_args):
    git_command('fetch', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def pull(ctx, git_args):
    git_command('pull', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def push(ctx, git_args):
    git_command('push', ctx.obj[REPOSITORIES], git_args)


@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.argument(GIT_ARGS, nargs=-1, required=False)
def checkout(ctx, git_args):
    git_command('checkout', ctx.obj[REPOSITORIES], git_args)


if __name__ == '__main__':
    main(prog_name='jock')
