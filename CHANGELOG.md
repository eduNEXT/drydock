# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/eduNEXT/drydock/compare/v17.3.0...HEAD)

Please do not update the unreleased notes.

## [v15.0.0](https://github.com/eduNEXT/drydock/compare/v0.7.3...v15.0.0) - 2023-10-09

### [15.0.0](https://github.com/eduNEXT/drydock/compare/v0.7.3...v15.0.0) (2023-10-09)

#### Features

- drydock refactor to work without reference logic and enable tutor cli via skipping tutor jobs instead of delete them. ([#47](https://github.com/eduNEXT/drydock/pull/47)) ([5b09240](https://github.com/eduNEXT/drydock/commit/5b0924017f474d364bb4b919e703b89955a713a2))
- add plugins extra, extracted from namespace template ([#48](https://github.com/eduNEXT/drydock/pull/48)) ([36c033f](https://github.com/eduNEXT/drydock/commit/36c033faecf7c3ebc701a085cb33e55629910d88))

<!-- Content should be placed here -->
## [v17.3.0](https://github.com/eduNEXT/drydock/compare/v17.2.0...v17.3.0) - 2024-04-18

### [17.3.0](https://github.com/eduNEXT/drydock/compare/v17.2.0...v17.3.0) (2024-04-18)

#### Features

- add auto generated jobs ([#87](https://github.com/eduNEXT/drydock/issues/87)) ([8af2745](https://github.com/eduNEXT/drydock/commit/8af27458901cdc2d57b3de4708fec0efd97cc875))

#### Bug Fixes

- run the jobs scripts with '-e' to exit on error ([#74](https://github.com/eduNEXT/drydock/issues/74)) ([cb8bcb2](https://github.com/eduNEXT/drydock/commit/cb8bcb24667eff45e853104248ff253c0dcc046b))

## [v17.2.0](https://github.com/eduNEXT/drydock/compare/v17.1.1...v17.2.0) - 2024-02-27

### [17.2.0](https://github.com/eduNEXT/drydock/compare/v17.1.1...v17.2.0) (2024-02-27)

#### Features

- iterate over added mfes to add its paths ([#72](https://github.com/eduNEXT/drydock/issues/72)) ([d61991b](https://github.com/eduNEXT/drydock/commit/d61991b133fdb154f5118583809bb813c868aeb5))

## [v17.1.1](https://github.com/eduNEXT/drydock/compare/v17.1.0...v17.1.1) - 2024-02-23

### [17.1.1](https://github.com/eduNEXT/drydock/compare/v17.1.0...v17.1.1) (2024-02-23)

### Bug Fixes

- notes annotations throw job skip from argocd sync ([#69](https://github.com/eduNEXT/drydock/issues/69)) ([d965aa7](https://github.com/eduNEXT/drydock/commit/d965aa7ad459b19b4b99bc450132d3b87c761fcd))

## [v17.1.0](https://github.com/eduNEXT/drydock/compare/v17.0.0...v17.1.0) - 2024-01-30

### [17.1.0](https://github.com/eduNEXT/drydock/compare/v17.0.0...v17.1.0) (2024-01-30)

#### Features

- add poddisruptionbudget ([#66](https://github.com/eduNEXT/drydock/issues/66)) ([9266f98](https://github.com/eduNEXT/drydock/commit/9266f985dc4adc8da4366cb1420fa731f47cd4df))

## [v17.0.0](https://github.com/eduNEXT/drydock/compare/v16.2.2...v17.0.0) - 2024-01-19

### [17.0.0](https://github.com/eduNEXT/drydock/compare/v16.2.2...v17.0.0) (2024-01-19)

#### ⚠ BREAKING CHANGES

- Support to tutor v17

#### Features

- add support to quince ([#61](https://github.com/eduNEXT/drydock/issues/61)) ([aeefdca](https://github.com/eduNEXT/drydock/commit/aeefdcaa18302eb1e9fc01191ed91d932db7044a))

## [v16.2.2](https://github.com/eduNEXT/drydock/compare/v16.2.1...v16.2.2) - 2024-01-18

### [16.2.2](https://github.com/eduNEXT/drydock/compare/v16.2.1...v16.2.2) (2024-01-18)

### Bug Fixes

- remove dash from endif ([#65](https://github.com/eduNEXT/drydock/issues/65)) ([3794a2f](https://github.com/eduNEXT/drydock/commit/3794a2fd278a77e276af2f2dafdec6870a3b7078))

## [v16.2.1](https://github.com/eduNEXT/drydock/compare/v16.2.0...v16.2.1) - 2024-01-18

### [16.2.1](https://github.com/eduNEXT/drydock/compare/v16.2.0...v16.2.1) (2024-01-18)

### Bug Fixes

- add missing drydock custom certs secret ([#64](https://github.com/eduNEXT/drydock/issues/64)) ([7812911](https://github.com/eduNEXT/drydock/commit/7812911a09d227428157876e64ede9b1274ff1ec))

## [v16.2.0](https://github.com/eduNEXT/drydock/compare/v16.1.0...v16.2.0) - 2024-01-17

### [16.2.0](https://github.com/eduNEXT/drydock/compare/v16.1.0...v16.2.0) (2024-01-17)

#### Features

- add mysql init job patch and fix command on mongo init job ([#63](https://github.com/eduNEXT/drydock/issues/63)) ([d838e22](https://github.com/eduNEXT/drydock/commit/d838e2211421d9bdb48a16987f1a277146227240))

## [v16.1.0](https://github.com/eduNEXT/drydock/compare/v16.0.1...v16.1.0) - 2024-01-10

### [16.1.0](https://github.com/eduNEXT/drydock/compare/v16.0.1...v16.1.0) (2024-01-10)

#### Features

- add a job to initialize mongodb users ([#60](https://github.com/eduNEXT/drydock/issues/60)) ([c19ae63](https://github.com/eduNEXT/drydock/commit/c19ae634ec0c8c3183f63e13ee6d03dcd8309134))

## [v16.0.1](https://github.com/eduNEXT/drydock/compare/v16.0.0...v16.0.1) - 2024-01-09

### [16.0.1](https://github.com/eduNEXT/drydock/compare/v16.0.0...v16.0.1) (2024-01-09)

### Bug Fixes

- add manifests file to allow install drydock non editable ([#59](https://github.com/eduNEXT/drydock/issues/59)) ([b150a41](https://github.com/eduNEXT/drydock/commit/b150a4136cf07e9865bcd5b740100fb9740531dc))

## [v16.0.0](https://github.com/eduNEXT/drydock/compare/v15.5.1...v16.0.0) - 2023-12-19

### [16.0.0](https://github.com/eduNEXT/drydock/compare/v15.5.1...v16.0.0) (2023-12-19)

#### ⚠ BREAKING CHANGES

- Drops support to python 3.7

#### Features

- add support to tutor palm ([#57](https://github.com/eduNEXT/drydock/issues/57)) ([f43fb18](https://github.com/eduNEXT/drydock/commit/f43fb1819d719087d13a2b58437b5b15b30222c8))

## [v15.5.1](https://github.com/eduNEXT/drydock/compare/v15.5.0...v15.5.1) - 2023-12-18

### [15.5.1](https://github.com/eduNEXT/drydock/compare/v15.5.0...v15.5.1) (2023-12-18)

### Bug Fixes

- issue at first run with lms and cms deployments ([#56](https://github.com/eduNEXT/drydock/issues/56)) ([e1b5636](https://github.com/eduNEXT/drydock/commit/e1b5636e249d9df5457ac5122def2ddd34a5f511))
- remove pat from release workflow ([#55](https://github.com/eduNEXT/drydock/issues/55)) ([acb59ad](https://github.com/eduNEXT/drydock/commit/acb59ade11414a1b708f9293121ef19aafeb613c))

## [v15.5.0](https://github.com/eduNEXT/drydock/compare/v15.4.0...v15.5.0) - 2023-11-29

### [15.5.0](https://github.com/eduNEXT/drydock/compare/v15.4.0...v15.5.0) (2023-11-29)

#### Features

- support docker operations for image in drydock backups ([#53](https://github.com/eduNEXT/drydock/issues/53)) ([07d0371](https://github.com/eduNEXT/drydock/commit/07d03719acbb7b7fadf700eb174ebb0de20ae245))

## [v15.4.0](https://github.com/eduNEXT/drydock/compare/v15.3.0...v15.4.0) - 2023-11-23

### [15.4.0](https://github.com/eduNEXT/drydock/compare/v15.3.0...v15.4.0) (2023-11-23)

#### Features

- Mongo DB backups proper implementation ([#52](https://github.com/eduNEXT/drydock/issues/52)) ([16d27ea](https://github.com/eduNEXT/drydock/commit/16d27eaca9063e70d32e4c85653465d673bd9ce1))

## [v15.3.0](https://github.com/eduNEXT/drydock/compare/v15.2.0...v15.3.0) - 2023-11-16

### [15.3.0](https://github.com/eduNEXT/drydock/compare/v15.2.0...v15.3.0) (2023-11-16)

#### Features

- use azcopy for databases backups ([#51](https://github.com/eduNEXT/drydock/issues/51)) ([03881f2](https://github.com/eduNEXT/drydock/commit/03881f2ca3c76f725a28ec71d6c233d4e8b734c3))

## [v15.2.0](https://github.com/eduNEXT/drydock/compare/v15.1.0...v15.2.0) - 2023-11-07

### [15.2.0](https://github.com/eduNEXT/drydock/compare/v15.1.0...v15.2.0) (2023-11-07)

#### Features

- split ingress per host, add patch to add lms extra hosts ([#50](https://github.com/eduNEXT/drydock/issues/50)) ([0401123](https://github.com/eduNEXT/drydock/commit/0401123b2ebf95e766312c3465bb2a9956d477bf))

## [v15.1.0](https://github.com/eduNEXT/drydock/compare/v0.7.3...v15.1.0) - 2023-11-01

### [15.1.0](https://github.com/eduNEXT/drydock/compare/v15.0.0...v15.1.0) (2023-11-01)

#### Features

- replacing Kustomize JSON patches with strategic merge patches. ([65a4b70](https://github.com/eduNEXT/drydock/commit/65a4b70367fd3ffead87695445b1a1be0acd9c3c))

#### Bug Fixes

- removing inexistent folder from github actions release flow ([81f3a06](https://github.com/eduNEXT/drydock/commit/81f3a0699f6043d7fccb140dd97db1c98ad08286))
- using Github PAT to bypass main branch protection ([ad40e6a](https://github.com/eduNEXT/drydock/commit/ad40e6a256bed62551e8f7436f43ae7841264776))

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
