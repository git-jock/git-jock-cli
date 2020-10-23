import subprocess

import click


def git_clone(repositories, git_args=()):
    for repository in repositories:
        click.echo(
            'Cloning [{}] in [..]'.format(repository)
        )
        subprocess.run(('git', '-C', '..', 'clone', repository) + git_args)


def git_pull(repositories, git_args=()):
    for repository_name in repositories:
        repository_path = '../' + repository_name
        click.echo('Pulling in [{}]'.format(repository_path))
        subprocess.run(('git', '-C', repository_path, 'pull') + git_args)


def git_fetch(repositories, git_args=()):
    for repository_name in repositories:
        repository_path = '../' + repository_name
        click.echo('Fetching in [{}]'.format(repository_path))
        subprocess.run(('git', '-C', repository_path, 'fetch') + git_args)


def git_push(repositories, git_args=()):
    for repository_name in repositories:
        repository_path = '../' + repository_name
        click.echo('Pushing in [{}]'.format(repository_path))
        subprocess.run(('git', '-C', repository_path, 'push') + git_args)


def git_add(repositories, git_args=()):
    for repository_name in repositories:
        repository_path = '../' + repository_name
        click.echo('Adding in [{}]'.format(repository_path))
        subprocess \
            .run(('git', '-C', repository_path, 'add') + git_args)
