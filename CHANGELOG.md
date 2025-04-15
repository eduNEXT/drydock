# CHANGELOG


## v19.2.0 (2025-04-15)

### Features

- Add drop-db command ([#156](https://github.com/eduNEXT/drydock/pull/156),
  [`bf09725`](https://github.com/eduNEXT/drydock/commit/bf097259ec8811f1bb86251df215a7826997aa3c))


## v19.1.0 (2025-04-14)

### Features

- Create patch for registry credentials ([#154](https://github.com/eduNEXT/drydock/pull/154),
  [`e6d8948`](https://github.com/eduNEXT/drydock/commit/e6d89483df9365c4e710c2e489df27b4110b3bc5))

* feat: create patch for registry credentials

* feat: include json transform

* feat: change secret render

* fix: correct files

* docs: update readmd

* fix: include extra workloads

* fix: change patch for cronjob and remove kind

* docs: update readme.md

Co-authored-by: Moisés González <moises.gonzalez@edunext.co>

* fix: remove deamonset and statefulsets

---------


## v19.0.1 (2025-01-31)

### Bug Fixes

- Configure custom forum DBs credentials ([#153](https://github.com/eduNEXT/drydock/pull/153),
  [`68b06f5`](https://github.com/eduNEXT/drydock/commit/68b06f5030abfc5647ee06a40f603cb26acfec93))

The tutor-forum plugin hardcodes the value of the name of the forum database in the Django settings,
  dropping the previous `FORUM_MONGODB_DATABASE` setting
  (https://github.com/overhangio/tutor-forum/blob/5d3d2dd7d1ea3c9a311ac5619eb5931a111ba363/tutorforum/plugin.py#L29).

We reintroduce the `FORUM_MONGODB_DATABASE` setting and ensure the mongodb user has permissions over
  the Forum Database.

In order to be able to override the hardcoded value we lower the priority level of the Drydock
  patches, guaranteeing that they are going to be applied after all the installed plugins.


## v19.0.0 (2024-12-18)

### Features

- Sumac release
  ([`e42e001`](https://github.com/eduNEXT/drydock/commit/e42e0015b184ac20ef619de1b510e59010684fac))

Empty commit to trigger a major version bump

- Sumac release ([#146](https://github.com/eduNEXT/drydock/pull/146),
  [`95ef30f`](https://github.com/eduNEXT/drydock/commit/95ef30f7ddc16d29dbce23efcd98b4da1eebfb3f))


## v18.2.8 (2024-10-16)

### Bug Fixes

- Adding replicaset info to mongosh connection command. Adding mongodb port variable
  ([#145](https://github.com/eduNEXT/drydock/pull/145),
  [`8855736`](https://github.com/eduNEXT/drydock/commit/88557360081f053bfc8b3e1b2dade6be395bc8a9))

- Include the MongoDB port in the mongosh command (useful when running MongoDB in a different port)
  - Include the replica set info in the mongosh command. It could be the case you aren't connected
  to a replica set primary but to a secondary one. If the replica set name is not specified, the
  mongosh command will fail since it is not possible to write to a secondary


## v18.2.7 (2024-10-15)

### Bug Fixes

- **newrelic**: Use the new location of uwsgi.ini in the launch command
  ([#144](https://github.com/eduNEXT/drydock/pull/144),
  [`67fb1fc`](https://github.com/eduNEXT/drydock/commit/67fb1fc3073ff66ad318799e36ebc0ff88a55eab))

The location of the uwsgi.ini file was changed in tutor==18.1.3 so we have to update the command run
  by the container. Additionally we remove an unused variable that was lingering.


## v18.2.6 (2024-09-24)

### Bug Fixes

- **scorm**: Use request host for scorm custom domain
  ([#141](https://github.com/eduNEXT/drydock/pull/141),
  [`55a5153`](https://github.com/eduNEXT/drydock/commit/55a515326aed82c23f9feb2e9c129f8511502d24))


## v18.2.5 (2024-09-19)

### Bug Fixes

- Use correct host for the CMS probes ([#138](https://github.com/eduNEXT/drydock/pull/138),
  [`d011d71`](https://github.com/eduNEXT/drydock/commit/d011d71e630f565aa431c2834eff2f11f1af4b07))


## v18.2.4 (2024-09-11)

### Bug Fixes

- Add readiness probe for lms/cms ([#133](https://github.com/eduNEXT/drydock/pull/133),
  [`f970e01`](https://github.com/eduNEXT/drydock/commit/f970e0102f36c3064201ff7be317d1a908557a87))

* fix: add readiness probe for lms/cms

* fix: add affinity to spread lms/cms to multiple nodes

* chore: remove readiness probe

* fix: reduce startup probe period seconds

* fix: gracefully kill uwsgi workers

* fix: disable local file loggers

* fix: disable logging

* fix: reduce max unavailable to 0

* fix: add liveness probe for cms and lms

* fix: fail early on tracking logger removal

* chore: remove rolling update options

* fix: restore preStop hook

* fix: use right host for cms livenessProbe

* fix: use lms/cms host only

* chore: restore prestopHook


## v18.2.3 (2024-08-13)

### Bug Fixes

- Drop celery support ([#129](https://github.com/eduNEXT/drydock/pull/129),
  [`86f2639`](https://github.com/eduNEXT/drydock/commit/86f26393d3ef54428a0011f1b24ac6c41853ce09))


## v18.2.2 (2024-08-12)

### Bug Fixes

- Add uwsgi tweaks for closed connection ([#126](https://github.com/eduNEXT/drydock/pull/126),
  [`a8cbf65`](https://github.com/eduNEXT/drydock/commit/a8cbf65857fa2cdbd47e74b26f03323128d76a5e))

fix: add readiness probe for lms

chore: remove startup probe and increase timeout of readiness probe

chore: restore startup probe


## v18.2.1 (2024-08-06)

### Bug Fixes

- Drop sentry support ([#128](https://github.com/eduNEXT/drydock/pull/128),
  [`89392b5`](https://github.com/eduNEXT/drydock/commit/89392b5109e63164ae2a8bac8723f2061a0e8680))


## v18.2.0 (2024-07-15)

### Features

- Add aspects deployments to post init deployments
  ([#123](https://github.com/eduNEXT/drydock/pull/123),
  [`762c356`](https://github.com/eduNEXT/drydock/commit/762c3569dd8578ea5296712e245553ad00b534e4))


## v18.1.1 (2024-07-05)

### Bug Fixes

- S3_host for alternative S3-compatible services
  ([#120](https://github.com/eduNEXT/drydock/pull/120),
  [`08d2ef3`](https://github.com/eduNEXT/drydock/commit/08d2ef3ec9aa60ed3d9402dfb5480530147b90de))

* fix: when using SCORM, S3_HOST must be used for alternative S3-compatible services


## v18.1.0 (2024-07-02)

### Bug Fixes

- Remove unnecesary annotations from the hpa sync wave
  ([#117](https://github.com/eduNEXT/drydock/pull/117),
  [`18c99e3`](https://github.com/eduNEXT/drydock/commit/18c99e335751c4007a6d0d8f9488ba1361b57c6e))

The HPA sync-wave patch includes annotations to indicate argocd in which order should the HPA
  resources be applied in relation to the other resources. The `argocd.argoproj.io/hook: Sync` and
  `argocd.argoproj.io/hook-delete-policy: HookSucceeded` annotations are used for ephemeral
  resources (like jobs) and should not be used for the HPA resources.

### Features

- Add support for static cache config ([#106](https://github.com/eduNEXT/drydock/pull/106),
  [`01d05ec`](https://github.com/eduNEXT/drydock/commit/01d05ec8c80e4a8dc96a9f25adf39ca62c0507ef))

fix: address PR suggestions

build: correct port and path for mfe tests


## v18.0.0 (2024-07-02)

### Features

- Redwood upgrade
  ([`fd100ad`](https://github.com/eduNEXT/drydock/commit/fd100ad44fb475a56ebf9e9a6ce154372a38f8fb))

BREAKING CHANGE: version 18

### Breaking Changes

- Version 18


## v17.3.5 (2024-06-12)

### Bug Fixes

- Replace deprecated bucket argument for recommended bucket_name
  ([#107](https://github.com/eduNEXT/drydock/pull/107),
  [`f21d338`](https://github.com/eduNEXT/drydock/commit/f21d3384c76dba6d3042ada7725797f1ea97673b))

The S3Boto3Storage backend no longer accepts the argument bucket. Use bucket_name or the setting
  AWS_STORAGE_BUCKET_NAME instead: https://github.com/jschneier/django-storages/pull/636


## v17.3.4 (2024-05-27)

### Bug Fixes

- Solve error check k8s workflow main ([#102](https://github.com/eduNEXT/drydock/pull/102),
  [`e6a4e91`](https://github.com/eduNEXT/drydock/commit/e6a4e913524638025b90095edbe8904e4de11258))

* fix: solve error check k8s workflow

* fix: define specific kubeconform version and include action on push

* fix: extract and set kubernetes version from kubectl


## v17.3.3 (2024-05-22)


## v17.3.2 (2024-04-26)

### Bug Fixes

- Verify minio host is defined on scorm proxy ([#96](https://github.com/eduNEXT/drydock/pull/96),
  [`503ab92`](https://github.com/eduNEXT/drydock/commit/503ab928499937fee45718c544ff02e35e6c7a38))

* fix: verify minio host is defined on scorm proxy

* chore: refactor scorm template


## v17.3.1 (2024-04-26)

### Bug Fixes

- Enable scorm proxy if s3 plugin is installed ([#92](https://github.com/eduNEXT/drydock/pull/92),
  [`c1ee060`](https://github.com/eduNEXT/drydock/commit/c1ee060e1ca4975119aa8a651597664b428d8c18))

docs: add documentation for ingress lm extra hosts


## v17.3.0 (2024-04-18)

### Bug Fixes

- Run the jobs scripts with '-e' to exit on error
  ([#74](https://github.com/eduNEXT/drydock/pull/74),
  [`cb8bcb2`](https://github.com/eduNEXT/drydock/commit/cb8bcb24667eff45e853104248ff253c0dcc046b))

### Features

- Add auto generated jobs ([#87](https://github.com/eduNEXT/drydock/pull/87),
  [`8af2745`](https://github.com/eduNEXT/drydock/commit/8af27458901cdc2d57b3de4708fec0efd97cc875))


## v17.2.0 (2024-02-27)

### Features

- Iterate over added mfes to add its paths ([#72](https://github.com/eduNEXT/drydock/pull/72),
  [`d61991b`](https://github.com/eduNEXT/drydock/commit/d61991b133fdb154f5118583809bb813c868aeb5))


## v17.1.1 (2024-02-23)

### Bug Fixes

- Notes annotations throw job skip from argocd sync
  ([#69](https://github.com/eduNEXT/drydock/pull/69),
  [`d965aa7`](https://github.com/eduNEXT/drydock/commit/d965aa7ad459b19b4b99bc450132d3b87c761fcd))


## v17.1.0 (2024-01-30)

### Features

- Add poddisruptionbudget ([#66](https://github.com/eduNEXT/drydock/pull/66),
  [`9266f98`](https://github.com/eduNEXT/drydock/commit/9266f985dc4adc8da4366cb1420fa731f47cd4df))

* feat: add poddisruptionbudget patches

* test: update pdb

* test: include pdbs in patches

* test: using kustomization

* test: include in resources

* fix: include conditional for mfe and forum

* fix: correct endlines

* feat: pdb value parametrizable

* fix: delete undefined variable

* fix: drydock variable names

* fix: change comparison operator and pdb path


## v17.0.0 (2024-01-19)

### Features

- Add support to quince ([#61](https://github.com/eduNEXT/drydock/pull/61),
  [`aeefdca`](https://github.com/eduNEXT/drydock/commit/aeefdcaa18302eb1e9fc01191ed91d932db7044a))

BREAKING CHANGE: Support to tutor v17

### Breaking Changes

- Support to tutor v17


## v16.2.2 (2024-01-18)

### Bug Fixes

- Remove dash from endif ([#65](https://github.com/eduNEXT/drydock/pull/65),
  [`3794a2f`](https://github.com/eduNEXT/drydock/commit/3794a2fd278a77e276af2f2dafdec6870a3b7078))


## v16.2.1 (2024-01-18)

### Bug Fixes

- Add missing drydock custom certs secret ([#64](https://github.com/eduNEXT/drydock/pull/64),
  [`7812911`](https://github.com/eduNEXT/drydock/commit/7812911a09d227428157876e64ede9b1274ff1ec))

(cherry picked from commit ed8b57a0600913ea77de02bd995f6adc134f1446)


## v16.2.0 (2024-01-17)

### Features

- Add mysql init job patch and fix command on mongo init job
  ([#63](https://github.com/eduNEXT/drydock/pull/63),
  [`d838e22`](https://github.com/eduNEXT/drydock/commit/d838e2211421d9bdb48a16987f1a277146227240))


## v16.1.0 (2024-01-10)

### Features

- Add a job to initialize mongodb users ([#60](https://github.com/eduNEXT/drydock/pull/60),
  [`c19ae63`](https://github.com/eduNEXT/drydock/commit/c19ae634ec0c8c3183f63e13ee6d03dcd8309134))

Include an initialization job similar to the MySQL one that creates a mongodb user with the
  necessary permissions. To simplify things a bit we use the same user for edxapp and forum and
  remove the need for the forum-overrides patch.


## v16.0.1 (2024-01-09)

### Bug Fixes

- Add manifests file to allow install drydock non editable
  ([#59](https://github.com/eduNEXT/drydock/pull/59),
  [`b150a41`](https://github.com/eduNEXT/drydock/commit/b150a4136cf07e9865bcd5b740100fb9740531dc))


## v16.0.0 (2023-12-19)

### Features

- Add support to tutor palm ([#57](https://github.com/eduNEXT/drydock/pull/57),
  [`f43fb18`](https://github.com/eduNEXT/drydock/commit/f43fb1819d719087d13a2b58437b5b15b30222c8))

BREAKING CHANGE: Drops support to python 3.7

### Breaking Changes

- Drops support to python 3.7


## v15.5.1 (2023-12-18)

### Bug Fixes

- Issue at first run with lms and cms deployments
  ([#56](https://github.com/eduNEXT/drydock/pull/56),
  [`e1b5636`](https://github.com/eduNEXT/drydock/commit/e1b5636e249d9df5457ac5122def2ddd34a5f511))

- Remove pat from release workflow ([#55](https://github.com/eduNEXT/drydock/pull/55),
  [`acb59ad`](https://github.com/eduNEXT/drydock/commit/acb59ade11414a1b708f9293121ef19aafeb613c))


## v15.5.0 (2023-11-29)

### Features

- Support docker operations for image in drydock backups
  ([#53](https://github.com/eduNEXT/drydock/pull/53),
  [`07d0371`](https://github.com/eduNEXT/drydock/commit/07d03719acbb7b7fadf700eb174ebb0de20ae245))

* feat: support docker operations for image in drydock backups

* fix: update image variable in defaults and jobs template

* fix: update .gitignore

* fix: using BACKUP_VARIABLE

* fix: update readme

* fix: update gitignore for /build/ folder


## v15.4.0 (2023-11-23)

### Features

- Mongo DB backups proper implementation ([#52](https://github.com/eduNEXT/drydock/pull/52),
  [`16d27ea`](https://github.com/eduNEXT/drydock/commit/16d27eaca9063e70d32e4c85653465d673bd9ce1))

* fix: update variables names and jumplines

* fix: duplicate key

* fix: include custom_storage_endpoint in aws block

* fix: newlines control

* fix: args for command

* fix: environment azure variables

* fix: include bucket path in all options

* fix: delete databases variable

* fix: update .sh

* fix: update default shipyard-utils image


## v15.3.0 (2023-11-16)

### Features

- Use azcopy for databases backups ([#51](https://github.com/eduNEXT/drydock/pull/51),
  [`03881f2`](https://github.com/eduNEXT/drydock/commit/03881f2ca3c76f725a28ec71d6c233d4e8b734c3))

* feat: install azcopy

* feat: add new variables and conditionals for storage services

* fix: include custom storage endpoint inside s3 conditional

* feat: add variables and azcopy command

* fix: update variable names

* fix: storage system names

* fix: default s3 value

* fix: error in readme

* update backup system variable name

* fix: azure-blob conditional


## v15.2.0 (2023-11-07)

### Features

- Split ingress per host, add patch to add lms extra hosts
  ([#50](https://github.com/eduNEXT/drydock/pull/50),
  [`0401123`](https://github.com/eduNEXT/drydock/commit/0401123b2ebf95e766312c3465bb2a9956d477bf))


## v15.1.0 (2023-11-01)

### Bug Fixes

- Removing inexistent folder from github actions release flow
  ([`81f3a06`](https://github.com/eduNEXT/drydock/commit/81f3a0699f6043d7fccb140dd97db1c98ad08286))

- Using Github PAT to bypass main branch protection
  ([`ad40e6a`](https://github.com/eduNEXT/drydock/commit/ad40e6a256bed62551e8f7436f43ae7841264776))

### Features

- Replacing Kustomize JSON patches with strategic merge patches.
  ([`65a4b70`](https://github.com/eduNEXT/drydock/commit/65a4b70367fd3ffead87695445b1a1be0acd9c3c))


## v15.0.0 (2023-10-09)

### Features

- Add extra plugin ([#48](https://github.com/eduNEXT/drydock/pull/48),
  [`36c033f`](https://github.com/eduNEXT/drydock/commit/36c033faecf7c3ebc701a085cb33e55629910d88))

- Drydock 1.0 ([#47](https://github.com/eduNEXT/drydock/pull/47),
  [`5b09240`](https://github.com/eduNEXT/drydock/commit/5b0924017f474d364bb4b919e703b89955a713a2))


## v0.7.3 (2023-08-08)

### Bug Fixes

- Set the correct path to use pvc volume ([#45](https://github.com/eduNEXT/drydock/pull/45),
  [`6f9189c`](https://github.com/eduNEXT/drydock/commit/6f9189c64699f9bbedbcc03d2ee2152ed58bdb2e))


## v0.7.2 (2023-07-14)

### Bug Fixes

- Conditional error when tutor version is up to 15.0.0
  ([#44](https://github.com/eduNEXT/drydock/pull/44),
  [`8360e3f`](https://github.com/eduNEXT/drydock/commit/8360e3f3a042e85431975ff61d003433cb8b5f24))


## v0.7.1 (2023-07-10)

### Bug Fixes

- Drydock fails in older versions to tutor palm ([#43](https://github.com/eduNEXT/drydock/pull/43),
  [`c3c5e0a`](https://github.com/eduNEXT/drydock/commit/c3c5e0a30f3d5f672a170f567568c59e4d16f0d3))


## v0.7.0 (2023-07-07)

### Features

- Add support to palm version ([#42](https://github.com/eduNEXT/drydock/pull/42),
  [`f3c8448`](https://github.com/eduNEXT/drydock/commit/f3c84484b0c9165108e153ca2a2f4d1b61af3429))


## v0.6.1 (2023-05-12)

### Bug Fixes

- Mysqldump faild due mysql version ([#41](https://github.com/eduNEXT/drydock/pull/41),
  [`62d0839`](https://github.com/eduNEXT/drydock/commit/62d083959e1abd8b49f8dd44c4af58c44c3f1a9c))


## v0.6.0 (2023-04-05)

### Features

- Add backups plugin ([#39](https://github.com/eduNEXT/drydock/pull/39),
  [`33df210`](https://github.com/eduNEXT/drydock/commit/33df2109f854aa159c431dc96250f73ed123ae72))

Co-authored-by: Cristhian Garcia <cristhian.garcia@edunext.co>

Co-authored-by: Jhony Avella <jhony.avella@edunext.co>


## v0.5.1 (2023-03-20)

### Bug Fixes

- Rendering NewRelic overrides properly in tutor14 Drydock templates
  ([#38](https://github.com/eduNEXT/drydock/pull/38),
  [`423bac3`](https://github.com/eduNEXT/drydock/commit/423bac33216385d02566fbef90c8918e0cba8f50))


## v0.5.0 (2023-02-28)

### Bug Fixes

- Cms_sso_user, cms debug pods and whitespace triming
  ([#37](https://github.com/eduNEXT/drydock/pull/37),
  [`fb36c65`](https://github.com/eduNEXT/drydock/commit/fb36c657e998a5f7bb68f94ad3695089e601c24b))

* fix: standarize whitespace triming

* fix: define DJANGO_SETTINGS_MODULE for the cms debug pods

* fix: use the DRYDOCK_CMS_SSO_USER variable on the init jobs

### Features

- Add templates with tutor15 support. ([#35](https://github.com/eduNEXT/drydock/pull/35),
  [`1e85e46`](https://github.com/eduNEXT/drydock/commit/1e85e46e7f26ff1f153e972f12aea9e8b974ce6d))

- update forum job according to the k8s-jobs patch from tutor-forum. - use simplified hooks API
  introduced in tutor V15.3.0. - fix getting incompatible yaml files. - use DRYDOCK_CMS_SSO_USER
  variable instead of hard coded value.


## v0.4.1 (2022-12-07)

### Features

- Add configuration for container interactivity ([#29](https://github.com/eduNEXT/drydock/pull/29),
  [`fbc4489`](https://github.com/eduNEXT/drydock/commit/fbc4489f0aa48a1b07c9e900fa7d9c9506f680fb))


## v0.4.0 (2022-12-01)

### Bug Fixes

- Add missing patch in V14 templates ([#27](https://github.com/eduNEXT/drydock/pull/27),
  [`bda221b`](https://github.com/eduNEXT/drydock/commit/bda221bff1460a0cf47ce1280332f594ef4898c1))

- Use the right target for the forum hpa ([#26](https://github.com/eduNEXT/drydock/pull/26),
  [`49df7d4`](https://github.com/eduNEXT/drydock/commit/49df7d4127aa314bf0b906de688b47ed95a01542))

### Features

- Add templates for debugging purposes ([#25](https://github.com/eduNEXT/drydock/pull/25),
  [`2cc049d`](https://github.com/eduNEXT/drydock/commit/2cc049d485f5335f219e81bd2bf804ea722af549))

This PR adds k8s templates for debug pods, i.e pods running with non-production setup (root user,
  container entrypoint/command changed, ...), which allow developers to debug services like LMS/CMS
  in a production-like environment.


## v0.3.4 (2022-11-09)

### Features

- Adding patch to enable multipurpose jobs in an OpenedX installation V14
  ([#23](https://github.com/eduNEXT/drydock/pull/23),
  [`75e35a1`](https://github.com/eduNEXT/drydock/commit/75e35a158af5611a7f45d1b9a12e16e609ebe5c4))


## v0.3.3 (2022-11-09)

### Features

- Adding patch to enable multipurpose jobs in an OpenedX installation
  ([#22](https://github.com/eduNEXT/drydock/pull/22),
  [`44d336d`](https://github.com/eduNEXT/drydock/commit/44d336d12d89a32e37e6ac3867e651a2c957551c))


## v0.3.2 (2022-11-01)

### Bug Fixes

- Add missing labels for notes jobs ([#21](https://github.com/eduNEXT/drydock/pull/21),
  [`0428575`](https://github.com/eduNEXT/drydock/commit/04285754bbb76086801ef3f5b68d432cd7031b20))


## v0.3.1 (2022-10-21)

### Features

- Refactor hpa with latest practices ([#19](https://github.com/eduNEXT/drydock/pull/19),
  [`3009617`](https://github.com/eduNEXT/drydock/commit/3009617687d50847d59a4fcfd584d5c4b3509994))


## v0.3.0 (2022-10-18)

### Features

- Add templates with tutor14 support ([#18](https://github.com/eduNEXT/drydock/pull/18),
  [`cc392bb`](https://github.com/eduNEXT/drydock/commit/cc392bba4164859f0d907fb572bb72e08c18a3ae))

- Make manifests template root configurable through reference
  ([#17](https://github.com/eduNEXT/drydock/pull/17),
  [`0382752`](https://github.com/eduNEXT/drydock/commit/0382752725f980ebf84f8f2bccaaf61b768e4645))


## v0.2.0 (2022-10-13)

### Bug Fixes

- Go back to production ingress ([#11](https://github.com/eduNEXT/drydock/pull/11),
  [`3be0bd2`](https://github.com/eduNEXT/drydock/commit/3be0bd2ab4ebca961387df66b04714944df0f0f0))

- Use the correct init command for forum and add missing annotations
  ([#12](https://github.com/eduNEXT/drydock/pull/12),
  [`9306d54`](https://github.com/eduNEXT/drydock/commit/9306d54451199b35d043e7ba1b1a56990195a959))

### Features

- Add 1st version of rendered jobs ([#10](https://github.com/eduNEXT/drydock/pull/10),
  [`e0e4162`](https://github.com/eduNEXT/drydock/commit/e0e416213e2a4d3562f4a1e71fce042b2d8bdfbd))

This PR adds a list of jobs for the most used services. This list can be configured using a variable
  defined in the config.yml with optional services such as minio or forum; required services like
  LMS are not removable. We configured this behavior using waves from argoCD.

- Add extra-jobs for extra tasks during initialization
  ([#14](https://github.com/eduNEXT/drydock/pull/14),
  [`bdfa07b`](https://github.com/eduNEXT/drydock/commit/bdfa07ba086ed0e0f26618ca9b8458cf74602aef))

- Add toggleable certificates ([#13](https://github.com/eduNEXT/drydock/pull/13),
  [`c021df9`](https://github.com/eduNEXT/drydock/commit/c021df9d99821b373006ae94c3adb7495e0176f7))

- Removing MySQL jobs when MySQL running outside the cluster
  ([#15](https://github.com/eduNEXT/drydock/pull/15),
  [`fca2272`](https://github.com/eduNEXT/drydock/commit/fca2272530be8f42e5d7cade135f56bc924bebfa))

* feat: removing MySQL jobs when MySQL service is running outside the cluster

* feat: adding labels to drydock jobs to better identify those from MySQL we want to skip

- Starting Forum pod in wave 4 to prevent issues before running the Forum job.
  ([#16](https://github.com/eduNEXT/drydock/pull/16),
  [`33d8c4a`](https://github.com/eduNEXT/drydock/commit/33d8c4ad02f8b8d989df1f7966dba35fb8c6d9ee))

Starting HPA resources in wave 5 to make sure deployments already exist


## v0.1.0 (2022-08-16)

### Bug Fixes

- Setting a default value for DRYDOCK_NEWRELIC_CONFIG variable
  ([`a67dbf1`](https://github.com/eduNEXT/drydock/commit/a67dbf1a1b183d60dba3dd9797b654d9d92dad8c))

### Features

- Add a basic manifest repository implementation ([#1](https://github.com/eduNEXT/drydock/pull/1),
  [`1f8208b`](https://github.com/eduNEXT/drydock/commit/1f8208bfa9d6ca67247449b90aa4db4b52b10b9f))

The `BaseManfests` builder will render a standard Tutor environment based on the templates used in
  version 13.3.1 of Tutor and use it as a base of Kustomization application with additional
  resources as overlays.

The `TutorExtendedConfig` will return the Tutor configuration values of the current `TUTOR_ROOT` and
  will use the default values of the template set (defined in a file `defaults.yml`) as a fallback.

- Add kustomize based extensions to the base manifests
  ([#3](https://github.com/eduNEXT/drydock/pull/3),
  [`2b93163`](https://github.com/eduNEXT/drydock/commit/2b93163090197dedfce5576755052b04a25e852c))

- Add newrelic manifests for tutor13 installation ([#6](https://github.com/eduNEXT/drydock/pull/6),
  [`8990e08`](https://github.com/eduNEXT/drydock/commit/8990e080e14c24a64ea8954f5218f4a5f98b344d))

- Add support for custom certificates
  ([`809ae3e`](https://github.com/eduNEXT/drydock/commit/809ae3e751d31056f4b54f80d397f6cb4a592048))

- Adding a better explanation at the readme
  ([`95d1490`](https://github.com/eduNEXT/drydock/commit/95d1490e5c45fb331fa003857fabe940045a4295))

- Adding readme
  ([`86f1c66`](https://github.com/eduNEXT/drydock/commit/86f1c66e5bc1355cbddb07d48b5247ae3b926d09))

- Cleaning the manifest output a bit
  ([`aa19367`](https://github.com/eduNEXT/drydock/commit/aa193675435793deebf02af81b148fcf5932d465))

- Connecting with tutor
  ([`76dec19`](https://github.com/eduNEXT/drydock/commit/76dec193030c1af82465b3d0baaf93f28e819bbb))

- Laying the groundwork for the architecture
  ([`bd6129c`](https://github.com/eduNEXT/drydock/commit/bd6129c3683895d2681c4050b1a010bc6a819cd1))

- Making all the classes be defined by the reference file
  ([`138307a`](https://github.com/eduNEXT/drydock/commit/138307ab081c982bb7287bb4ebce9b778940d1b3))

- Making reference support options
  ([`7b69f2c`](https://github.com/eduNEXT/drydock/commit/7b69f2c8b756d22bbb9307fb55d7752dd722563b))

- Making tutor_v13 volume sizes configurable
  ([`6bbebca`](https://github.com/eduNEXT/drydock/commit/6bbebcaf72dbfe7d10a4f99aea84206bc8c4e41f))

- Moving the tutor renderer to the actual implementing class
  ([`e2a6119`](https://github.com/eduNEXT/drydock/commit/e2a611943e4ce72553bebb8847264ae23e7c4768))

- Render global environment for prometheus outside tutor-env
  ([#5](https://github.com/eduNEXT/drydock/pull/5),
  [`f114243`](https://github.com/eduNEXT/drydock/commit/f11424323f20751150fd21cfe15524f1532c3144))

- Stating the purpose and context for this project
  ([`2ba3280`](https://github.com/eduNEXT/drydock/commit/2ba328034eae987310f70431e49b8a0d625fce90))
