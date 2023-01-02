# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/eduNEXT/drydock/compare/v0.4.1...HEAD)

Please do not update the unreleased notes.

<!-- Content should be placed here -->
## [v0.4.1](https://github.com/eduNEXT/drydock/compare/v0.4.0...v0.4.1) - 2022-12-07

### [0.4.1](https://github.com/eduNEXT/drydock/compare/v0.4.0...v0.4.1) (2022-12-07)

#### Features

- Add configuration for container interactivity.

#### Code Refactoring

- Increase default debug replicas to at least one

## [v0.4.0](https://github.com/eduNEXT/drydock/compare/v0.3.4...v0.4.0) - 2022-12-01

### [0.4.0](https://github.com/eduNEXT/drydock/compare/v0.3.4...v0.4.0) (2022-12-01)

#### Features

- Add templates for debugging purposes.

#### Code Refactoring

- Check if forum is defined before adding resources.

#### Bug Fixes

- Use the right target for the forum hpa.
- Add missing patch in V14 templates.

## [v0.3.4](https://github.com/eduNEXT/drydock/compare/v0.3.3...v0.3.4) - 2022-11-09

### [0.3.4](https://github.com/eduNEXT/drydock/compare/v0.3.3...v0.3.4) (2022-11-09)

#### Features

- Add multipurpose jobs for tutor version 14.

## [v0.3.3](https://github.com/eduNEXT/drydock/compare/v0.3.2...v0.3.3) - 2022-11-09

### [0.3.3](https://github.com/eduNEXT/drydock/compare/v0.3.2...v0.3.3) (2022-11-09)

#### Features

- Add multipurpose jobs.

## [v0.3.2](https://github.com/eduNEXT/drydock/compare/v0.3.1...v0.3.2) - 2022-11-09

### [0.3.2](https://github.com/eduNEXT/drydock/compare/v0.3.1...v0.3.2) (2022-11-09)

#### Bug Fixes

- Add missing labels for notes jobs.

## [v0.3.1](https://github.com/eduNEXT/drydock/compare/v0.3.0...v0.3.1) - 2022-10-21

### [0.3.1](https://github.com/eduNEXT/drydock/compare/v0.3.0...v0.3.1) (2022-10-21)

#### Code Refactoring

- Refactor hpa with latest practices.

## [v0.3.0](https://github.com/eduNEXT/drydock/compare/v0.2.0...v0.3.0) - 2022-10-18

### [0.3.0](https://github.com/eduNEXT/drydock/compare/v0.2.0...v0.3.0) (2022-10-18)

#### Features

- Make manifests template root configurable through reference.
- Add templates with tutor14 support.

## [v0.2.0](https://github.com/eduNEXT/drydock/compare/v0.1.0...v0.2.0) - 2022-10-13

### [0.2.0](https://github.com/eduNEXT/drydock/compare/v0.1.0...v0.2.0) (2022-10-13)

#### Features

- Add 1st version of rendered jobs.
- Add toggleable certificates.
- Add extra-jobs for extra tasks during initialization.

#### Bug fixes

- Use production ingress instead of dummy.
- Use the correct init command for forum and add missing annotations.

#### Code Refactoring

- Move forum pod to wave 4, HPA to wave 5.
- Remove MySQL jobs when MySQL running outside the cluster.

## [v0.1.0](https://github.com/eduNEXT/drydock/commits/v0.1.0) - 2022-10-12

### [0.1.0](https://github.com/eduNEXT/drydock/commits/v0.1.0) (2022-10-12)

#### Features

- Add a basic manifest repository implementation.
- Add kustomize based extensions to the base manifests.
- Add newrelic manifests for tutor13 installation.
- Render global environment outside tutor-env.
- Add support for custom SSL certificates.

#### Bug fixes

- Set a default value for DRYDOCK_NEWRELIC_CONFIG variable.
