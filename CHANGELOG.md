# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.11.0] - XXXX-XX-XX


## [0.10.3] - 2021-08-05
### Added
- New `-c` shortcut to pass cluster name in commands

## [0.10.2] - 2021-08-04
### Added
- New `ecs task logs` command, to display task logs
- New `ecs task list` command, to display currently running tasks

### Fixed
- Use session for selecting region for AWS rather than env variable
- Display both "Created At" and "Started at" for task

## [0.10.1] - 2021-08-04
### Added
- New `ecs task show` command

### Changed
- Fixed display of service without running tasks

## [0.10.0] - 2021-07-30
Big migration from old structure to new one. Literally whole codebase changed.
