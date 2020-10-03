import subprocess
import unittest
from unittest.mock import call, patch

from jockcli.git import Git


class TestGit(unittest.TestCase):
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

    @patch.object(subprocess, 'run')
    def test_clone_clones_all(self, mock_run):
        # Given
        git = Git(self.repository_addresses)
        expected_calls = [
            call(['git', 'clone', self.repository_addresses[0], '../' + self.repository_names[0]]),
            call(['git', 'clone', self.repository_addresses[1], '../' + self.repository_names[1]]),
            call(['git', 'clone', self.repository_addresses[2], '../' + self.repository_names[2]])
        ]
        # When
        git.clone()
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(expected_calls))

    @patch.object(subprocess, 'run')
    def test_pull_pulls_all(self, mock_run):
        # Given
        git = Git(self.repository_names)
        expected_calls = [
            call(['git', '-C', '../' + self.repository_names[0], 'pull']),
            call(['git', '-C', '../' + self.repository_names[1], 'pull']),
            call(['git', '-C', '../' + self.repository_names[2], 'pull'])
        ]
        # When
        git.pull()
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(expected_calls))
