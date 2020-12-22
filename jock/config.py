import os
import subprocess

import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# TODO: get sys temp
TMP_IMPORT_DIR = '/tmp/jock-imports/'


def load_config():
    with open(os.path.expanduser('~/.jockrc'), 'r') as file:
        return yaml.load(file, Loader=Loader)


def import_config():
    config = load_config()
    imports = config['imports']
    for import_name in imports:
        imp = imports[import_name]
        subprocess.run(('git', 'clone', '--no-checkout', imp['address'], TMP_IMPORT_DIR + import_name))
        subprocess.run(('git', '-C', TMP_IMPORT_DIR + import_name, 'reset'))
        subprocess.run(('git', '-C', TMP_IMPORT_DIR + import_name, 'checkout', '.jockrc'))
        with open(os.path.expanduser(TMP_IMPORT_DIR + import_name + '/.jockrc'), 'r') as file:
            print(yaml.load(file, Loader=Loader))
        subprocess.run(('rm', '-rf', TMP_IMPORT_DIR))


def get_selected_repositories(selected_repositories, selected_groups):
    config = load_config()

    repositories = dict({})
    config_repositories = config['repositories']
    for repo_name in selected_repositories:
        repositories[repo_name] = config_repositories[repo_name]

    if config.get('groups') is not None:
        config_groups = config['groups']
        for group_name in selected_groups:
            for repo_name in config_groups[group_name]['repositories']:
                repositories[repo_name] = config_repositories[repo_name]

    return repositories
