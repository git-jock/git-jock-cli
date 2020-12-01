#!/usr/bin/env python
import os

import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def load_repositories():
    home = os.environ.get('HOME')

    file_path = home + '/.jockrc'
    with open(file_path, 'r') as file:
        config = yaml.load(file, Loader=Loader)
        # print(config)

        return config['repositories']

        # if repositories is not None:
        #     for repo in repositories:
        #         print(repo['name'])
