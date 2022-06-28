drydock: a flexible manifest builder for Open edX
=================================================

Installation
------------

::

    tvm plugins install -e git+https://github.com/edunext/drydock#egg=drydock

Usage
-----

::

    tutor plugins enable drydock
    tutor drydock save -r drydock/references/tutor_v13.yml


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
