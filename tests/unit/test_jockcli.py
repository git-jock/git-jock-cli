from unittest import TestCase
from unittest.mock import patch

from click.testing import CliRunner

from jock.cli import main
from jock.git import Git
from tests.utils import map_list_with_repository_flag


class TestJockCLI(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch('jock.cli.Git')
    def test_clone_git_init(self, git_mock):
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
        git_mock.assert_called_once_with(repository_addresses)

    @patch.object(Git, 'clone')
    def test_clone_git_clone(self, mock_init):
        # Given
        # When
        self.runner.invoke(main, ('--repository=asd', 'clone'))
        # Then
        mock_init.assert_called_once()

    @patch('jock.cli.Git')
    def test_pull_git_init(self, git_mock):
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
        git_mock.assert_called_once_with(repository_names)

    @patch.object(Git, 'pull')
    def test_pull_git_pull(self, mock_init):
        # Given
        # When
        self.runner.invoke(main, ('--repository=dsa', 'pull'))
        # Then
        mock_init.assert_called_once()

    @patch('jock.cli.Git')
    def test_fetch_git_init(self, git_mock):
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
        git_mock.assert_called_once_with(repository_names)

    @patch.object(Git, 'fetch')
    def test_fetch_git_fetch(self, mock_init):
        # Given
        # When
        self.runner.invoke(main, ('--repository=sad', 'fetch'))
        # Then
        mock_init.assert_called_once()

    @patch('jock.cli.Git')
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
        git_mock.assert_called_once_with(expected_repository_addresses)
