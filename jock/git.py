import subprocess

import click


def git_common(command, repositories, git_args=()):
    for repository_name in repositories:
        repository_path = '../' + repository_name
        click.echo('Pulling in [{}]'.format(repository_path))
        subprocess.run(('git', '-C', repository_path, command) + git_args)


def git_clone(repositories, git_args=()):
    for repository in repositories:
        click.echo(
            'Cloning [{}] in [..]'.format(repository)
        )
        subprocess.run(('git', '-C', '..', 'clone', repository) + git_args)


GIT_COMMANDS = {
    'clone': lambda c, r, a: git_clone(r, a),
    'pull': git_common,
    'fetch': git_common,
    'add': git_common,
    'push': git_common,
}


def git_command(command, repositories, git_args):
    release_func = GIT_COMMANDS.get(command)

    if release_func is None:
        print('Unsupported command ' + command)

    release_func(command, repositories, git_args)
