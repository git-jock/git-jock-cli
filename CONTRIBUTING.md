# Contributing to Git Jock CLI
Git Jock is open to contributions, through feature requests, issue reporting, pull requests and anything else you think
would improve the tool.

This document sets out the most common instructions on how to contribute, however if something isn't clear feel free to
reach out via an [issue](https://github.com/git-jock/git-jock-cli/issues).

## Issues & Feature Requests
Even if you don't have the time or knowledge to enhance the tool by contributing code, you can enable other to using
GitHub Issues. In order to do this in the most effective way please follow these steps.

You can see the [current issues here](https://github.com/git-jock/git-jock-cli/issues). 

1. First, ensure that you have an up to date version and that the issue or feature isn't already there.
1. Check to see if someone else has already reported the issue or requested the same (or a similar) feature.
1. If so, you can comment to express your interest in seeing it resolved as this can help with prioritisation.
1. If there is nothing, you can submit your own issue.

### Security Issues
Security issues are taken very seriously, and it may not be desirable to share these publicly until they have been 
patched to decrease the likelihood of exploits.

If you wish to report a security issue please email git-jock-security at gavinfenton dot com

### Issues
1. Tag your issue with:
   1. `bug` for any bugs, i.e. things not working or behaving unexpectedly.
   1. `question` for anything you find is unclear.
1. Describe what the issue is, with steps to replicate it, i.e. 
    1. what command you were running,
    1. your CLI version,
    1. system details,
    1. anything else that may be related.
1. Let us know if you are willing and able to develop it yourself.

### Feature Requests
1. Tag your issue with `enhancement`.
1. Give details on the feature you would like to see.
1. Explain why you want the feature, what issue does it solve?
1. Give some acceptance criteria for what you would expect to see when it is implemented.
1. Finally, let us know if you are willing and able to develop it yourself.

## Contributing Code

### Picking up Issues
All work should be tracked in an issue (see above), this helps ensure that anyone can see what is currently in 
development or in the pipeline. It also helps avoid duplication of effort in case two people happen to be looking at the
same area.

If you have something you want to implement, log an issue if there isn't one already. If there is one, comment on it to
let us know you want to pick it up. You are free to start working before doing this, but there is no guarantee your 
contribution will be accepted if it hasn't been 'vetted' through an issue first.

If the issue is unassigned and you show you are willing and able to pick it up, it will be assigned to you. Note that if
you haven't contributed before you will generally be assigned a maximum of one issue until you log a PR.

### Submitting Code
The coding standards currently consist of what is enforced in the workflows:
- `flake8` enforces pep8 and a McCabe complexity threshold of 10
- `pytest` ensures all tests are passing
    - New functionality should have new test cases, so simply passing isn't enough. This will be enforced by a 
    maintainer.
- ShiftLeft and SonarCloud will run SAST scans on the code when a PR is opened.

You should also include a [CHANGELOG](https://github.com/git-jock/git-jock-cli/blob/main/CHANGELOG.md) entry under the 
Unreleased section if there are any noticeable changes for a user, e.g. a new feature or a bugfix with a notable impact.

Though there aren't formal standards, you should match your code style to that already present in the repository, we may
give suggestions on how to do this at PR, or make minor edits to the code ourselves before accepting it.

If you wish to have an alpha version released of your PR (see below), you can ask a maintainer to do this.

You can run the build steps locally using [nektos/act](https://github.com/nektos/act).

## Branches

### `main`
The main development branch. This is the default branch enhancements should be branched from, and the targeted to.

### `release`
Holds the code released, for the latest released Major version.

Bug fix branches may be branched from here to avoid merge issues with prerelease code coming from `main`.

No manual commits go into `release`, they will all be through automated tasks for releasing.

### Others
The only other branches will be development branches. At a stage where there is a second major release, a second release
branch may be created so that bug fixes can be applied to both major versions.

## Releases

The tool follows [SemVer](https://semver.org/), i.e. MAJOR.MINOR.PATCH versioning, with alpha and beta releases also 
being used.

The release pipeline is still to be implemented and is open to change, so these are loose outlines rather than strict
guidelines at this stage.

### Major Releases `X.0.0`
* Major functionality change
* Breaking changes
* Lives in `release` with `major` tag

### Minor Releases `0.Y.0`
* New features or functionality changes
* Backwards compatible
* Lives in `release` with `minor` tag

### Patch Releases `0.0.Z`
* Bug fixes
* No features or functionality changes
* Backwards compatible
* Lives in `release` with `patch` tag

### Beta Releases `0.0.0bX`
* Releases on `develop` that haven't made it into `main` release
* Should be stable, having passed PR and tests, but still pre-release
* Released to TestPyPI

### Alpha Releases `0.0.0aX`
* Releases on specific PRs with the `alpha` label or commits with `[alpha]` in the message
  * Note: `[alpha]` must be in the most recent, single-line, commit message in a push event for this
* May be used to test before release or PR
  * Tests may also be skipped or failing
* Label/tag is only trusted from maintainers
* Alpha code **should not be trusted** as it may be external or buggy
* Released to TestPyPI