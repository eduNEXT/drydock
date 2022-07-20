drydock: a flexible manifest builder for Open edX
=================================================

**⚠️ Warning**: drydock is currently in an alpha stage and may suffer substantial changes
while it transitions in to a stable stage.


Installation
------------

::

    tvm plugins install -e git+https://github.com/edunext/drydock#egg=drydock
    tutor plugins enable drydock

Getting started
---------------

Drydock aims to offer flexibility on the kind of environment you want to generate, for that reason
you can chose different kind of implementations (of renderers?) depending on your needs. At the
moment Drydock ships with a basic manifest builder that wraps the Kubernetes generated files by tutor
in a Kustomize application with some useful extra resources.

To use drydock just use the reference that defines the implementation you want drydock to use and run:

..  code:: bash

    tutor drydock save -r reference.yml

An example reference would look something like this:

..  code:: yaml

    drydock:
      builder_class:  drydock.manifest_builder.application.manifest_builder.ManifestBuilder
      config_class: drydock.manifest_builder.infrastructure.tutor_config.TutorConfig
      manifest_class: drydock.manifest_builder.infrastructure.tutor_based_manifests.BaseManifests
      manifest_options:
        output: "drydock-environment"

This will render the default drydock environment on the `drydock-environment` directory, allowing
you to check the files onto version control and use tools for continuous deployment such as
Flux or ArgoCD. The default environment is generated using Tutor and its templates, as a result
it should be compatible with all the plugins, variables and patches.

**Note:** If you are using module or yaml plugins in tutor and set ``manifest_options.output=env``
you will have to define your ``TUTOR_PLUGINS_ROOT`` outside of your ``TUTOR_ROOT`` because 
drydock will override your tutor env and erase your plugins.


Extended builder
~~~~~~~~~~~~~~~~
Drydock also ships with an extended builder that adds the ability to use arbitrary
templates as an extra overlay for the Kustomize app used by the base builder.
To use it one must run drydock with the following reference:

..  code:: yaml

    ---
    drydock:
      builder_class:  drydock.manifest_builder.application.manifest_builder.ManifestBuilder
      config_class: drydock.manifest_builder.infrastructure.tutor_config.TutorExtendedConfig
      manifest_class: drydock.manifest_builder.infrastructure.tutor_based_manifests.ExtendedManifest
      manifest_options:
        output: "env"
        extra_templates: extra_templates_root

Where ``extra_templates_root`` points to the directory that holds your extra templates.
In ``extra_templates_root`` you must include an directory named ``extra-extensions``.
Inside ``extra-extensions`` you can write any template that you want but is meant to
be used as a Kustomize overlay, therefore you will need at least a Kustomization.yml file.

One use case is to use the extended builder to add helm chart definitions:

..  code:: yaml

    # extra_templates_root/extra-extensions/kustomization.yml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization

    helmCharts:
      - name: ingress-nginx
        repo: https://kubernetes.github.io/ingress-nginx
        namespace: ingress-nginx
        version: 4.0.18
        releaseName: ingress-nginxx

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
