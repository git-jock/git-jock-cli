import os
from unittest import TestCase
from unittest.mock import patch

import yaml

from jock.config import load_config
from tests.utils import CONFIG_REPOSITORIES

CONFIG = dict({'repositories': CONFIG_REPOSITORIES})

open_name = '%s.open' % __name__


class TestConfig(TestCase):
    @patch('builtins.open', read_data='data')
    @patch.object(yaml, 'load')
    @patch.object(os.path, 'expanduser')
    def test_load_config(self, mock_expanduser, mock_yaml, mock_open):
        # Given
        expected_rc_path = '~/.jockrc'
        expected_expanded_path = '/some/path'
        mock_expanduser.return_value = expected_expanded_path
        mock_yaml.return_value = CONFIG
        # When
        actual_config = load_config()
        # Then
        mock_expanduser.assert_called_once_with(expected_rc_path)
        mock_open.assert_called_once_with(expected_expanded_path, 'r')
        mock_yaml.assert_called_once()
        self.assertEqual(CONFIG, actual_config)
