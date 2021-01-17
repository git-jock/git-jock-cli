import subprocess
import sys

import click

from jock.config import ADDRESS, LOCATION
from jock.utils import get_repository_path

GIT = 'git'
COMMAND_PATH = '-C'


def git_common(command, selected_repositories, git_args=()):
    for repository_name in selected_repositories:
        repository = selected_repositories[repository_name]
        repository_path = get_repository_path(repository[LOCATION])
        click.echo('Executing [{}] in [{}]'.format(command, repository_path))
        subprocess.run((GIT, COMMAND_PATH, repository_path, command) + git_args)


def git_clone(selected_repositories, git_args=()):
    for repository_name in selected_repositories:
        repository = selected_repositories[repository_name]
        repository_path = get_repository_path(repository[LOCATION])
        click.echo(
            'Cloning [{}] in [{}]'.format(repository_name, repository_path)
        )
        subprocess.run((GIT, 'clone', repository[ADDRESS], repository_path) + git_args)


GIT_COMMANDS = {
    'clone': lambda _, sr, a: git_clone(sr, a),
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


def git_command(command, selected_repositories, git_args):
    git_func = GIT_COMMANDS.get(command)

    if git_func is None:
        print('Unsupported command ' + command)
        sys.exit(1)

    git_func(command, selected_repositories, git_args)
