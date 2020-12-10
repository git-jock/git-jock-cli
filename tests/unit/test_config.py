import os
from unittest import TestCase
from unittest.mock import patch

import yaml

from jock.config import load_config
from tests.utils import CONFIG_REPOSITORIES

CONFIG = dict({'repositories': CONFIG_REPOSITORIES})

open_name = '%s.open' % __name__


class TestConfig(TestCase):
    @patch("builtins.open", read_data="data")
    @patch.object(yaml, 'load')
    @patch.object(os.path, 'expanduser')
    def test_load_repositories(self, mock_expanduser, mock_yaml, mock_open):
        # Given
        expected_rc_path = '~/.jockrc'
        mock_expanduser.return_value = '/some/path'
        mock_yaml.return_value = CONFIG
        # When
        actual_repositories = load_config()
        # Then
        self.assertEqual(CONFIG_REPOSITORIES, actual_repositories)
