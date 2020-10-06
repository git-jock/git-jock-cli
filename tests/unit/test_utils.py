from unittest import TestCase

from jock.utils import get_repository_name


class TestUtils(TestCase):
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

    def test_get_repository_name(self):
        for i in range(len(self.repository_addresses)):
            # Given
            expected_name = self.repository_names[i]
            # When
            actual_name = get_repository_name(self.repository_addresses[i])
            # Then
            self.assertEqual(expected_name, actual_name)
