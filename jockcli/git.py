import subprocess


class Git(object):
    def __init__(self, repositories=None):
        self.repositories = repositories

    def _git_command(self, command=None):
        for repository in self.repositories:
            subprocess.call(['git', command, repository, '../' + repository])

    def clone(self):
        self._git_command('clone')
