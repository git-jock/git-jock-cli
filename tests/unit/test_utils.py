import os
from unittest import TestCase
from unittest.mock import patch

from jock.utils import get_repository_name, get_repository_path


class TestUtils(TestCase):
    def setUp(self):
        self.repository_paths = (
            'git/repo-1',
            '~/git/r-e-p-o-2',
            '/home/jock/git/repo3'
        )

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

    def test_get_repository_name(self):
        for i in range(len(self.repository_addresses)):
            # Given
            expected_name = self.repository_names[i]
            # When
            actual_name = get_repository_name(self.repository_addresses[i])
            # Then
            self.assertEqual(expected_name, actual_name)

    @patch.object(os.path, 'isabs')
    @patch.object(os.path, 'expanduser')
    def test_get_repository_path(self, mock_expanduser, mock_isabs):
        for i in range(len(self.repository_paths)):
            # Given
            mock_expanduser.side_effect = lambda r: '/now/abs/' + r
            mock_isabs.side_effect = lambda _: i % 2 == 0
            expected_path = self.repository_paths[i]
            if i % 2 == 0:
                expected_path = '/now/abs/' + expected_path
            else:
                expected_path = '/now/abs/~/' + expected_path
            # When
            actual_path = get_repository_path(self.repository_paths[i])
            # Then
            self.assertEqual(expected_path, actual_path)
