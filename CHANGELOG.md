# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to 
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Note, "non-notable" changes may be small patches with no noticeable effect to the user.

## Unreleased


## 0.2.0 2020-12-17
### Added
- Configuration file
    - `~/.jockrc` stores repositories and groups for commands to be run on (YAML formatted)
    - `--group` can be used to refer to groups of repositories (same usage as repositories)
  
### Changed
- `--respository` now refers to repository stored in `.jockrc`, previously looked at adjacent directories


## 0.1.0 2020-11-27
### Added
- Initial usage: `jock [OPTIONS] COMMAND [ARGS]`
    - OPTIONS can be `--version`, `--help` or a list of repositories such as `-r git-jock-cli` or `--repository 
    some-service`
    - COMMAND is any of the currently supported git commands: `add`, `branch`, `checkout`, `clone`, `commit`, `fetch`, 
    `pull`, `push`, `reset`, `restore`, `rm`, `switch`, or `tag`
    - ARGS are git arguments passed directly to the git command