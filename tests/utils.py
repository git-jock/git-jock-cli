def add_repository_flag(repository):
    return '--repository=' + repository


def map_list_with_repository_flag(repositories):
    return tuple(map(
        add_repository_flag,
        repositories
    ))


REPOSITORY_NAMES = (
    'repo-1',
    'r-e-p-o-2',
    'repo3',
)

GROUP_NAMES = (
    'oneandtwo',
    'oneandthree',
    'three',
)

CONFIG_REPOSITORIES = dict({
    REPOSITORY_NAMES[0]: dict({
        'address': 'git@github.com:some-owner/repo-1.git',
        'location': 'git/repo-1',
    }),
    REPOSITORY_NAMES[1]: dict({
        'address': 'git@github.com:other-owner/r-e-p-o-2.git',
        'location': '~/git/r-e-p-o-2',
    }),
    REPOSITORY_NAMES[2]: dict({
        'address': 'git@github.com:owner3/repo3.git',
        'location': '/home/jock/git/repo3',
    }),
})

CONFIG_GROUPS = dict({
    GROUP_NAMES[0]: {'repositories': [REPOSITORY_NAMES[0], REPOSITORY_NAMES[1]]},
    GROUP_NAMES[1]: {'repositories': [REPOSITORY_NAMES[0], REPOSITORY_NAMES[2]]},
    GROUP_NAMES[2]: {'repositories': [REPOSITORY_NAMES[2]]},
})
