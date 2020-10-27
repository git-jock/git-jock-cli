def add_repository_flag(repository):
    return '--repository=' + repository


def map_list_with_repository_flag(repositories):
    return tuple(map(
        add_repository_flag,
        repositories
    ))
