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
