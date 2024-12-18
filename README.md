Drydock
=======

Drydock is an opinionated tool offering a set of Tutor plugins aiming to provide features that enhance the operation of OpenedX installations in Kubernetes. It is developed by [Edunext](https://www.edunext.co/).

- A set of Kubernetes Jobs that replace the current tutor jobs with [ArgoCD Sync Waves](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/) that allow for a more controlled deployment of openedx.
- A set of Kustomization overrides adding [ArgoCD Sync Waves](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/) annotations to needed additional resources such as debug, workers or hpa.
- Backup cronjobs that allow backup of the MySQL and MongoDB databases.
- Integration of New Relic monitoring
- Add a custom nginx and cert-manager configuration
- Add a set of debug resources to help diagnose issues

Extra plugins added:

- Allows caddy to catch requests for multiple domains through `DRYDOCK_ENABLE_MULTITENANCY`
- Add scorm matcher to caddy through `DRYDOCK_ENABLE_SCORM`
- Patch for cms and lms worker pods to allow pod probes and lifecycle to work properly. Enabled via `DRYDOCK_POD_LIFECYCLE`

Version compatibility matrix
----------------------------

You must install a supported release of this plugin to match the Open
edX and Tutor version you are deploying. If you are installing this
plugin from a branch in this Git repository, you must select the
appropriate one:

| Open edX release | Tutor version     | Plugin branch | Plugin release |
|------------------|-------------------|---------------|----------------|
| Maple            | `>=13.2, <14`     | Not supported | 0.7.x          |
| Nutmeg           | `>=14.0, <15`     | Not supported | 0.7.x          |
| Olive            | `>=15.0, <16`     | Not supported | 15.x.x         |
| Palm             | `>=16.0, <17`     | Not supported | 16.x.x         |
| Quince           | `>=17.0, <18`     | `quince`      | 17.x.x         |
| Redwood          | `>=18.0, <19`     | `redwood`     | 18.x.x         |
| Sumac          | `>=19.0, <20`     | `main`        | >=19.0.0       |

Installation
------------

``` bash
pip install tutor-contrib-drydock
tutor plugins enable drydock
tutor config save
```

Getting started
---------------

``` bash
tutor config save
```

Configuration
-------------

The following configuration options are available:

- `DRYDOCK_INIT_JOBS`: Whether run the initialization jobs or not. Defaults to `false`.
- `DRYDOCK_CMS_SSO_USER`: The username of the CMS SSO user. Defaults to `cms`.
- `DRYDOCK_AUTO_TLS`: Whether to use cert-manager to automatically generate TLS certificates. Defaults to `true`.
- `DRYDOCK_INGRESS`: Whether to deploy an ingress for the LMS and CMS. Defaults to `true`.
- `DRYDOCK_INGRESS_EXTRA_HOSTS`: A list of extra hosts to add to the ingress. Defaults to `[]`.
- `DRYDOCK_INGRESS_LMS_EXTRA_HOSTS`: A list of extra hosts to add to the LMS ingress. Defaults to `[]`.
- `DRYDOCK_CUSTOM_CERTS`: A dictionary of custom certificates to use with cert-manager. Defaults to `{}`.
- `DRYDOCK_NEWRELIC_LICENSE_KEY`: The New Relic license key. Defaults to `""`.
- `DRYDOCK_DEBUG`: Whether to deploy debug resources. Defaults to `false`.
- `DRYDOCK_ENABLE_MULTITENANCY`: Whether to enable multitennacy. Defaults to `true`.
- `DRYDOCK_ENABLE_SCORM`: Whether to enable scorm. Defaults to `true`.
- `DRYDOCK_POD_LIFECYCLE`: Whether to enable pod lifecycle. Defaults to `true`.
- `NGINX_STATIC_CACHE_CONFIG`: A list of dictionaries with settings for different services to cache their assets in NGINX.
  The following is an example of the expected values:
  ```yaml
  NGINX_STATIC_CACHE_CONFIG:
    {{service_name}}:
        host: {{service_host}} # e.g: {{LMS_HOST}}
        path: /static/ # you can specify a different path
        port: {{service_port}} # only needed if you have DRYDOCK_BYPASS_CADDY enabled
  ```
- `DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_MFE`: The minimum available percentage for the MFE's PodDisruptionBudget. To disable the PodDisruptionBudget, set `0`. Defaults to `0`.
- `DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_FORUM`: The minimum available percentage for the FORUM's PodDisruptionBudget. To disable the PodDisruptionBudget, set `0`. Defaults to `0`.
- `DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_CADDY`: The minimum available percentage for the CADDY's PodDisruptionBudget. To disable the PodDisruptionBudget, set `0`. Defaults to `0`.
- `DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_LMS`: The minimum available percentage for the LMS's PodDisruptionBudget. To disable the PodDisruptionBudget, set `0`. Defaults to `0`.
- `DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_LMS_WORKER`: The minimum available percentage for the LMS WORKER's PodDisruptionBudget. To disable the PodDisruptionBudget, set `0`. Defaults to `0`.
- `DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_CMS`: The minimum available percentage for the CMS's PodDisruptionBudget. To disable the PodDisruptionBudget, set `0`. Defaults to `0`.
- `DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_CMS_WORKER`: The minimum available percentage for the worker's PodDisruptionBudget. To disable the PodDisruptionBudget, set `0`. Defaults to `0`.
- `DRYDOCK_MIGRATE_FROM`: it allows defining the version of the OpenedX platform we are migrating from. It accepts the integer value mapping the origin release, for instance, `13`(maple) or `14`(nutmeg). When this variable is set, a group of `release-specific upgrade jobs` are added to the Kubernetes manifests. These jobs are applied to the cluster in a suitable order (thanks to the GitOps implementation with ArgoCD + sync waves) to guarantee the correct behavior of the platform in the new version. This brings the `tutor k8s upgrade <https://github.com/overhangio/tutor/blob/v15.3.7/tutor/commands/k8s.py#L484>`_ command to the GitOps pattern. The release-specific upgrade jobs are supported from release `13`(maple). Defaults to `0` (which disables release-specific upgrade jobs)

> **_NOTE:_** You also need to set `DRYDOCK_INIT_JOBS` to `true` to enable the release-specific upgrade jobs in the case of a platform migration.

Job generation
--------------

Tutor doesn't generate manifest files for the initialization jobs, in consequence we can't use GitOps tools like ArgoCD to deploy the initialization jobs.

We had been using a static definition of the initialization jobs, but now we are using the `Tutor filters <https://docs.tutor.edly.io/reference/api/hooks/filters.html>`_ to generate the kubernetes definition of the initialization jobs. This is a big improvement because now we can add new initialization jobs without modifying the Drydock code. The jobs are taken from `COMMANDS_PRE_INIT`, `COMMANDS_INIT` and `CLI_DO_INIT_TASKS` Filters.

ArgoCD Sync Waves Support
-----------------------

[Tutor filter](https://docs.tutor.edly.io/reference/api/hooks/filters.html) **SYNC_WAVES_ORDER** was added to allow define [ArgoCD Sync Waves](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/) order and apply to the kubernetes resources through **get_sync_waves_for_resource** function.

We are defined by defult the following order:

1. `All kubernetes resources` (except the ones that are defined in the next waves)
2. `Initialization Jobs`
3. `Upgrade Jobs`: When **DRYDOCK_MIGRATE_FROM** is set, over the Sync Wave 50
4. `CMS and LMS Deployments`: When **DRYDOCK_POD_LIFECYCLE** is active, over the Sync Wave 100
5. `Debug Resources`: When **DRYDOCK_DEBUG** active, over the Sync Wave 100
6. `Horizontal Pod Autoscalers`: When active, over the Sync Wave 150

Workaround to upgrade from Maple to Palm or later
-------------------------------------------------

> **_NOTE:_** Quince uses Django 4.2 which only supports MySQL 8 or higher. You must upgrade your version of MySQL prior to performing the upgrade.

The upgrade from Maple to Palm fails because an issue with a squashed migration in [edx-enterprise](https://github.com/openedx/edx-enterprise/blob/3.61.11/integrated_channels/blackboard/migrations/0001_initial_squashed_0014_alter_blackboardlearnerassessmentdatatransmissionaudit_enterprise_course_enrollment_id.py). To go around this issue, we need to apply migrations using an older version of edx-enterprise (3.60.4).

1. Run the sync to Palm without enabling the init jobs or upgrade jobs.

2. Once the LMS Deployment is running in the Palm version, go inside a pod and run the following:

    ``` bash
    pip install edx-enterprise==3.60.4
    ./manage.py lms migrate
    pip install edx-enterprise==3.61.11
    ```

3. Now, you can enable the init jobs and upgrade jobs and run the sync again.

This workaround references the [Andrey's comment](https://discuss.openedx.org/t/updating-tutor-lilac-to-palm-now-that-palms-released-fails/10557/23)

Migration steps
---------------

This guide delineates the necessary steps for a seamless migration to Quince using Drydock, ensuring a smooth transition with careful consideration of potential challenges.

### Regarding initialization jobs

Since Drydock version 17.3.0, a new mechanism was introduced to automatically generate Kubernetes
manifest files for the initialization jobs defined by Tutor and Tutor plugins.
The generated files are meant to be used by ArgoCD for deployment.
Previously you would need to write the manifest files for the initialization jobs
manually if you wanted to use a tool like ArgoCD.

1. For Quince, it is necessary to update the version of [Drydock](https://github.com/eduNEXT/drydock) to the latest version 17.x.x in the requirements.txt file of your environment, including:

    ``` bash
    git+https://github.com/edunext/drydock@v17.x.x#egg=drydock==17.x.x
    ```

2. In the `config.yml` file, include variables that activate the initialization jobs and post-migration jobs:

    ``` yaml
    DRYDOCK_INIT_JOBS: True
    DRYDOCK_MIGRATE_FROM: <MAJOR_OF_TUTOR_VERSION>
    ```

   Set `DRYDOCK_MIGRATE_FROM` to the integer value mapping the origin release, for instance, `13`(Maple) or `14`(Nutmeg). Please refer to the Drydock configuration reference for a full description.

3. Re-generate the configuration by running:

    ```bash
    tutor config save
    ```

4. Push the changes generated by previous step to the corresponding manifests repository.

5. In ArgoCD, locate the corresponding application, and sync all resources.

6. If all synchronization occurs without issues, set:

    ```yaml
    DRYDOCK_INIT_JOBS: False
    ```

    remove `DRYDOCK_MIGRATE_FROM` from you config file and run:

    ```bash
    tutor config save
    ```

7. Push the changes and sync again in ArgoCD.

Rationale
---------

This project is proposed as a possible way of creating a community maintained
reference for large openedx installation.
Sometimes the needs for customization in large instances of openedx goes
against the required simplicity in the configuration that the tutor project
strives for. In those cases, the solution is to create a tutor plugin that
allows for such advanced customization options.

This projects intends to fill that gap with a solution that should allow many
community members to collaborate in one repo on the heavy toll that is the
maintainance of openedx operations.

License
-------

This software is licensed under the terms of the AGPLv3.
