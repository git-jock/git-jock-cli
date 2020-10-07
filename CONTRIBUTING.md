# Contributing to Git Jock CLI

This is still to be documented to allow others to contribute, there is currently an issue for it.

Currently it only documents branches and releases.




<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## Branches

### `main`
The main development branch. This is the default branch that should be branched from, and the target of any PRs.

### `release`
Holds the code released, for the latest released Major version.

No manual commits go into `release`, they will all be through automated tasks for releasing.

### Others
The only other branches will be development branch. At a stage where there is a second major release, a second release
branch will be created so that bug fixes can be applied to both major versions.

## Releases

The tool follows MAJOR.MINOR.PATCH versioning, with alpha and beta releases also being used.

The release pipeline is still to be implemented and is open to change, so these are loose outlines rather than strict
guidelines at this stage.

### Major Releases `X.0.0`
* Major functionality change
* Breaking changes
* Lives in `release` with `major` tag

### Minor Releases `0.X.0`
* New features or functionality changes
* Backwards compatible
* Lives in `release` with `minor` tag

### Patch Releases `0.0.X`
* Bug fixes
* No features or functionality changes
* Backwards compatible
* Lives in `release` with `patch` tag

### Beta Releases `0.0.0bX`
* Releases on `develop` that haven't made it into `main` release
* Should be stable, but still pre-release
* Released to TestPyPI

### Alpha Releases `0.0.0aX`
* Releases on specific PRs with the `alpha` label or commits with `[alpha]` in the message
  * Note: `[alpha]` must be the most recent commit in a push for this
* May be used to test before release or PR
* Label/tag is only trusted from maintainers
* Alpha code **should not be trusted** as it may be external or buggy
* Released to TestPyPI