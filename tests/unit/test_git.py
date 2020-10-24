import subprocess
from unittest import TestCase
from unittest.mock import call, patch

from jock.git import git_command


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
    def _get_clone_call(repository_address):
        return call((
            'git',
            '-C', '..',
            'clone',
            repository_address
        ))

    @patch.object(subprocess, 'run')
    def test_clone_clones_all(self, mock_run):
        # Given
        expected_calls = map(
            self._get_clone_call,
            self.repository_addresses
        )
        # When
        git_command('clone', self.repository_addresses, ())
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(self.repository_addresses))

    @staticmethod
    def _get_pull_call(repository_name):
        return call(('git', '-C', '../' + repository_name, 'pull'))

    @patch.object(subprocess, 'run')
    def test_pull_pulls_all(self, mock_run):
        # Given
        expected_calls = map(
            self._get_pull_call,
            self.repository_names
        )
        # When
        git_command('pull', self.repository_names, ())
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(self.repository_names))

    @staticmethod
    def _get_fetch_call(repository_name):
        return call(('git', '-C', '../' + repository_name, 'fetch'))

    @patch.object(subprocess, 'run')
    def test_fetch_fetches_all(self, mock_run):
        # Given
        expected_calls = map(
            self._get_fetch_call,
            self.repository_names
        )
        # When
        git_command('fetch', self.repository_names, ())
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(self.repository_names))

    @staticmethod
    def _get_push_call(repository_name):
        return call(('git', '-C', '../' + repository_name, 'push'))

    @patch.object(subprocess, 'run')
    def test_push_pushes_all(self, mock_run):
        # Given
        expected_calls = map(
            self._get_push_call,
            self.repository_names
        )
        # When
        git_command('push', self.repository_names, ())
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(self.repository_names))

    @staticmethod
    def _get_add_call(repository_name):
        return call(('git', '-C', '../' + repository_name, 'add'))

    @patch.object(subprocess, 'run')
    def test_add_adds_all(self, mock_run):
        # Given
        expected_calls = map(
            self._get_add_call,
            self.repository_names
        )
        # When
        git_command('add', self.repository_names, ())
        # Then
        mock_run.assert_has_calls(expected_calls)
        self.assertEqual(mock_run.call_count, len(self.repository_names))
