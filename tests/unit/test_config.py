import os
import sys
import tempfile
from unittest import TestCase
from unittest.mock import patch

import yaml

from jock.config import load_config, get_selected_repositories, exit_with_message, validate_config, \
    assert_config_has_key, merge_config_and_import_key, get_tmp_path, fetch_remote_rc
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

    @patch('jock.config.assert_config_has_key')
    @patch('jock.config.exit_with_message')
    def test_validate_exits_when_config_is_none(self, mock_exit, mock_assert_config):
        # Given
        config = None
        # When
        validate_config(config)
        # Then
        mock_exit.assert_called_once_with(1, 'Config is empty')

    @patch('jock.config.assert_config_has_key')
    def test_validate_calls_assert_config_has_key(self, mock_assert_config):
        # Given
        config = dict({})
        # When
        validate_config(config)
        # Then
        mock_assert_config.assert_called_once_with(config, 'repositories')

    @patch('jock.config.merge_config_and_import_key')
    @patch('jock.config.exit_with_message')
    def test_assert_config_has_key_exits_when_key_doesnt_exit(self, mock_exit, mock_merge):
        # Given
        config = None
        key = 'some_key'
        mock_merge.return_value = dict({})
        # When
        assert_config_has_key(config, key)
        # Then
        mock_merge.assert_called_once_with(config, key)
        mock_exit.assert_called_once_with(1, 'No ' + key + ' found in config')

    def test_merge_config_and_import_key_returns_merge(self):
        # Given
        key = 'common_key'
        config_data = dict({'key1': 123})
        import_1_data = dict({'key2': 231})
        import_2_data = dict({'key3': 312})
        input_config = dict({
            key: config_data,
            'imports': dict({
                'import_1': dict({'data': {**dict({key: import_1_data}), **dict({'other_key': 'abc'})}}),
                'import_2': dict({'data': {**dict({'other_key': 'cba'}), **dict({key: import_2_data})}})
            })
        })
        expected = {**config_data, **import_1_data, **import_2_data}
        # When
        actual = merge_config_and_import_key(input_config, key)
        # Then
        self.assertEqual(expected, actual)

    @patch('jock.config.subprocess_steps')
    @patch.object(os.path, 'join')
    @patch('jock.config.get_tmp_path')
    def test_fetch_remote_rc_clones_to_tmp_dir(self, mock_get_tmp, mock_join, mock_subprocess):
        # Given
        import_name = 'import_name'
        address = 'address'
        temp_dir = 'tmp_dir'
        temp_path = 'temp_path'
        mock_get_tmp.return_value = temp_dir
        mock_join.return_value = temp_path
        # When
        fetch_remote_rc(import_name, address)
        # Then
        mock_get_tmp.assert_called_once()
        mock_join.assert_called_once_with(temp_dir, import_name)
        mock_subprocess.assert_called_once_with(
            success_message='Imported "' + import_name + '"',
            error='Import "' + import_name + '" could not be retrieved from "' + address + '"',
            steps=[
                ('git', 'clone', '--no-checkout', address, temp_path),
                ('git', '-C', temp_path, 'reset'),
                ('git', '-C', temp_path, 'checkout', '.jockrc')
            ])

    @patch.object(tempfile, 'gettempdir')
    @patch.object(os.path, 'join')
    def test_get_tmp_path_returns_tmp_with_jock_dir(self, mock_join, mock_gettempdir):
        # Given
        tempdir = 'something'
        mock_gettempdir.return_value = tempdir
        # When
        get_tmp_path()
        # Then
        mock_gettempdir.assert_called_once()
        mock_join.assert_called_once_with(tempdir, 'jock-imports')

    # TODO:import_config

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

    @patch.object(sys, 'exit')
    def test_exit_with_message_prints_message_and_exits_with_code(self, mock_exit):
        # Given
        exit_code = 123
        message = 'some message'
        # When
        exit_with_message(exit_code, message)
        # Then
        mock_exit.assert_called_once_with(exit_code)

    # TODO: subprocesses
