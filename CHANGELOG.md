# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/eduNEXT/drydock/compare/v0.7.3...HEAD)

Please do not update the unreleased notes.

## [v15.0.0](https://github.com/eduNEXT/drydock/compare/v0.7.3...v15.0.0) - 2023-10-09

### [15.0.0](https://github.com/eduNEXT/drydock/compare/v0.7.3...v15.0.0) (2023-10-09)

#### Features

- drydock refactor to work without reference logic and enable tutor cli via skipping tutor jobs instead of delete them. ([#47](https://github.com/eduNEXT/drydock/pull/47)) ([5b09240](https://github.com/eduNEXT/drydock/commit/5b0924017f474d364bb4b919e703b89955a713a2))
- add plugins extra, extracted from namespace template ([#48](https://github.com/eduNEXT/drydock/pull/48)) ([36c033f](https://github.com/eduNEXT/drydock/commit/36c033faecf7c3ebc701a085cb33e55629910d88))

<!-- Content should be placed here -->
## [v0.7.3](https://github.com/eduNEXT/drydock/compare/v0.7.2...v0.7.3) - 2023-08-08

### [0.7.3](https://github.com/eduNEXT/drydock/compare/v0.7.2...v0.7.3) (2023-08-08)

### Bug Fixes

- set the correct path to use pvc volume ([#45](https://github.com/eduNEXT/drydock/issues/45)) ([6f9189c](https://github.com/eduNEXT/drydock/commit/6f9189c64699f9bbedbcc03d2ee2152ed58bdb2e))

## [v0.7.2](https://github.com/eduNEXT/drydock/compare/v0.7.1...v0.7.2) - 2023-07-14

### [0.7.2](https://github.com/eduNEXT/drydock/compare/v0.7.1...v0.7.2) (2023-07-14)

### Bug Fixes

- conditional error when tutor version is up to 15.0.0 ([#44](https://github.com/eduNEXT/drydock/issues/44)) ([8360e3f](https://github.com/eduNEXT/drydock/commit/8360e3f3a042e85431975ff61d003433cb8b5f24))

## [v0.7.1](https://github.com/eduNEXT/drydock/compare/v0.7.0...v0.7.1) - 2023-07-10

### [0.7.1](https://github.com/eduNEXT/drydock/compare/v0.7.0...v0.7.1) (2023-07-10)

### Bug Fixes

- drydock fails in older versions to tutor palm ([#43](https://github.com/eduNEXT/drydock/issues/43)) ([c3c5e0a](https://github.com/eduNEXT/drydock/commit/c3c5e0a30f3d5f672a170f567568c59e4d16f0d3))

## [v0.7.0](https://github.com/eduNEXT/drydock/compare/v0.6.1...v0.7.0) - 2023-07-07

### [0.7.0](https://github.com/eduNEXT/drydock/compare/v0.6.1...v0.7.0) (2023-07-07)

#### Features

- add support to palm version ([#42](https://github.com/eduNEXT/drydock/issues/42)) ([f3c8448](https://github.com/eduNEXT/drydock/commit/f3c84484b0c9165108e153ca2a2f4d1b61af3429))

## [v0.6.1](https://github.com/eduNEXT/drydock/compare/v0.6.0...v0.6.1) - 2023-05-12

### [0.6.1](https://github.com/eduNEXT/drydock/compare/v0.6.0...v0.6.1) (2023-05-12)

### Bug Fixes

- mysqldump faild due mysql version ([#41](https://github.com/eduNEXT/drydock/issues/41)) ([62d0839](https://github.com/eduNEXT/drydock/commit/62d083959e1abd8b49f8dd44c4af58c44c3f1a9c))

## [v0.6.0](https://github.com/eduNEXT/drydock/compare/v0.5.1...v0.6.0) - 2023-04-05

### [0.6.0](https://github.com/eduNEXT/drydock/compare/v0.5.1...v0.6.0) (2023-04-05)

#### Features

- add backups plugin ([#39](https://github.com/eduNEXT/drydock/issues/39)) ([33df210](https://github.com/eduNEXT/drydock/commit/33df2109f854aa159c431dc96250f73ed123ae72))

## [v0.5.1](https://github.com/eduNEXT/drydock/compare/v0.5.0...v0.5.1) - 2023-03-20

### [0.5.1](https://github.com/eduNEXT/drydock/compare/v0.5.0...v0.5.1) (2023-03-20)

### Bug Fixes

- rendering NewRelic overrides properly in tutor14 Drydock templates ([#38](https://github.com/eduNEXT/drydock/issues/38)) ([423bac3](https://github.com/eduNEXT/drydock/commit/423bac33216385d02566fbef90c8918e0cba8f50))

## [v0.5.0](https://github.com/eduNEXT/drydock/compare/v0.4.1...v0.5.0) - 2023-02-28

### [0.5.0](https://github.com/eduNEXT/drydock/compare/v0.4.1...v0.5.0) (2023-02-28)

#### Features

- add templates with tutor15 support. ([#35](https://github.com/eduNEXT/drydock/issues/35)) ([1e85e46](https://github.com/eduNEXT/drydock/commit/1e85e46e7f26ff1f153e972f12aea9e8b974ce6d))

#### Bug Fixes

- CMS_SSO_USER, cms debug pods and whitespace triming ([#37](https://github.com/eduNEXT/drydock/issues/37)) ([fb36c65](https://github.com/eduNEXT/drydock/commit/fb36c657e998a5f7bb68f94ad3695089e601c24b))

#### Build Systems

- add release GitHub workflow ([#32](https://github.com/eduNEXT/drydock/issues/32)) ([1e9a559](https://github.com/eduNEXT/drydock/commit/1e9a5598562b3a45d3077adf5bf5a42354a749e1))

#### Code Refactoring

- rename CMS SSO user to avoid conflicts with existent data ([#24](https://github.com/eduNEXT/drydock/issues/24)) ([6842da5](https://github.com/eduNEXT/drydock/commit/6842da52c2878c23abe45075eb29a6bbc0533eed))

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
