from unittest import TestCase
from unittest.mock import call, patch

from click.testing import CliRunner

from jock.cli import main
from tests.utils import map_list_with_repository_flag


class TestCLI(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch('jock.cli.git_command')
    def test_git_commands(self, git_command):
        # Given
        commands = [
            'clone',
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
        repository_addresses = (
            'git@github.com:some-owner/repo-1.git',
            'git@github.com:other-owner/r-e-p-o-2.git',
            'git@github.com:owner3/repo3.git',
        )
        args = ('-a', '--woof')
        expected_calls = [
            call(commands[0], repository_addresses, args),
            call(commands[1], repository_addresses, args),
            call(commands[2], repository_addresses, args),
            call(commands[3], repository_addresses, args),
            call(commands[4], repository_addresses, args),
            call(commands[5], repository_addresses, args),
            call(commands[6], repository_addresses, args),
            call(commands[7], repository_addresses, args),
            call(commands[8], repository_addresses, args),
            call(commands[9], repository_addresses, args),
            call(commands[10], repository_addresses, args),
            call(commands[11], repository_addresses, args),
            call(commands[12], repository_addresses, args),
        ]
        flagged_repositories = \
            map_list_with_repository_flag(repository_addresses)
        # When
        for command in commands:
            print(flagged_repositories + (command,) + args)
            self.runner.invoke(main, flagged_repositories + (command,) + args)
        # Then
        git_command.assert_has_calls(expected_calls)
        self.assertEqual(git_command.call_count, len(expected_calls))

    @patch('jock.cli.git_command')
    def test_all_repository_flags_work(self, git_mock):
        # Given
        flagged_repository_addresses = (
            '--repository=git@github.com:some-owner/repo-1.git',
            '-r git@github.com:other-owner/r-e-p-o-2.git',
            '-r=git@github.com:owner3/repo3.git'
        )
        expected_repository_addresses = (
            'git@github.com:some-owner/repo-1.git',
            'git@github.com:other-owner/r-e-p-o-2.git',
            'git@github.com:owner3/repo3.git'
        )
        # When
        self.runner.invoke(main, flagged_repository_addresses + ('clone',))
        # Then
        git_mock.assert_called_once_with('clone', expected_repository_addresses, ())
