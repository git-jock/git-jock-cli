import click
import subprocess
from utils import get_repository_name


class Git(object):
    def __init__(self, repositories=None):
        self.repositories = repositories

    def _git_command(self, command=None):
        for repository in self.repositories:
            repository_path = '../' + get_repository_name(repository)
            click.echo('Cloning [{}] into [{}]'.format(repository, repository_path))
            subprocess.call(['git', command, repository, repository_path])

    def clone(self):
        self._git_command('clone')
