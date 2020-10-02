import subprocess

import click
from utils import get_repository_name


class Git(object):
    def __init__(self, repositories=None):
        self.repositories = repositories

    def clone(self):
        for repository in self.repositories:
            repository_path = '../' + get_repository_name(repository)
            click.echo('Cloning [{}] into [{}]'.format(repository, repository_path))
            subprocess.call(['git', 'clone', repository, repository_path])

    def pull(self):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Pulling in [{}]'.format(repository_path))
            subprocess.call(['git', '-C', repository_path, 'pull'])
