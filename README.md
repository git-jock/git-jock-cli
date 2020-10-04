# Git Jock Cli

Much like this image, the tool is under construction.

<p align="center">

<img src="docresrouces/jock.png" data-canonical-src="docresrouces/jock.png" height="400" alt="Jock" title="Jock"/>

:construction: :construction_worker_man: :building_construction: :construction_worker_woman: :construction:

</p>

## What is Jock CLI?

The CLI is intended to make dealing with multiple connected repositories easier, by grouping repositories and running 
git commands across them all.

## Roadmap

This is a loose roadmap to explain where the tool will end up, the versions & functionality against them are open to 
changes.

### 1.0

Basic git command functionality using list of repo addresses or directories.

e.g. `jock clone git@github.com:some-owner/repo-1.git ... git@github.com:some-other-owner/repo-42.git`
  - `clone` :sheep: :sheep:
  - `fetch` :softball: :dog2: :dash:
  - `pull` :no_good_woman: :flat_shoe: :service_dog:
  - `push` 	:arrow_left: :poodle:
  - `checkout` (inc. `-b` :herb:)
  
### 1.1

Stored repository settings and groups.

e.g. with a config of
```yaml
repositories:
  - name: auth-service
    address: git@github.com:some-startup/authentication-service.git
    directory: ../authentication-service
  - name: shared-entities
    address: git@github.com:some-startup/shared-entities.git
    directory: ../shared-entities
  - ...
  - name: user-service
    address: git@github.com:some-startup/user-service.git
    directory: ../users

groups:
  - name: services
    repositories:
      - auth-service
      - user-service
```
Commands could be grouped without stating individual repositories

`jock -g=services checkout -b update-shared-entities-version`

### 1.2 +

- Filtering on branch names
- Terminal sessions
- ???

Feel free to suggest feature requests in the [issues](https://github.com/GavinF17/git-jock/issues).

## Why is it called Git Jock?

That's Jock at the top, he's good at fetching, pulling etc. and I wish I could clone him. So it's a natural fit.