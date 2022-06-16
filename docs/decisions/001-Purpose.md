Purpose of this repo
====================


The goal of this project is to make a flexible renderer of a manifest for openedx hosting.


Context:
--------

- Explanation of groove and subsequent forum conversation:
    * https://discuss.openedx.org/t/tech-talk-demo-deploying-multiple-open-edx-instances-onto-a-kubernetes-cluster-with-tutor/4641
    * https://forum.opencraft.com/t/tech-talk-demo-deploying-multiple-open-edx-instances-onto-a-kubernetes-cluster-with-tutor/887
- Proposal of making tutor the supported installation https://discuss.openedx.org/t/lets-talk-about-the-native-installation/3269
- oep-45: https://open-edx-proposals.readthedocs.io/en/latest/architectural-decisions/oep-0045-arch-ops-and-config.html
- oep-45-ADR-tutor: https://open-edx-proposals.readthedocs.io/en/latest/architectural-decisions/oep-0045-arch-ops-and-config.html
- Braindump on Configuration: Today and Future with Cory Lee from edx https://drive.google.com/file/d/1wWfTbhy2blF526Fi4IvJQyFLz_3rawIX/view
- Notes of the BTR meeting in Lisbon https://discuss.openedx.org/t/build-test-release-notes-lisbon-2022/7133


Decision:
---------

1. Create a POC for a ver flexible builder of manifests that focuses on the usecases not covered already by tutor.
2. Use a very flexible architecture that is open for extension from the very conception. Hexagonal architecture was chosen for this.


Consequence:
------------

1. The builder should work as a tutor plugin. Even if it has other standalone cases.
2. Every piece of the builder should be able to be replaced by a different implementation of the same interface.
