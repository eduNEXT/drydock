Drydock
=======

Drydock is an opinionated tool offering a set of Tutor plugins aiming to provide features that enhance the operation of OpenedX installations in Kubernetes. It is developed by `Edunext <https://www.edunext.co/>`_


- A set of Kubernetes Jobs that replace the current tutor jobs with `ArgoCD Sync Waves <https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/>`_ that allow for a more controlled deployment of openedx.
- A set of Kustomization overrides adding `ArgoCD Sync Waves <https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/>`_ annotations to needed additional resources such as debug, workers or hpa.
- Backup cronjobs that allow backup of the MySQL and MongoDB databases.
- Integration of New Relic monitoring
- Add flower deployment for Celery
- Add a custom nginx and cert-manager configuration
- Add a set of debug resources to help diagnose issues

Extra plugins added:

- A patch that allows for the tuning of celery workers via `DRYDOCK_ENABLE_CELERY_TUNING`
- Allows caddy to catch requests for multiple domains through `DRYDOCK_ENABLE_MULTITENANCY`
- Add scorm matcher to caddy through `DRYDOCK_ENABLE_SCORM`
- A patch that allows for the use of sentry via `DRYDOCK_ENABLE_SENTRY` and `DRYDOCK_SENTRY_DSN`
- Patch for cms and lms worker pods to allow pod probes and lifecycle to work properly. Enabled via `DRYDOCK_POD_LIFECYCLE`

Installation
------------

.. code-block:: bash

    tvm plugins install -e git+https://github.com/edunext/drydock#egg=drydock
    tutor plugins enable drydock
    tutor config save

Getting started
---------------

.. code-block:: bash

    tutor config save


Configuration
-------------

The following configuration options are available:

- `DRYDOCK_INIT_JOBS`: Whether run the initialization jobs or not. Defaults to `false`.
- `DRYDOCK_CMS_SSO_USER`: The username of the CMS SSO user. Defaults to `cms`.
- `DRYDOCK_AUTO_TLS`: Whether to use cert-manager to automatically generate TLS certificates. Defaults to `false`.
- `DRYDOCK_FLOWER`: Whether to deploy a flower deployment for celery. Defaults to `false`.
- `DRYDOCK_INGRESS`: Whether to deploy an ingress for the LMS and CMS. Defaults to `false`.
- `DRYDOCK_INGRESS_EXTRA_HOSTS`: A list of extra hosts to add to the ingress. Defaults to `[]`.
- `DRYDOCK_CUSTOM_CERTS`: A dictionary of custom certificates to use with cert-manager. Defaults to `{}`.
- `DRYDOCK_NEWRELIC_LICENSE_KEY`: The New Relic license key. Defaults to `""`.
- `DRYDOCK_DEBUG`: Whether to deploy debug resources. Defaults to `false`.
- `DRYDOCK_ENABLE_CELERY_TUNING`: Whether to enable celery tuning. Defaults to `true`.
- `DRYDOCK_ENABLE_MULTITENANCY`: Whether to enable multitennacy. Defaults to `true`.
- `DRYDOCK_ENABLE_SCORM`: Whether to enable scorm. Defaults to `true`.
- `DRYDOCK_ENABLE_SENTRY`: Whether to enable sentry. Defaults to `true`.
- `DRYDOCK_SENTRY_DSN`: The sentry DSN. Defaults to `""`.
- `DRYDOCK_POD_LIFECYCLE`: Whether to enable pod lifecycle. Defaults to `true`.
- `DRYDOCK_MIGRATE_FROM`: it allows defining the version of the OpenedX platform we are migrating from. It accepts the integer value mapping the origin release, for instance, `13`(maple) or `14`(nutmeg). When this variable is set, a group of `release-specific upgrade jobs` are added to the Kubernetes manifests. These jobs are applied to the cluster in a suitable order (thanks to the GitOps implementation with ArgoCD + sync waves) to guarantee the correct behavior of the platform in the new version. This brings the `tutor k8s upgrade <https://github.com/overhangio/tutor/blob/v16.1.8/tutor/commands/k8s.py#L486>`_ command to the GitOps pattern. The release-specific upgrade jobs are supported from release `13`(maple). Defaults to `0` (which disables release-specific upgrade jobs)
- `DRYDOCK_POST_INIT_DEPLOYMENTS`: A list of Kubernetes deployments to be applied after the initialization jobs. There are specific deployments that won't report a healthy status in ArgoCD unless the initialization requirements are guaranteed (for instance, database users creation). Thanks to the ArgoCD sync waves feature, the deployments defined in this variable can be synchronized in a phase after the execution of the initialization jobs in order to prevent OpenedX environment syncing failures. In most cases this variable should not be changed. Defaults to `["lms", "cms", "lms-worker", "cms-worker", "forum"]`.

