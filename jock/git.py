import subprocess
import sys

import click


def git_common(command, repositories, git_args=()):
    for repository_name in repositories:
        repository_path = '../' + repository_name
        click.echo('Executing [{}] in [{}]'.format(command, repository_path))
        subprocess.run(('git', '-C', repository_path, command) + git_args)


def git_clone(repositories, git_args=()):
    for repository in repositories:
        click.echo(
            'Cloning [{}] in [..]'.format(repository)
        )
        subprocess.run(('git', '-C', '..', 'clone', repository) + git_args)


GIT_COMMANDS = {
    'clone': lambda c, r, a: git_clone(r, a),
    'add': git_common,
    'restore': git_common,
    'rm': git_common,
    'branch': git_common,
    'commit': git_common,
    'reset': git_common,
    'switch': git_common,
    'tag': git_common,
    'fetch': git_common,
    'pull': git_common,
    'push': git_common,
    'checkout': git_common,
}


def git_command(command, repositories, git_args):
    release_func = GIT_COMMANDS.get(command)

    if release_func is None:
        print('Unsupported command ' + command)
        sys.exit(1)

    release_func(command, repositories, git_args)
