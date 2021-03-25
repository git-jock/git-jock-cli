import subprocess
import sys
import tempfile
from os import path

import yaml

from jock.constant import GIT, COMMAND_PATH, IMPORTS, ADDRESS, REPOSITORIES, GROUPS, DATA

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def load_config():
    try:
        with open(path.expanduser('~/.jockrc'), 'r') as file:
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
                merged = {**merged, **imp[DATA][key]}

    return merged


def get_tmp_path():
    return path.join(tempfile.gettempdir(), 'jock-imports')


def fetch_remote_rc(import_name, address):
    temp_dir = get_tmp_path()
    temp_path = path.join(temp_dir, import_name)

    subprocess_steps(
        success_message='Imported "' + import_name + '"',
        error='Import "' + import_name + '" could not be retrieved from "' + address + '"',
        steps=[
            (GIT, 'clone', '--no-checkout', address, temp_path),
            (GIT, COMMAND_PATH, temp_path, 'reset'),
            (GIT, COMMAND_PATH, temp_path, 'checkout', '.jockrc')
        ])


def merge_config_and_imported(config, import_name, imported):
    if DATA not in config[IMPORTS][import_name]:
        config[IMPORTS][import_name][DATA] = dict({})

    config[IMPORTS][import_name][DATA][REPOSITORIES] = imported[REPOSITORIES]
    config[IMPORTS][import_name][DATA][GROUPS] = imported[GROUPS]

    return config


def fetch_and_merge_remote(config, imports, import_name, temp_dir):
    fetch_remote_rc(import_name, imports[import_name][ADDRESS])

    with open(path.join(temp_dir, import_name, '.jockrc'), 'r') as imported_file:
        imported = yaml.load(imported_file, Loader=Loader)

        config = merge_config_and_imported(config, import_name, imported)

        with open(path.expanduser('~/.jockrc'), 'w') as config_file:
            yaml.dump(config, config_file, sort_keys=False)


def fetch_and_merge_remotes(config, imports, temp_dir):
    for import_name in imports:
        fetch_and_merge_remote(config, imports, import_name, temp_dir)


def import_config():
    config = load_config()
    imports = config[IMPORTS]
    temp_dir = get_tmp_path()

    subprocess.run(('rm', '-rf', temp_dir))

    fetch_and_merge_remotes(config, imports, temp_dir)

    subprocess.run(('rm', '-rf', temp_dir))


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
            if group_name not in groups:
                exit_with_message(1, 'Group "' + group_name + '" not found in config')
            elif REPOSITORIES not in groups[group_name]:
                exit_with_message(1, 'Group "' + group_name + '" has no repository field')
            else:
                for repo_name in groups[group_name][REPOSITORIES]:
                    selected[repo_name] = repositories[repo_name]


    if len(selected) == 0:
        exit_with_message(1, 'No repositories selected')

    return selected


def exit_with_message(exit_code, message):
    print(message)
    sys.exit(exit_code)


def quiet_subprocess(args):
    return subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT).returncode


def subprocess_steps(steps, error=None, success_message=None):
    for args in steps:
        exit_code = quiet_subprocess(args)
        if exit_code > 0:
            if error is not None:
                exit_with_message(1, error)
            return

    if success_message is not None:
        print(success_message)
