import os
import subprocess
import sys

import yaml

from jock.constant import GIT, COMMAND_PATH, IMPORTS, ADDRESS, REPOSITORIES, GROUPS, DATA

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# TODO: get sys temp
TMP_IMPORT_DIR = '/tmp/jock-imports/'


def load_config():
    try:
        with open(os.path.expanduser('~/.jockrc'), 'r') as file:
            config = yaml.load(file, Loader=Loader)
            validate_config(config)
            return config
    except IOError:
        exit_with_message(1, 'Could not read configuration at ~/.jockrc')


def validate_config(config):
    if config is None:
        exit_with_message(1, 'Config is empty')

    assert_config_has_key(config, REPOSITORIES)


def assert_config_has_key(config, key):
    key_merged = merge_config_and_import_key(config, key)

    if len(key_merged.keys()) == 0:
        exit_with_message(1, 'No ' + key + ' found in config')


def merge_config_and_import_key(config, key):
    merged = dict({})

    if key in config:
        merged = {**merged, **config[key]}

    if IMPORTS in config:
        imports = config[IMPORTS]
        for import_name in imports:
            imp = imports[import_name]
            if DATA in imp and key in imp[DATA]:
                merged = {**merged, **config[key]}

    return merged


def import_config():
    config = load_config()
    imports = config[IMPORTS]
    for import_name in imports:
        imp = imports[import_name]
        subprocess.run((GIT, 'clone', '--no-checkout', imp[ADDRESS], TMP_IMPORT_DIR + import_name))
        subprocess.run((GIT, COMMAND_PATH, TMP_IMPORT_DIR + import_name, 'reset'))
        subprocess.run((GIT, COMMAND_PATH, TMP_IMPORT_DIR + import_name, 'checkout', '.jockrc'))
        with open(os.path.expanduser(TMP_IMPORT_DIR + import_name + '/.jockrc'), 'r') as imported_file:
            imported = yaml.load(imported_file, Loader=Loader)

            if DATA not in config[IMPORTS][import_name]:
                config[IMPORTS][import_name][DATA] = dict({})

            config[IMPORTS][import_name][DATA][REPOSITORIES] = imported[REPOSITORIES]
            config[IMPORTS][import_name][DATA][GROUPS] = imported[GROUPS]

            with open(os.path.expanduser('~/.jockrc'), 'w') as config_file:
                yaml.dump(config, config_file, sort_keys=False)

        subprocess.run(('rm', '-rf', TMP_IMPORT_DIR))


def get_selected_repositories(selected_repositories, selected_groups):
    if len(selected_repositories) + len(selected_groups) == 0:
        exit_with_message(1, 'No repositories/groups provided')

    config = load_config()

    repositories = merge_config_and_import_key(config, REPOSITORIES)
    groups = merge_config_and_import_key(config, GROUPS)

    selected = dict({})

    for repo_name in selected_repositories:
        if repo_name in repositories:
            selected[repo_name] = repositories[repo_name]
        else:
            exit_with_message(1, 'Repository "' + repo_name + '" not found in config')

    if config.get(GROUPS) is not None:
        for group_name in selected_groups:
            if group_name in groups:
                for repo_name in groups[group_name][REPOSITORIES]:
                    selected[repo_name] = repositories[repo_name]
            else:
                exit_with_message(1, 'Group "' + group_name + '" not found in config')

    if len(selected) == 0:
        exit_with_message(1, 'No repositories selected')

    return selected


def exit_with_message(exit_code, message):
    print(message)
    sys.exit(exit_code)
