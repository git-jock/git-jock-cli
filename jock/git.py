import subprocess

import click


class Git(object):
    def __init__(self, repositories=None):
        self.repositories = repositories

    def clone(self):
        for repository in self.repositories:
            click.echo(
                'Cloning [{}] in [..]'.format(repository)
            )
            subprocess.run(['git', '-C', '..', 'clone', repository])

    def pull(self, git_args=()):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Pulling in [{}]'.format(repository_path))
            subprocess.run(('git', '-C', repository_path, 'pull') + git_args)

    def fetch(self, git_args=()):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Fetching in [{}]'.format(repository_path))
            subprocess.run(('git', '-C', repository_path, 'fetch') + git_args)

    def push(self, git_args=()):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Pushing in [{}]'.format(repository_path))
            subprocess.run(('git', '-C', repository_path, 'push') + git_args)

    def add(self, git_args=()):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Adding in [{}]'.format(repository_path))
            subprocess \
                .run(('git', '-C', repository_path, 'add') + git_args)
