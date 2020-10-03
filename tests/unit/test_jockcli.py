from unittest import TestCase
from unittest.mock import patch

from click.testing import CliRunner

from jockcli.git import Git
from jockcli.jockcli import jock_cli


class TestJockCLI(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch.object(Git, '__init__')
    def test_clone_git_init(self, mock_init):
        # Given
        repository_addresses = (
            'git@github.com:some-owner/repo-1.git',
            'git@github.com:other-owner/r-e-p-o-2.git',
            'git@github.com:owner3/repo3.git'
        )
        # When
        self.runner.invoke(jock_cli, ('clone',) + repository_addresses)
        # Then
        mock_init.assert_called_once_with(repository_addresses)

    @patch.object(Git, 'clone')
    def test_clone_git_clone(self, mock_init):
        # Given
        # When
        self.runner.invoke(jock_cli, ('clone', 'asd'))
        # Then
        mock_init.assert_called_once()
