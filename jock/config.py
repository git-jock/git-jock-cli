import os
import subprocess

import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

IMPORTS = 'imports'
DATA = 'data'
REPOSITORIES = 'repositories'
GROUPS = 'groups'
LOCATION = 'location'
ADDRESS = 'address'

# TODO: get sys temp
TMP_IMPORT_DIR = '/tmp/jock-imports/'


def load_config():
    with open(os.path.expanduser('~/.jockrc'), 'r') as file:
        return yaml.load(file, Loader=Loader)


def import_config():
    config = load_config()
    imports = config[IMPORTS]
    for import_name in imports:
        imp = imports[import_name]
        subprocess.run(('git', 'clone', '--no-checkout', imp['address'], TMP_IMPORT_DIR + import_name))
        subprocess.run(('git', '-C', TMP_IMPORT_DIR + import_name, 'reset'))
        subprocess.run(('git', '-C', TMP_IMPORT_DIR + import_name, 'checkout', '.jockrc'))
        with open(os.path.expanduser(TMP_IMPORT_DIR + import_name + '/.jockrc'), 'r') as imported_file:
            imported = yaml.load(imported_file, Loader=Loader)

            if DATA not in config[IMPORTS][import_name]:
                config[IMPORTS][import_name][DATA] = dict({})

            config[IMPORTS][import_name][DATA][REPOSITORIES] = imported[REPOSITORIES]
            config[IMPORTS][import_name][DATA][GROUPS] = imported[GROUPS]

            with open(os.path.expanduser('~/.jockrc'), 'w') as config_file:
                yaml.dump(config, config_file, sort_keys=False)

        subprocess.run(('rm', '-rf', TMP_IMPORT_DIR))


def get_repositories(config, selected_repositories, selected_groups):
    repositories = dict({})
    config_repositories = config[REPOSITORIES]
    for repo_name in selected_repositories:
        repositories[repo_name] = config_repositories[repo_name]

    if config.get(GROUPS) is not None:
        config_groups = config[GROUPS]
        for group_name in selected_groups:
            if group_name in config_groups:
                for repo_name in config_groups[group_name][REPOSITORIES]:
                    repositories[repo_name] = config_repositories[repo_name]

    return repositories


def get_selected_repositories(selected_repositories, selected_groups):
    config = load_config()

    local_repos = get_repositories(config, selected_repositories, selected_groups)

    if config.get(IMPORTS) is not None:
        config_imports = config[IMPORTS]

        for import_name in config_imports:
            import_repos = get_repositories(config_imports[import_name][DATA], selected_repositories, selected_groups)
            local_repos = {**local_repos, **import_repos}

    return local_repos
