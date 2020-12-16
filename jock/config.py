#!/usr/bin/env python
import os

import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def load_config():
    with open(os.path.expanduser('~/.jockrc'), 'r') as file:
        return yaml.load(file, Loader=Loader)


def get_selected_repositories(selected_repositories, selected_groups):
    config = load_config()
    config_groups = config['groups']
    config_repositories = config['repositories']

    repositories = dict({})

    for repo_name in selected_repositories:
        repositories[repo_name] = config_repositories[repo_name]

    for group_name in selected_groups:
        for repo_name in config_groups[group_name]['repositories']:
            repositories[repo_name] = config_repositories[repo_name]

    return repositories
