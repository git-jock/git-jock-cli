#!/usr/bin/env python
import os

import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def load_repositories():
    with open(os.path.expanduser('~/.jockrc'), 'r') as file:
        config = yaml.load(file, Loader=Loader)
        return config['repositories']


def get_repository_path(path):
    expanded = os.path.expanduser(path)
    if not os.path.isabs(expanded):
        expanded = os.path.expanduser('~/' + path)
    return expanded
