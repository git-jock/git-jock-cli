import os
import re

REPOSITORY_NAME_PATTERN = '([\\w\\.-]+)(.git)/?$'
REPOSITORY_NAME_PATTERN_GROUP = 1


def get_repository_name(repository):
    match = re.search(REPOSITORY_NAME_PATTERN, repository, re.IGNORECASE)
    if match:
        return match.group(REPOSITORY_NAME_PATTERN_GROUP)


def get_repository_path(path):
    expanded = os.path.expanduser(path)
    if not os.path.isabs(expanded):
        expanded = os.path.expanduser('~/' + path)
    return expanded
