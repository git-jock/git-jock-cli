import re

REPOSITORY_NAME_PATTERN = '([\\w\\.-]+)(.git)/?$'
REPOSITORY_NAME_PATTERN_GROUP = 1


def get_repository_name(repository):
    if match := re.search(REPOSITORY_NAME_PATTERN, repository, re.IGNORECASE):
        return match.group(REPOSITORY_NAME_PATTERN_GROUP)
