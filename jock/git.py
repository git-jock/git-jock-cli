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
            subprocess.run(['git', '--exec-path=..', 'clone', repository])

    def pull(self):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Pulling in [{}]'.format(repository_path))
            subprocess.run(['git', '--exec-path=' + repository_path, 'pull'])

    def fetch(self):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Fetching in [{}]'.format(repository_path))
            subprocess.run(['git', '--exec-path=' + repository_path, 'fetch'])

    def push(self):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Pushing in [{}]'.format(repository_path))
            subprocess.run(['git', '--exec-path=' + repository_path, 'push'])

    def add(self, git_args=None):
        for repository_name in self.repositories:
            repository_path = '../' + repository_name
            click.echo('Adding in [{}]'.format(repository_path))
            subprocess \
                .run(('git', '--exec-path=' + repository_path, 'add') + ('.',))
