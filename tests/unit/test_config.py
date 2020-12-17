import os
from unittest import TestCase
from unittest.mock import patch

import yaml

from jock.config import load_config, get_selected_repositories
from tests.utils import CONFIG_REPOSITORIES, REPOSITORY_NAMES, GROUP_NAMES, CONFIG_GROUPS

open_name = '%s.open' % __name__


class TestConfig(TestCase):
    @patch('builtins.open', read_data='data')
    @patch.object(yaml, 'load')
    @patch.object(os.path, 'expanduser')
    def test_load_config(self, mock_expanduser, mock_yaml, mock_open):
        # Given
        expected_rc_path = '~/.jockrc'
        expected_expanded_path = '/some/path'
        expected_config = dict({'repositories': CONFIG_REPOSITORIES})
        mock_expanduser.return_value = expected_expanded_path
        mock_yaml.return_value = expected_config
        # When
        actual_config = load_config()
        # Then
        mock_expanduser.assert_called_once_with(expected_rc_path)
        mock_open.assert_called_once_with(expected_expanded_path, 'r')
        mock_yaml.assert_called_once()
        self.assertEqual(expected_config, actual_config)

    @patch('jock.config.load_config')
    def test_get_selected_repositories_returns_selected_repos(self, mock_load_config):
        # Given
        selected_repositories = (REPOSITORY_NAMES[0], REPOSITORY_NAMES[2])
        mock_load_config.return_value = dict({
            'repositories': CONFIG_REPOSITORIES,
            'groups': CONFIG_REPOSITORIES
        })
        expected_repositories = dict({
            REPOSITORY_NAMES[0]: CONFIG_REPOSITORIES[REPOSITORY_NAMES[0]],
            REPOSITORY_NAMES[2]: CONFIG_REPOSITORIES[REPOSITORY_NAMES[2]]
        })
        # When
        actual_repositories = get_selected_repositories(selected_repositories, tuple())
        # Then
        mock_load_config.assert_called_once()
        self.assertEqual(expected_repositories, actual_repositories)

    @patch('jock.config.load_config')
    def test_get_selected_repositories_returns_selected_groups(self, mock_load_config):
        # Given
        selected_groups = (GROUP_NAMES[1], GROUP_NAMES[2])
        mock_load_config.return_value = dict({
            'repositories': CONFIG_REPOSITORIES,
            'groups': CONFIG_GROUPS
        })
        expected_repositories = dict({
            REPOSITORY_NAMES[0]: CONFIG_REPOSITORIES[REPOSITORY_NAMES[0]],
            REPOSITORY_NAMES[2]: CONFIG_REPOSITORIES[REPOSITORY_NAMES[2]]
        })
        # When
        actual_repositories = get_selected_repositories(tuple(), selected_groups)
        # Then
        mock_load_config.assert_called_once()
        self.assertEqual(expected_repositories, actual_repositories)

    @patch('jock.config.load_config')
    def test_get_selected_repositories_returns_both_selections(self, mock_load_config):
        # Given
        selected_repositories = (REPOSITORY_NAMES[1],)
        selected_groups = (GROUP_NAMES[1], GROUP_NAMES[2])
        mock_load_config.return_value = dict({
            'repositories': CONFIG_REPOSITORIES,
            'groups': CONFIG_GROUPS
        })
        expected_repositories = dict({
            REPOSITORY_NAMES[0]: CONFIG_REPOSITORIES[REPOSITORY_NAMES[0]],
            REPOSITORY_NAMES[1]: CONFIG_REPOSITORIES[REPOSITORY_NAMES[1]],
            REPOSITORY_NAMES[2]: CONFIG_REPOSITORIES[REPOSITORY_NAMES[2]]
        })
        # When
        actual_repositories = get_selected_repositories(selected_repositories, selected_groups)
        # Then
        mock_load_config.assert_called_once()
        self.assertEqual(expected_repositories, actual_repositories)
