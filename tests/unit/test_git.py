import subprocess
from unittest import TestCase
from unittest.mock import call, patch

import pytest

from jock.git import git_command, git_common

REPOSITORY_NAMES = (
    'repo-1',
    'r-e-p-o-2',
    'repo3',
)

CONFIG_REPOSITORIES = dict({
    REPOSITORY_NAMES[0]: dict({
        'address': 'git@github.com:some-owner/repo-1.git',
        'location': 'git/repo-1',
    }),
    REPOSITORY_NAMES[1]: dict({
        'address': 'git@github.com:other-owner/r-e-p-o-2.git',
        'location': '~/git/r-e-p-o-2',
    }),
    REPOSITORY_NAMES[2]: dict({
        'address': 'git@github.com:owner3/repo3.git',
        'location': '/usr/jock/git/repo3',
    }),
})


class TestGit(TestCase):
    @staticmethod
    def _get_clone_call(name, git_args=()):
        repository = CONFIG_REPOSITORIES[name]
        return call((
                        'git',
                        'clone',
                        repository['address'],
                        repository['location']
                    ) + git_args)

    # @patch('jock.git.get_repository_path') # TODO: Mock
    @patch.object(subprocess, 'run')
    def test_clone_clones_all(self, mock_run):
        # Given
        args = ('--scary', '--bork')
        expected_calls = [
            self._get_clone_call(REPOSITORY_NAMES[0], args),
            self._get_clone_call(REPOSITORY_NAMES[1], args),
            self._get_clone_call(REPOSITORY_NAMES[2], args)
        ]
        # When
        git_command('clone', CONFIG_REPOSITORIES, REPOSITORY_NAMES, args)
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(REPOSITORY_NAMES))

    @staticmethod
    def _get_common_call(repository_name, command, git_args=()):
        return call(('git', '-C', '../' + repository_name, command) + git_args)

    @patch('jock.git.get_repository_path')
    @patch.object(subprocess, 'run')
    def test_common_call(self, mock_run, mock_get_repository_path):
        # Given
        command = 'bark'
        args = ('-a', '--woof')
        expected_calls = [
            self._get_common_call(REPOSITORY_NAMES[0], command, args),
            self._get_common_call(REPOSITORY_NAMES[1], command, args),
            self._get_common_call(REPOSITORY_NAMES[2], command, args)
        ]
        # When
        git_common(command, CONFIG_REPOSITORIES, REPOSITORY_NAMES, args)
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(REPOSITORY_NAMES))

    @patch.object(subprocess, 'run')
    def test_git_command(self, mock_run):
        # Given
        common_commands = [
            'add',
            'restore',
            'rm',
            'branch',
            'commit',
            'reset',
            'switch',
            'tag',
            'fetch',
            'pull',
            'push',
            'checkout',
        ]
        args = ('-a', '--woof')
        repository = 'some-repo'
        expected_calls = [
            self._get_common_call(repository, common_commands[0], args),
            self._get_common_call(repository, common_commands[1], args),
            self._get_common_call(repository, common_commands[2], args),
            self._get_common_call(repository, common_commands[3], args),
            self._get_common_call(repository, common_commands[4], args),
            self._get_common_call(repository, common_commands[5], args),
            self._get_common_call(repository, common_commands[6], args),
            self._get_common_call(repository, common_commands[7], args),
            self._get_common_call(repository, common_commands[8], args),
            self._get_common_call(repository, common_commands[9], args),
            self._get_common_call(repository, common_commands[10], args),
            self._get_common_call(repository, common_commands[11], args),
            self._get_clone_call(repository, args)
        ]
        # When
        for command in common_commands:
            git_command(command, (repository,), args)
        git_command('clone', (repository,), args)
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(expected_calls))

    def test_git_command_exits(self):
        # Given
        unknown_command = 'grrrr'
        expected_exit_code = 1
        # When
        with pytest.raises(SystemExit) as wrapped_exit:
            git_command(unknown_command, ('repository',), ())
        # Then
        self.assertEqual(expected_exit_code, wrapped_exit.value.code)
