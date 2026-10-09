# How to contribute

External contributions are welcome and strongly encouraged. There are only a few
guidelines you need to follow.

## Commit and Pull Request Guidelines

We expect code submissions to go through code review. We use GitHub pull
requests for this purpose.

When submitting a change make sure to provide all the necessary context upfront
for maintainers to see. A well crafted commit message and PR description goes a
long way in speeding up the reviewing process.

Like other projects in the Open edX ecosystem, we use [Conventional Commits]. A
one-line commit message is sufficient for small or self-evident changes.
Extensive changes or those with deeper technical implications require longer
explanations in the commit body. If you are unsure how to start, read this guide
on [how to write good commit messages].

Document changes that have a direct effect on the user in the `CHANGELOG.md`
file. We use [`scriv`] to manage changelog entries and compile them into the
final `CHANGELOG.md` for each release. Run `make changelog-entry` to create a
fragment, edit it accordingly, and include it in your PR.

[Conventional Commits]: https://www.conventionalcommits.org/en/v1.0.0/
[how to write good commit messages]: https://cbea.ms/git-commit/
[`scriv`]: https://scriv.readthedocs.io/

## Development

We use [uv](https://github.com/astral-sh/uv) for project and dependency
management. You will need to install relatively recent version of the uv CLI to
make use of any the Makefile targets and common development workflow.

Run `uv sync` to set up the development environment. You can then run commands
prefixed with `uv run` for development, including running Tutor itself. We
recommend pointing the `TUTOR_ROOT` and `TUTOR_PLUGINS_ROOT` environment
variables to an isolated location for a clean environment.

Several Make targets are available for common actions. Run `make help` or `make`
without a target to list them.

## Releases

New releases are tagged on GitHub and published to PyPI via a manually triggered
GitHub Action.

Follow these steps to perform a release:

1. Create release commit bumping the package version and send a PR for review.
   We follow [Semantic Versioning], but major versions are only bumped between
   Open edX releases. Note: a release commit does not need to be standalone, it
   can be bundled with a feature change.
2. Run `make changelog-collect` to gather changelog entries (this must be done
   after bumping the version).
3. After reviewing and merging the release commit, manually trigger the CI
   workflow in GitHub Actions targeting the `main` branch.
4. Verify the workflow runs without errors and the package is properly published
   to PyPI.