.. note::
    You also need to set `DRYDOCK_INIT_JOBS` to `true` to enable the release-specific upgrade jobs in the case of a platform migration.

Job generation
--------------

Tutor doesn't generate manifest files for the initialization jobs, in consequence we can't use GitOps tools like ArgoCD to deploy the initialization jobs.

We had been using a static definition of the initialization jobs, but now we are using the `Tutor filters <https://docs.tutor.edly.io/reference/api/hooks/filters.html>`_ to generate the kubernetes definition of the initialization jobs. This is a big improvement because now we can add new initialization jobs without modifying the Drydock code. The jobs are taken from `COMMANDS_PRE_INIT`, `COMMANDS_INIT` and `CLI_DO_INIT_TASKS` Filters.

ArgoCD Sync Waves Support
-----------------------

`Tutor filter <https://docs.tutor.edly.io/reference/api/hooks/filters.html>`_ **SYNC_WAVES_ORDER** was added to allow define `ArgoCD Sync Waves <https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/>`_ order and apply to the kubernetes resources through **get_sync_waves_for_resource** function.

We are defined by defult the following order:
- `All kubernetes resources` (except the ones that are defined in the next waves)
- `Initialization Jobs`
- `Upgrade Jobs`: When **DRYDOCK_MIGRATE_FROM** is set, over the Sync Wave 50
- `CMS and LMS Deployments`: When **DRYDOCK_POD_LIFECYCLE** is active, over the Sync Wave 100
- `Debug Resources`: When **DRYDOCK_DEBUG** active, over the Sync Wave 100
- `Horizontal Pod Autoscalers`: When active, over the Sync Wave 150

Migration steps
---------------

This guide delineates the necessary steps for a seamless migration to Olive using Drydock, ensuring a smooth transition with careful consideration of potential challenges.

Regarding initialization jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since Drydock version 15.8.1, a new mechanism was introduced to automatically generate Kubernetes
manifest files for the initialization jobs defined by Tutor and Tutor plugins.
The generated files are meant to be used by ArgoCD for deployment.
Previously you would need to write the manifest files for the initialization jobs
manually if you wanted to use a tool like ArgoCD.


1. For Olive, it is necessary to update the version of `Drydock <https://github.com/eduNEXT/drydock>`_ to the latest version 15.x.x in the requirements.txt file of your environment, including:

    .. code:: bash

        git+https://github.com/edunext/drydock@v15.x.x#egg=drydock==15.x.x

2. In the `config.yml` file, include variables that activate the initialization jobs and post-migration jobs:

    .. code:: yaml

        DRYDOCK_INIT_JOBS: True
        DRYDOCK_MIGRATE_FROM: <MAJOR_OF_TUTOR_VERSION>

   Set `DRYDOCK_MIGRATE_FROM` to 13 for migrating from **Maple** or 14 for migrating from **Nutmeg**.

3. Re-generate the configuration by running:

    .. code:: bash

        tutor config save

4. Push the changes generated by previous step to the corresponding manifests repository.

5. In ArgoCD, locate the corresponding application, and sync all resources.

6. If all synchronization occurs without issues, set:

    .. code:: yaml

        DRYDOCK_INIT_JOBS: False

   remove `DRYDOCK_MIGRATE_FROM` from you config file and run:

    .. code:: bash

        tutor config save

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
