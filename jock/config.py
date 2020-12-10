#!/usr/bin/env python
import os

import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def load_config():
    with open(os.path.expanduser('~/.jockrc'), 'r') as file:
        config = yaml.load(file, Loader=Loader)
        return config


def get_selected_repositories(selected_repositories, selected_groups):
    config = load_config()
    config_groups = config['groups']
    config_repositories = config['repositories']
    print(selected_groups)
    selected_repositories_set = set(selected_repositories)
    # for group in selected_groups:
    #     for sub_
    selected_repository_dict = dict()
    for selected_repository in selected_repositories_set:
        selected_repository_dict[selected_repository] = config_repositories[selected_repository]
