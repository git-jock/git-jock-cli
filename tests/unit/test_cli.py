from unittest import TestCase
from unittest.mock import call, patch

from click.testing import CliRunner

from jock.cli import main
from tests.utils import map_list_with_repository_flag, CONFIG_REPOSITORIES, REPOSITORY_NAMES


class TestCLI(TestCase):

    def setUp(self):
        self.runner = CliRunner()

    @patch('jock.cli.get_selected_repositories')
    @patch('jock.cli.git_command')
    def test_git_commands(self, git_command, get_selected_repositories_mock):
        # Given
        get_selected_repositories_mock.return_value = CONFIG_REPOSITORIES
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

        args = ('-a', '--woof')
        expected_calls = [
            call(commands[0], CONFIG_REPOSITORIES, args),
            call(commands[1], CONFIG_REPOSITORIES, args),
            call(commands[2], CONFIG_REPOSITORIES, args),
            call(commands[3], CONFIG_REPOSITORIES, args),
            call(commands[4], CONFIG_REPOSITORIES, args),
            call(commands[5], CONFIG_REPOSITORIES, args),
            call(commands[6], CONFIG_REPOSITORIES, args),
            call(commands[7], CONFIG_REPOSITORIES, args),
            call(commands[8], CONFIG_REPOSITORIES, args),
            call(commands[9], CONFIG_REPOSITORIES, args),
            call(commands[10], CONFIG_REPOSITORIES, args),
            call(commands[11], CONFIG_REPOSITORIES, args),
            call(commands[12], CONFIG_REPOSITORIES, args),
        ]
        flagged_repositories = \
            map_list_with_repository_flag(REPOSITORY_NAMES)
        # When
        for command in commands:
            print(flagged_repositories + (command,) + args)
            self.runner.invoke(main, flagged_repositories + (command,) + args)
        # Then
        git_command.assert_has_calls(expected_calls)
        self.assertEqual(git_command.call_count, len(expected_calls))

    @patch('jock.cli.get_selected_repositories')
    @patch('jock.cli.git_command')
    def test_all_repository_flags_work(self, git_mock, get_selected_repositories_mock):
        # Given
        get_selected_repositories_mock.return_value = CONFIG_REPOSITORIES
        flagged_repository_names = (
            '--repository=' + REPOSITORY_NAMES[0],
            '-r ' + REPOSITORY_NAMES[1],
            '-r=' + REPOSITORY_NAMES[2]
        )
        # When
        self.runner.invoke(main, flagged_repository_names + ('clone',))
        # Then
        git_mock.assert_called_once_with('clone', CONFIG_REPOSITORIES, ())
