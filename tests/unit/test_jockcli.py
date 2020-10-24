from unittest import TestCase
from unittest.mock import patch

from click.testing import CliRunner

from jock.cli import main
from tests.utils import map_list_with_repository_flag


class TestJockCLI(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch('jock.cli.git_command')
    def test_clone_git_clone(self, git_clone):
        # Given
        repository_addresses = (
            'git@github.com:some-owner/repo-1.git',
            'git@github.com:other-owner/r-e-p-o-2.git',
            'git@github.com:owner3/repo3.git',
        )
        flagged_repositories = \
            map_list_with_repository_flag(repository_addresses)
        # When
        self.runner.invoke(main, flagged_repositories + ('clone',))
        # Then
        git_clone.assert_called_once_with('clone', repository_addresses, ())

    @patch('jock.cli.git_command')
    def test_pull_git_pull(self, git_pull):
        # Given
        repository_names = (
            'repo-1',
            'r-e-p-o-2',
            'repo3'
        )
        flagged_repositories = \
            map_list_with_repository_flag(repository_names)
        # When
        self.runner.invoke(main, flagged_repositories + ('pull',))
        # Then
        git_pull.assert_called_once_with('pull', repository_names, ())

    @patch('jock.cli.git_command')
    def test_fetch_git_fetch(self, git_fetch):
        # Given
        repository_names = (
            'repo-1',
            'r-e-p-o-2',
            'repo3'
        )
        flagged_repositories = \
            map_list_with_repository_flag(repository_names)
        # When
        self.runner.invoke(main, flagged_repositories + ('fetch',))
        # Then
        git_fetch.assert_called_once_with('fetch', repository_names, ())

    @patch('jock.cli.git_command')
    def test_push_git_push(self, git_push):
        # Given
        repository_names = (
            'repo-1',
            'r-e-p-o-2',
            'repo3'
        )
        flagged_repositories = \
            map_list_with_repository_flag(repository_names)
        # When
        self.runner.invoke(main, flagged_repositories + ('push',))
        # Then
        git_push.assert_called_once_with('push', repository_names, ())

    @patch('jock.cli.git_command')
    def test_add_git_add(self, mock_add):
        # Given
        repository_names = (
            'repo-1',
            'r-e-p-o-2',
            'repo3'
        )
        flagged_repositories = \
            map_list_with_repository_flag(repository_names)
        # When
        self.runner.invoke(main, flagged_repositories + ('add',))
        # Then
        mock_add.assert_called_once_with('add', repository_names, ())

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
