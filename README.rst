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
- `DRYDOCK_ENABLE_CELERY_TUNING` : Whether to enable celery tuning. Defaults to `true`.
- `DRYDOCK_ENABLE_MULTITENANCY` : Whether to enable multitennacy. Defaults to `true`.
- `DRYDOCK_ENABLE_SCORM` : Whether to enable scorm. Defaults to `true`.
- `DRYDOCK_ENABLE_SENTRY` : Whether to enable sentry. Defaults to `true`.
- `DRYDOCK_SENTRY_DSN` : The sentry DSN. Defaults to `""`.
- `DRYDOCK_POD_LIFECYCLE` : Whether to enable pod lifecycle. Defaults to `true`.

About Drydock v15.8.0
---------------------

This version of Drydock have some important features and improvements, is **highly** recommended to update to this version.

- We had been using a static definition of the initialization jobs, but now we are using the `Tutor filters <https://docs.tutor.edly.io/reference/api/hooks/filters.html>`_ to generate the kubernetes definition of the initialization jobs. This is a big improvement because now we can add new initialization jobs without modifying the Drydock code. The jobs are taken from `COMMANDS_PRE_INIT`, `COMMANDS_INIT` and `CLI_DO_INIT_TASKS` Filters.
- A new `Tutor filter <https://docs.tutor.edly.io/reference/api/hooks/filters.html>`_ **SYNC_WAVES_ORDER** was added to allow define `ArgoCD Sync Waves <https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/>`_ order and apply to the kubernetes resources through **get_sync_waves_for_resource** function.
    We are defined by defult the following order:
    - `All kubernetes resources` (except the ones that are defined in the next waves)
    - `Initialization Jobs`
    - `Upgrade Jobs`: When **DRYDOCK_MIGRATE_FROM** is set, over the Sync Wave 50
    - `CMS and LMS Deployments`: When **DRYDOCK_POD_LIFECYCLE** is active, over the Sync Wave 100
    - `Debug Resources`: When **DRYDOCK_DEBUG** active, over the Sync Wave 100
    - `Horizontal Pod Autoscalers`: When active, over the Sync Wave 150

- **DRYDOCK_MIGRATE_FROM** was added to allow define the version of the OpenedX platform that we are migrating from. From major `13`(maple) to `15`(olive).
    When this variable is set, the `Upgrade Jobs` will be applied over the Sync Wave 50 based on the Tutor Versions between the older and the current version.

.. note::
    You also need to have DRYDOCK_INIT_JOBS set to `true` to apply migrations in case of platform migration.


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
