import subprocess
from unittest import TestCase
from unittest.mock import call, patch

import pytest

from jock.git import git_command, git_common


class TestGit(TestCase):
    def setUp(self):
        self.repository_addresses = (
            'git@github.com:some-owner/repo-1.git',
            'git@github.com:other-owner/r-e-p-o-2.git',
            'git@github.com:owner3/repo3.git'
        )

        self.repository_names = (
            'repo-1',
            'r-e-p-o-2',
            'repo3'
        )

    @staticmethod
    def _get_clone_call(repository_address, git_args=()):
        return call((
                        'git',
                        '-C', '..',
                        'clone',
                        repository_address
                    ) + git_args)

    @patch.object(subprocess, 'run')
    def test_clone_clones_all(self, mock_run):
        # Given
        args = ('--scary', '--bork')
        expected_calls = [
            self._get_clone_call(self.repository_addresses[0], args),
            self._get_clone_call(self.repository_addresses[1], args),
            self._get_clone_call(self.repository_addresses[2], args)
        ]
        # When
        git_command('clone', self.repository_addresses, args)
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(self.repository_addresses))

    @staticmethod
    def _get_common_call(repository_name, command, git_args=()):
        return call(('git', '-C', '../' + repository_name, command) + git_args)

    @patch.object(subprocess, 'run')
    def test_common_call(self, mock_run):
        # Given
        command = 'bark'
        args = ('-a', '--woof')
        expected_calls = [
            self._get_common_call(self.repository_names[0], command, args),
            self._get_common_call(self.repository_names[1], command, args),
            self._get_common_call(self.repository_names[2], command, args)
        ]
        # When
        git_common(command, self.repository_names, args)
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(self.repository_names))

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
