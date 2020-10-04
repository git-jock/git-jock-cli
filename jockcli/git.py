import subprocess

import click

from jockcli.utils import get_repository_name


class Git(object):
    def __init__(self, repositories=None):
        self.repositories = repositories

    def clone(self):
        for repository in self.repositories:
            repository_path = '../' + get_repository_name(repository)
            click.echo(
                'Cloning [{}] into [{}]'.format(repository, repository_path)
            )
            subprocess.run(['git', 'clone', repository, repository_path])

    def pull(self):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Pulling in [{}]'.format(repository_path))
            subprocess.run(['git', '-C', repository_path, 'pull'])

    def fetch(self):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Fetching from [{}]'.format(repository_path))
            subprocess.run(['git', 'fetch', repository_path])

    def push(self):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Pushing to [{}]'.format(repository_path))
            subprocess.run(['git', 'push', repository_path])
