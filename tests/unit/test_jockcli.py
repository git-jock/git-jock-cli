from unittest import TestCase
from unittest.mock import patch

from click.testing import CliRunner

from jock.git import Git
from jock.cli import main


class TestJockCLI(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch('jock.cli.Git')
    def test_clone_git_init(self, git_mock):
        # Given
        repository_addresses = (
            'git@github.com:some-owner/repo-1.git',
            'git@github.com:other-owner/r-e-p-o-2.git',
            'git@github.com:owner3/repo3.git'
        )
        # When
        self.runner.invoke(main, ('clone',) + repository_addresses)
        # Then
        git_mock.assert_called_once_with(repository_addresses)

    @patch.object(Git, 'clone')
    def test_clone_git_clone(self, mock_init):
        # Given
        # When
        self.runner.invoke(main, ('clone', 'asd'))
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
        # When
        self.runner.invoke(main, ('pull',) + repository_names)
        # Then
        git_mock.assert_called_once_with(repository_names)

    @patch.object(Git, 'pull')
    def test_pull_git_pull(self, mock_init):
        # Given
        # When
        self.runner.invoke(main, ('pull', 'dsa'))
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
        # When
        self.runner.invoke(main, ('fetch',) + repository_names)
        # Then
        git_mock.assert_called_once_with(repository_names)

    @patch.object(Git, 'fetch')
    def test_fetch_git_fetch(self, mock_init):
        # Given
        # When
        self.runner.invoke(main, ('fetch', 'dsa'))
        # Then
        mock_init.assert_called_once()
