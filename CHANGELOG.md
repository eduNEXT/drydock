# CHANGELOG

## v18.2.3 (2024-08-13)

### Fix

* fix: drop celery support (#129) ([`86f2639`](https://github.com/eduNEXT/drydock/commit/86f26393d3ef54428a0011f1b24ac6c41853ce09))

## v18.2.2 (2024-08-12)

### Chore

* chore(release): preparing 18.2.2 ([`6235a74`](https://github.com/eduNEXT/drydock/commit/6235a74da31640e2f32a777f9a8086e429ed5d73))

### Fix

* fix: add uwsgi tweaks for closed connection (#126)

fix: add readiness probe for lms

chore: remove startup probe and increase timeout of readiness probe

chore: restore startup probe ([`a8cbf65`](https://github.com/eduNEXT/drydock/commit/a8cbf65857fa2cdbd47e74b26f03323128d76a5e))

## v18.2.1 (2024-08-06)

### Chore

* chore(release): preparing 18.2.1 ([`773a814`](https://github.com/eduNEXT/drydock/commit/773a81434b300f700d6f8ae8ccaccc099861c1cd))

### Fix

* fix: drop sentry support (#128) ([`89392b5`](https://github.com/eduNEXT/drydock/commit/89392b5109e63164ae2a8bac8723f2061a0e8680))

## v18.2.0 (2024-07-15)

### Chore

* chore(release): preparing 18.2.0 ([`3a734e2`](https://github.com/eduNEXT/drydock/commit/3a734e2207887aaf48ff0655092ae21b10fe2dfe))

### Feature

* feat: add aspects deployments to post init deployments (#123) ([`762c356`](https://github.com/eduNEXT/drydock/commit/762c3569dd8578ea5296712e245553ad00b534e4))

## v18.1.1 (2024-07-05)

### Chore

* chore(release): preparing 18.1.1 ([`6af587e`](https://github.com/eduNEXT/drydock/commit/6af587e45103e19f00026a7922840a32e680e173))

### Fix

* fix: S3_HOST for alternative S3-compatible services (#120)

* fix: when using SCORM, S3_HOST must be used for alternative S3-compatible services ([`08d2ef3`](https://github.com/eduNEXT/drydock/commit/08d2ef3ec9aa60ed3d9402dfb5480530147b90de))

## v18.1.0 (2024-07-02)

### Chore

* chore(release): preparing 18.1.0 ([`f87b84d`](https://github.com/eduNEXT/drydock/commit/f87b84d4884793e42bf33591d8f3ce7e4c09f4cc))

### Feature

* feat: add support for static cache config (#106)

fix: address PR suggestions

fix: address PR suggestions

fix: address PR suggestions

fix: address PR suggestions

build: correct port and path for mfe tests ([`01d05ec`](https://github.com/eduNEXT/drydock/commit/01d05ec8c80e4a8dc96a9f25adf39ca62c0507ef))

### Fix

* fix: remove unnecesary annotations from the hpa sync wave (#117)

The HPA sync-wave patch includes annotations to indicate argocd
in which order should the HPA resources be applied in relation
to the other resources. The `argocd.argoproj.io/hook: Sync`
and `argocd.argoproj.io/hook-delete-policy: HookSucceeded`
annotations are used for ephemeral resources (like jobs) and
should not be used for the HPA resources. ([`18c99e3`](https://github.com/eduNEXT/drydock/commit/18c99e335751c4007a6d0d8f9488ba1361b57c6e))

## v18.0.0 (2024-07-02)

### Breaking

* feat: redwood upgrade

BREAKING CHANGE: version 18 ([`fd100ad`](https://github.com/eduNEXT/drydock/commit/fd100ad44fb475a56ebf9e9a6ce154372a38f8fb))

### Chore

* chore(release): preparing 18.0.0 ([`30a4cc0`](https://github.com/eduNEXT/drydock/commit/30a4cc00848bb745a91fb70f1d5a9da09d76aa8a))

### Ci

* ci: ignore commits in changelog and release notes (#113) ([`693c91b`](https://github.com/eduNEXT/drydock/commit/693c91bed3772e3fa59d45eff85c8a0b8593677d))

## v17.3.5 (2024-06-12)

### Chore

* chore(release): preparing 17.3.5 ([`6ed209b`](https://github.com/eduNEXT/drydock/commit/6ed209b00822a7ccef48082b146c96c8e217e022))

### Ci

* ci: change release workflow (#108) ([`2ecac04`](https://github.com/eduNEXT/drydock/commit/2ecac04c21ba58fcbbf5a4f5b32c57087fcb36fd))

### Fix

* fix: replace deprecated bucket argument for recommended bucket_name (#107)

The S3Boto3Storage backend no longer accepts the argument bucket. Use
bucket_name or the setting AWS_STORAGE_BUCKET_NAME instead:
https://github.com/jschneier/django-storages/pull/636 ([`f21d338`](https://github.com/eduNEXT/drydock/commit/f21d3384c76dba6d3042ada7725797f1ea97673b))

## v17.3.4 (2024-05-27)

### Chore

* chore(release): preparing 17.3.4 ([`7bd3266`](https://github.com/eduNEXT/drydock/commit/7bd3266b00c9be65e007dd5746d98ac4960dfd04))

### Fix

* fix: solve error check k8s workflow main (#102)

* fix: solve error check k8s workflow

* fix: define specific kubeconform version and include action on push

* fix: extract and set kubernetes version from kubectl ([`e6a4e91`](https://github.com/eduNEXT/drydock/commit/e6a4e913524638025b90095edbe8904e4de11258))

## v17.3.3 (2024-05-22)

### Chore

* chore(release): preparing 17.3.3 ([`c01f238`](https://github.com/eduNEXT/drydock/commit/c01f238bbff75d9aa4c73319a7bdf7a441817d65))

## v17.3.2 (2024-04-26)

### Chore

* chore(release): preparing 17.3.2 ([`dfbbef4`](https://github.com/eduNEXT/drydock/commit/dfbbef464113874ab8dc4a072b3b22c2c96be5c9))

### Fix

* fix: verify minio host is defined on scorm proxy (#96)

* fix: verify minio host is defined on scorm proxy

* chore: refactor scorm template ([`503ab92`](https://github.com/eduNEXT/drydock/commit/503ab928499937fee45718c544ff02e35e6c7a38))

## v17.3.1 (2024-04-26)

### Chore

* chore(release): preparing 17.3.1 ([`eb47084`](https://github.com/eduNEXT/drydock/commit/eb47084434d2905544ea44f5938138f4ca31da86))

### Fix

* fix: enable scorm proxy if s3 plugin is installed (#92)

docs: add documentation for ingress lm extra hosts ([`c1ee060`](https://github.com/eduNEXT/drydock/commit/c1ee060e1ca4975119aa8a651597664b428d8c18))

## v17.3.0 (2024-04-18)

### Chore

* chore(release): preparing 17.3.0 ([`8e1f74e`](https://github.com/eduNEXT/drydock/commit/8e1f74ef2ff3de53de5212bc0c7bc057d995e0bd))

### Feature

* feat: add auto generated jobs (#87) ([`8af2745`](https://github.com/eduNEXT/drydock/commit/8af27458901cdc2d57b3de4708fec0efd97cc875))

### Fix

* fix: run the jobs scripts with &#39;-e&#39; to exit on error (#74) ([`cb8bcb2`](https://github.com/eduNEXT/drydock/commit/cb8bcb24667eff45e853104248ff253c0dcc046b))

## v17.2.0 (2024-02-27)

### Chore

* chore(release): preparing 17.2.0 ([`0d3cee4`](https://github.com/eduNEXT/drydock/commit/0d3cee4baa3334a3f4314e7d5c5d6ee56804dcfc))

### Feature

* feat: iterate over added mfes to add its paths (#72) ([`d61991b`](https://github.com/eduNEXT/drydock/commit/d61991b133fdb154f5118583809bb813c868aeb5))

## v17.1.1 (2024-02-23)

### Chore

* chore(release): preparing 17.1.1 ([`f4c58ae`](https://github.com/eduNEXT/drydock/commit/f4c58ae59825bb8af109183d9d3751546057451b))

### Fix

* fix: notes annotations throw job skip from argocd sync (#69) ([`d965aa7`](https://github.com/eduNEXT/drydock/commit/d965aa7ad459b19b4b99bc450132d3b87c761fcd))

## v17.1.0 (2024-01-30)

### Chore

* chore(release): preparing 17.1.0 ([`03fa727`](https://github.com/eduNEXT/drydock/commit/03fa72792ac602fdce1154629c0665252e0bc932))

### Feature

* feat: add poddisruptionbudget (#66)

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

* fix: change comparison operator and pdb path ([`9266f98`](https://github.com/eduNEXT/drydock/commit/9266f985dc4adc8da4366cb1420fa731f47cd4df))

## v17.0.0 (2024-01-19)

### Breaking

* feat: add support to quince (#61)

BREAKING CHANGE: Support to tutor v17 ([`aeefdca`](https://github.com/eduNEXT/drydock/commit/aeefdcaa18302eb1e9fc01191ed91d932db7044a))

### Chore

* chore(release): preparing 17.0.0 ([`5e41bf9`](https://github.com/eduNEXT/drydock/commit/5e41bf9441b922f0db30a8b728e5c17d95a07ef3))

## v16.2.2 (2024-01-18)

### Chore

* chore(release): preparing 16.2.2 ([`cab4205`](https://github.com/eduNEXT/drydock/commit/cab42057f9ef53ceba205fe28c3097e959125c59))

### Fix

* fix: remove dash from endif (#65) ([`3794a2f`](https://github.com/eduNEXT/drydock/commit/3794a2fd278a77e276af2f2dafdec6870a3b7078))

## v16.2.1 (2024-01-18)

### Chore

* chore(release): preparing 16.2.1 ([`b3032de`](https://github.com/eduNEXT/drydock/commit/b3032deee65b229327c7da90548a084b5836fbb6))

### Fix

* fix: add missing drydock custom certs secret (#64)

(cherry picked from commit ed8b57a0600913ea77de02bd995f6adc134f1446) ([`7812911`](https://github.com/eduNEXT/drydock/commit/7812911a09d227428157876e64ede9b1274ff1ec))

## v16.2.0 (2024-01-17)

### Chore

* chore(release): preparing 16.2.0 ([`d18281f`](https://github.com/eduNEXT/drydock/commit/d18281f5d872c96b1509d004dce973770b94d555))

### Feature

* feat: add mysql init job patch and fix command on mongo init job (#63) ([`d838e22`](https://github.com/eduNEXT/drydock/commit/d838e2211421d9bdb48a16987f1a277146227240))

## v16.1.0 (2024-01-10)

### Chore

* chore(release): preparing 16.1.0 ([`4ef0da5`](https://github.com/eduNEXT/drydock/commit/4ef0da5a1b3197ab92427eba4c6db51a7a7bcc37))

### Feature

* feat: add a job to initialize mongodb users (#60)

Include an initialization job similar to the MySQL one that creates a
mongodb user with the necessary permissions. To simplify things a bit we
use the same user for edxapp and forum and remove the need for the
forum-overrides patch. ([`c19ae63`](https://github.com/eduNEXT/drydock/commit/c19ae634ec0c8c3183f63e13ee6d03dcd8309134))

## v16.0.1 (2024-01-09)

### Chore

* chore(release): preparing 16.0.1 ([`840e2a7`](https://github.com/eduNEXT/drydock/commit/840e2a769687717aed6c547d24befa5bffed222f))

### Fix

* fix: add manifests file to allow install drydock non editable (#59) ([`b150a41`](https://github.com/eduNEXT/drydock/commit/b150a4136cf07e9865bcd5b740100fb9740531dc))

## v16.0.0 (2023-12-19)

### Breaking

* feat: add support to tutor palm (#57)

BREAKING CHANGE: Drops support to python 3.7 ([`f43fb18`](https://github.com/eduNEXT/drydock/commit/f43fb1819d719087d13a2b58437b5b15b30222c8))

### Chore

* chore(release): preparing 16.0.0 ([`af7e3a6`](https://github.com/eduNEXT/drydock/commit/af7e3a6619fb80144ffd59235f1939267d306e73))

## v15.5.1 (2023-12-18)

### Chore

* chore(release): preparing 15.5.1 ([`98c3bc9`](https://github.com/eduNEXT/drydock/commit/98c3bc9f149a9fb8ed4867af60dfaf636923675d))

### Fix

* fix: issue at first run with lms and cms deployments (#56) ([`e1b5636`](https://github.com/eduNEXT/drydock/commit/e1b5636e249d9df5457ac5122def2ddd34a5f511))

* fix: remove pat from release workflow (#55) ([`acb59ad`](https://github.com/eduNEXT/drydock/commit/acb59ade11414a1b708f9293121ef19aafeb613c))

### Unknown

* doc: update instructions for build docker image (#54) ([`705a748`](https://github.com/eduNEXT/drydock/commit/705a748e05a8179cc82243575a3393a12d03cb44))

## v15.5.0 (2023-11-29)

### Chore

* chore(release): preparing 15.5.0 ([`5f6b52c`](https://github.com/eduNEXT/drydock/commit/5f6b52cb7612e21729057a7a6b35fdf87f6b9256))

### Feature

* feat: support docker operations for image in drydock backups (#53)

* feat: support docker operations for image in drydock backups

* fix: update image variable in defaults and jobs template

* fix: update .gitignore

* fix: using BACKUP_VARIABLE

* fix: update readme

* fix: update gitignore for /build/ folder ([`07d0371`](https://github.com/eduNEXT/drydock/commit/07d03719acbb7b7fadf700eb174ebb0de20ae245))

## v15.4.0 (2023-11-23)

### Chore

* chore(release): preparing 15.4.0 ([`98f2cb3`](https://github.com/eduNEXT/drydock/commit/98f2cb318df6deb8b400be1234f64836521393b4))

### Feature

* feat: Mongo DB backups proper implementation (#52)

* fix: update variables names and jumplines

* fix: duplicate key

* fix: include custom_storage_endpoint in aws block

* fix: newlines control

* fix: args for command

* fix: environment azure variables

* fix: include bucket path in all options

* fix: delete databases variable

* fix: update .sh

* fix: update default shipyard-utils image ([`16d27ea`](https://github.com/eduNEXT/drydock/commit/16d27eaca9063e70d32e4c85653465d673bd9ce1))

## v15.3.0 (2023-11-16)

### Chore

* chore(release): preparing 15.3.0 ([`5320b7f`](https://github.com/eduNEXT/drydock/commit/5320b7f66fce98bbbdfa9e2aac8c9980a0ba7e51))

### Feature

* feat: use azcopy for databases backups (#51)

* feat: install azcopy

* feat: add new variables and conditionals for storage services

* fix: include custom storage endpoint inside s3 conditional

* feat: add variables and azcopy command

* fix: update variable names

* fix: storage system names

* fix: default s3 value

* fix: default s3 value

* fix: error in readme

* update backup system variable name

* fix: azure-blob conditional ([`03881f2`](https://github.com/eduNEXT/drydock/commit/03881f2ca3c76f725a28ec71d6c233d4e8b734c3))

## v15.2.0 (2023-11-07)

### Chore

* chore(release): preparing 15.2.0 ([`816cfb0`](https://github.com/eduNEXT/drydock/commit/816cfb089eda520cedc2c2b20a9109bad2dd3666))

### Feature

* feat: split ingress per host, add patch to add lms extra hosts (#50) ([`0401123`](https://github.com/eduNEXT/drydock/commit/0401123b2ebf95e766312c3465bb2a9956d477bf))

## v15.1.0 (2023-11-01)

### Chore

* chore(release): preparing 15.1.0 ([`2ee44b0`](https://github.com/eduNEXT/drydock/commit/2ee44b0b2656179b5e78030f6b822780dd768304))

### Feature

* feat: replacing Kustomize JSON patches with strategic merge patches.
These patches prevent resource fields replacement ([`65a4b70`](https://github.com/eduNEXT/drydock/commit/65a4b70367fd3ffead87695445b1a1be0acd9c3c))

### Fix

* fix: using Github PAT to bypass main branch protection ([`ad40e6a`](https://github.com/eduNEXT/drydock/commit/ad40e6a256bed62551e8f7436f43ae7841264776))

* fix: removing inexistent folder from github actions release flow ([`81f3a06`](https://github.com/eduNEXT/drydock/commit/81f3a0699f6043d7fccb140dd97db1c98ad08286))

## v15.0.0 (2023-10-09)

### Feature

* feat: add extra plugin (#48) ([`36c033f`](https://github.com/eduNEXT/drydock/commit/36c033faecf7c3ebc701a085cb33e55629910d88))

* feat: drydock 1.0 (#47) ([`5b09240`](https://github.com/eduNEXT/drydock/commit/5b0924017f474d364bb4b919e703b89955a713a2))

## v0.7.3 (2023-08-08)

### Chore

* chore(release): preparing 0.7.3 ([`4f59f73`](https://github.com/eduNEXT/drydock/commit/4f59f736f15944c05dad7776f1015a220a65f391))

### Fix

* fix: set the correct path to use pvc volume (#45) ([`6f9189c`](https://github.com/eduNEXT/drydock/commit/6f9189c64699f9bbedbcc03d2ee2152ed58bdb2e))

## v0.7.2 (2023-07-14)

### Chore

* chore(release): preparing 0.7.2 ([`8b8284f`](https://github.com/eduNEXT/drydock/commit/8b8284f17b1d80ce6619f5eabd81e3816b405e6d))

### Fix

* fix: conditional error when tutor version is up to 15.0.0 (#44) ([`8360e3f`](https://github.com/eduNEXT/drydock/commit/8360e3f3a042e85431975ff61d003433cb8b5f24))

## v0.7.1 (2023-07-10)

### Chore

* chore(release): preparing 0.7.1 ([`9a771ed`](https://github.com/eduNEXT/drydock/commit/9a771ed087321f2bf34cadc143dad596d74be686))

### Fix

* fix: drydock fails in older versions to tutor palm (#43) ([`c3c5e0a`](https://github.com/eduNEXT/drydock/commit/c3c5e0a30f3d5f672a170f567568c59e4d16f0d3))

## v0.7.0 (2023-07-07)

### Chore

* chore(release): preparing 0.7.0 ([`7750b51`](https://github.com/eduNEXT/drydock/commit/7750b5115c6bf2e111a47397e4a21fefd2558272))

### Feature

* feat: add support to palm version (#42) ([`f3c8448`](https://github.com/eduNEXT/drydock/commit/f3c84484b0c9165108e153ca2a2f4d1b61af3429))

## v0.6.1 (2023-05-12)

### Chore

* chore(release): preparing 0.6.1 ([`e850ab4`](https://github.com/eduNEXT/drydock/commit/e850ab4bffc9c8eebd9a649799501dfdb75d9cc9))

### Fix

* fix: mysqldump faild due mysql version (#41) ([`62d0839`](https://github.com/eduNEXT/drydock/commit/62d083959e1abd8b49f8dd44c4af58c44c3f1a9c))

## v0.6.0 (2023-04-05)

### Chore

* chore(release): preparing 0.6.0 ([`6575f39`](https://github.com/eduNEXT/drydock/commit/6575f39c7c948879cba3db443680a766b3433171))

### Feature

* feat: add backups plugin (#39)

Co-authored-by: Cristhian Garcia &lt;cristhian.garcia@edunext.co&gt;
Co-authored-by: Jhony Avella &lt;jhony.avella@edunext.co&gt; ([`33df210`](https://github.com/eduNEXT/drydock/commit/33df2109f854aa159c431dc96250f73ed123ae72))

## v0.5.1 (2023-03-20)

### Chore

* chore(release): preparing 0.5.1 ([`4fc77ae`](https://github.com/eduNEXT/drydock/commit/4fc77aef05899322c905bbcfb31afb9f67604f36))

### Fix

* fix: rendering NewRelic overrides properly in tutor14 Drydock templates (#38) ([`423bac3`](https://github.com/eduNEXT/drydock/commit/423bac33216385d02566fbef90c8918e0cba8f50))

## v0.5.0 (2023-02-28)

### Chore

* chore(release): preparing 0.5.0 ([`a5abacd`](https://github.com/eduNEXT/drydock/commit/a5abacdf60aca67527af1cd46b338137d9308285))

### Feature

* feat: add templates with tutor15 support. (#35)

- update forum job according to the k8s-jobs patch from tutor-forum.
- use simplified hooks API introduced in tutor V15.3.0.
- fix getting incompatible yaml files.
- use DRYDOCK_CMS_SSO_USER variable instead of hard coded value. ([`1e85e46`](https://github.com/eduNEXT/drydock/commit/1e85e46e7f26ff1f153e972f12aea9e8b974ce6d))

### Fix

* fix: CMS_SSO_USER, cms debug pods and whitespace triming (#37)

* fix: standarize whitespace triming

* fix: define DJANGO_SETTINGS_MODULE for the cms debug pods

* fix: use the DRYDOCK_CMS_SSO_USER variable on the init jobs ([`fb36c65`](https://github.com/eduNEXT/drydock/commit/fb36c657e998a5f7bb68f94ad3695089e601c24b))

### Refactor

* refactor: rename CMS SSO user to avoid conflicts with existent data (#24) ([`6842da5`](https://github.com/eduNEXT/drydock/commit/6842da52c2878c23abe45075eb29a6bbc0533eed))

### Unknown

* Merge pull request #33 from eduNEXT/catalog-info

chore: adding backstage catalog and owners ([`30108f9`](https://github.com/eduNEXT/drydock/commit/30108f9a1a4ee2097a860f99457218d804233f86))

## v0.4.1 (2022-12-07)

### Feature

* feat: add configuration for container interactivity (#29) ([`fbc4489`](https://github.com/eduNEXT/drydock/commit/fbc4489f0aa48a1b07c9e900fa7d9c9506f680fb))

### Refactor

* refactor: increase default debug replicas to at least one (#30) ([`7de9fbf`](https://github.com/eduNEXT/drydock/commit/7de9fbffd3cfb9b2d283b7c007d2eb0e34ca3941))

## v0.4.0 (2022-12-01)

### Feature

* feat: add templates for debugging purposes (#25)

This PR adds k8s templates for debug pods, i.e pods running with non-production setup (root user, container entrypoint/command changed, ...), which allow developers to debug services like LMS/CMS in a production-like environment. ([`2cc049d`](https://github.com/eduNEXT/drydock/commit/2cc049d485f5335f219e81bd2bf804ea722af549))

### Fix

* fix: add missing patch in V14 templates (#27) ([`bda221b`](https://github.com/eduNEXT/drydock/commit/bda221bff1460a0cf47ce1280332f594ef4898c1))

* fix: use the right target for the forum hpa (#26) ([`49df7d4`](https://github.com/eduNEXT/drydock/commit/49df7d4127aa314bf0b906de688b47ed95a01542))

### Refactor

* refactor: check if forum is defined before adding resources (#28) ([`1ee0ad1`](https://github.com/eduNEXT/drydock/commit/1ee0ad15283d186cfd2a425146c9b32af73f8fff))

## v0.3.4 (2022-11-09)

### Feature

* feat: adding patch to enable multipurpose jobs in an OpenedX installation V14 (#23) ([`75e35a1`](https://github.com/eduNEXT/drydock/commit/75e35a158af5611a7f45d1b9a12e16e609ebe5c4))

## v0.3.3 (2022-11-09)

### Feature

* feat: adding patch to enable multipurpose jobs in an OpenedX installation (#22) ([`44d336d`](https://github.com/eduNEXT/drydock/commit/44d336d12d89a32e37e6ac3867e651a2c957551c))

## v0.3.2 (2022-11-01)

### Fix

* fix: add missing labels for notes jobs (#21) ([`0428575`](https://github.com/eduNEXT/drydock/commit/04285754bbb76086801ef3f5b68d432cd7031b20))

## v0.3.1 (2022-10-21)

### Feature

* feat: refactor hpa with latest practices (#19) ([`3009617`](https://github.com/eduNEXT/drydock/commit/3009617687d50847d59a4fcfd584d5c4b3509994))

## v0.3.0 (2022-10-18)

### Feature

* feat: add templates with tutor14 support (#18) ([`cc392bb`](https://github.com/eduNEXT/drydock/commit/cc392bba4164859f0d907fb572bb72e08c18a3ae))

* feat: make manifests template root configurable through reference (#17) ([`0382752`](https://github.com/eduNEXT/drydock/commit/0382752725f980ebf84f8f2bccaaf61b768e4645))

## v0.2.0 (2022-10-13)

### Feature

* feat: removing MySQL jobs when MySQL running outside the cluster (#15)

* feat: removing MySQL jobs when MySQL service is running outside the cluster

* feat: adding labels to drydock jobs to better identify those from MySQL we want to skip ([`fca2272`](https://github.com/eduNEXT/drydock/commit/fca2272530be8f42e5d7cade135f56bc924bebfa))

* feat: Starting Forum pod in wave 4 to prevent issues before running the Forum job. (#16)

Starting HPA resources in wave 5 to make sure deployments already exist ([`33d8c4a`](https://github.com/eduNEXT/drydock/commit/33d8c4ad02f8b8d989df1f7966dba35fb8c6d9ee))

* feat: add extra-jobs for extra tasks during initialization (#14) ([`bdfa07b`](https://github.com/eduNEXT/drydock/commit/bdfa07ba086ed0e0f26618ca9b8458cf74602aef))

* feat: add toggleable certificates (#13) ([`c021df9`](https://github.com/eduNEXT/drydock/commit/c021df9d99821b373006ae94c3adb7495e0176f7))

* feat: add 1st version of rendered jobs (#10)

This PR adds a list of jobs for the most used services. This list can be configured using a variable defined in the config.yml with optional services such as minio or forum; required services like LMS are not removable. We configured this behavior using waves from argoCD. ([`e0e4162`](https://github.com/eduNEXT/drydock/commit/e0e416213e2a4d3562f4a1e71fce042b2d8bdfbd))

### Fix

* fix: use the correct init command for forum and add missing annotations (#12) ([`9306d54`](https://github.com/eduNEXT/drydock/commit/9306d54451199b35d043e7ba1b1a56990195a959))

* fix: go back to production ingress (#11) ([`3be0bd2`](https://github.com/eduNEXT/drydock/commit/3be0bd2ab4ebca961387df66b04714944df0f0f0))

## v0.1.0 (2022-08-16)

### Feature

* feat: add support for custom certificates ([`809ae3e`](https://github.com/eduNEXT/drydock/commit/809ae3e751d31056f4b54f80d397f6cb4a592048))

* feat: render global environment for prometheus outside tutor-env (#5) ([`f114243`](https://github.com/eduNEXT/drydock/commit/f11424323f20751150fd21cfe15524f1532c3144))

* feat: add newrelic manifests for tutor13 installation (#6) ([`8990e08`](https://github.com/eduNEXT/drydock/commit/8990e080e14c24a64ea8954f5218f4a5f98b344d))

* feat: add kustomize based extensions to the base manifests (#3) ([`2b93163`](https://github.com/eduNEXT/drydock/commit/2b93163090197dedfce5576755052b04a25e852c))

* feat: add a basic manifest repository implementation (#1)

The `BaseManfests` builder will render a standard Tutor environment
based on the templates used in version 13.3.1 of Tutor and use it
as a base of Kustomization application with additional resources as
overlays.

The `TutorExtendedConfig` will return the Tutor configuration values
of the current `TUTOR_ROOT` and will use the default values of
the template set (defined in a file `defaults.yml`) as a fallback. ([`1f8208b`](https://github.com/eduNEXT/drydock/commit/1f8208bfa9d6ca67247449b90aa4db4b52b10b9f))

* feat: cleaning the manifest output a bit ([`aa19367`](https://github.com/eduNEXT/drydock/commit/aa193675435793deebf02af81b148fcf5932d465))

* feat: making tutor_v13 volume sizes configurable ([`6bbebca`](https://github.com/eduNEXT/drydock/commit/6bbebcaf72dbfe7d10a4f99aea84206bc8c4e41f))

* feat: adding a better explanation at the readme ([`95d1490`](https://github.com/eduNEXT/drydock/commit/95d1490e5c45fb331fa003857fabe940045a4295))

* feat: making reference support options ([`7b69f2c`](https://github.com/eduNEXT/drydock/commit/7b69f2c8b756d22bbb9307fb55d7752dd722563b))

* feat: making all the classes be defined by the reference file ([`138307a`](https://github.com/eduNEXT/drydock/commit/138307ab081c982bb7287bb4ebce9b778940d1b3))

* feat: moving the tutor renderer to the actual implementing class ([`e2a6119`](https://github.com/eduNEXT/drydock/commit/e2a611943e4ce72553bebb8847264ae23e7c4768))

* feat: adding readme ([`86f1c66`](https://github.com/eduNEXT/drydock/commit/86f1c66e5bc1355cbddb07d48b5247ae3b926d09))

* feat: connecting with tutor ([`76dec19`](https://github.com/eduNEXT/drydock/commit/76dec193030c1af82465b3d0baaf93f28e819bbb))

* feat: laying the groundwork for the architecture ([`bd6129c`](https://github.com/eduNEXT/drydock/commit/bd6129c3683895d2681c4050b1a010bc6a819cd1))

* feat: stating the purpose and context for this project ([`2ba3280`](https://github.com/eduNEXT/drydock/commit/2ba328034eae987310f70431e49b8a0d625fce90))

### Fix

* fix: setting a default value for DRYDOCK_NEWRELIC_CONFIG variable ([`a67dbf1`](https://github.com/eduNEXT/drydock/commit/a67dbf1a1b183d60dba3dd9797b654d9d92dad8c))

### Unknown

* Merge pull request #8 from eduNEXT/mgs/custom-certs

Add support for custom certificates ([`7859fbd`](https://github.com/eduNEXT/drydock/commit/7859fbddb96220f6b11e326ee1eb3366ce7dca5a))

* Merge pull request #7 from eduNEXT/Jhony/fix_default_newrelic

fix: setting a default value for DRYDOCK_NEWRELIC_CONFIG variable ([`5093cbd`](https://github.com/eduNEXT/drydock/commit/5093cbd735a116280cf5bf676069aecbfd33fa24))

* Initial commit ([`0a9b26b`](https://github.com/eduNEXT/drydock/commit/0a9b26bfec676618ba19e723821a0861337f0bce))
