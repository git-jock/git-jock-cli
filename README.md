# Git Jock Cli

Much like this image, the tool is under construction.

<p align="center">
<img src="docresrouces/jock.png" data-canonical-src="docresrouces/jock.png" height="400" alt="Jock" title="Jock"/>
</p>

<h1 align="center">:construction: :construction_worker_man: :building_construction: :construction_worker_woman: :construction:</h1>


<table>
  <tr>
    <td align="center" colspan="3">
      <strong>Build & Releases<strong>
      <a href="#"><img src="docresrouces/line.png" height="1"></a>
    </td>
  </tr>
  
  <tr>
    <td align="center">:rocket:</td>
    <td align="center">
      <a href="https://github.com/git-jock/git-jock-cli/releases/latest"><img src="https://img.shields.io/github/v/release/git-jock/git-jock-cli?label=GH%20Release&logo=github" alt="GitHub Release" height="20"></a>
      <a href="https://pypi.org/project/git-jock/"><img src="https://img.shields.io/pypi/v/git-jock?logo=python&label=PyPI" alt="PyPi" height="20"></a>
    </td>
    <td align="center">:rocket:</td>
  </tr>

  <tr>
    <td align="center">:test_tube:</td>
    <td align="center">
      <a href="https://github.com/git-jock/git-jock-cli/actions"><img src="https://github.com/git-jock/git-jock-cli/workflows/Validate%20Python/badge.svg" alt="Validate Python" height="20"></a>
      <a href='https://coveralls.io/github/git-jock/git-jock-cli'><img src='https://coveralls.io/repos/github/git-jock/git-jock-cli/badge.svg' alt='Coverage Status' /></a>
      <a href="https://bestpractices.coreinfrastructure.org/projects/4345"><img src="https://bestpractices.coreinfrastructure.org/projects/4345/badge"></a>
    </td>
    <td align="center">:test_tube:</td>
  </tr>

  <tr>
    <td align="center">:closed_lock_with_key:</td>
    <td align="center">
      <a href="https://github.com/git-jock/git-jock-cli/actions"><img src="https://github.com/git-jock/git-jock-cli/workflows/ShiftLeft/badge.svg" alt="ShiftLeft" height="20"></a>
      <a href="https://sonarcloud.io/dashboard?id=git-jock_git-jock-cli"><img src="https://sonarcloud.io/api/project_badges/measure?project=git-jock_git-jock-cli&metric=alert_status" alt="Quality Gate Status" height="20"></a>
    </td>
    <td align="center">:closed_lock_with_key:</td>
  </tr>
</table>

## What is Jock CLI?

The CLI is intended to make dealing with multiple connected repositories easier, by grouping repositories and running 
git commands across them all.

## Install

To install or update on Linux or MacOS, you can download from 
[releases](https://github.com/git-jock/git-jock-cli/releases/latest) or run:
```bash
curl -s -L https://raw.githubusercontent.com/git-jock/git-jock-cli/main/scripts/install.sh | bash
```
:warning: _Note this script uses sudo to move the binary to `/usr/local/bin` and you should check the script before 
execution._

## Usage

### Configuration

Repositories and groups must be configured in `~/.jockrc`, in YAML format like below

```yaml
repositories:
  auth-service:
    address: git@github.com:some-startup/authentication-service.git
    location: /home/jock/git/authentication-service
  shared-entities:
    address: git@github.com:some-startup/shared-entities.git
    location: ~/shared-entities
  ...
  user-service:
    address: git@github.com:some-startup/user-service.git
    location: ../users

groups:
  - name: services
    repositories:
      - auth-service
      - user-service
```

- `address` is the remote git address
- `location` is the local location, can be relative to home or absolute

### CLI Usage

```
Usage: jock [OPTIONS] COMMAND [ARGS]...

Options:
  --version              Show the version and exit.
  -r, --repository TEXT  Repository, specified in ~/.jockrc, you wish to run
                         commands on. Multiple repositories can be specified
                         using multiple flags.

  -g, --group TEXT       Group of repositories, specified in ~/.jockrc, you
                         wish to run commands on.Multiple  groups can be
                         specified using multiple flags.

  --help                 Show this message and exit.

Commands:
  add branch checkout clone commit fetch pull push reset restore rm switch
```
- OPTIONS can be `--version`, `--help` or a list of repositories such as `-r git-jock-cli` or `--repository 
some-service`
- COMMAND is any of the currently supported git commands: `add`, `branch`, `checkout`, `clone`, `commit`, `fetch`, 
`pull`, `push`, `reset`, `restore`, `rm`, `switch`, or `tag`
- ARGS are git arguments passed directly to the git command


## Roadmap

This is a loose roadmap to explain where the tool will end up, the versions & functionality against them are open to 
changes.

### 0.3 +

- Filtering on branch names
- Terminal sessions
- ???

Feel free to suggest feature requests in the [issues](https://github.com/git-jock/git-jock-cli/issues).

## Why is it called Git Jock?

That's Jock at the top, he's good at fetching, pulling etc. and I wish I could clone him. So it's a natural fit.
