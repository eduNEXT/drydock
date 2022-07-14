# Drydock Templates

The inventory of template sets used by drydock.

## Template list

1. `kustomized/tutor13`: Kubernetes focused template set. Uses the templates from Tutor v13 as a Kustomize
    base (rendered in the `base` directory) and adds additional resources as an overlay in the
    `extensions` directory.
    The additional resources include:

    ```yaml
    - flowers.yml # A flowers deployment to track celery tasks.
    - hpa.yml     # An Horizontal Pod Autoscaler for lms, cms and workers.
    - ingress.yml # An ingress with certmanager to use instead of caddy as web proxy.
    ```

    The list of variables with their default values can be found in [defaults.yml](kustomized/tutor13/defaults.yml)

    <details>
    <summary>List of patches</summary>

    ```
    {{ patch("drydock-kustomization-resources")}}
    {{ patch("drydock-kustomization-patches")}}
    {{ patch("drydock-overrides") }}
    ```
    </details>

2. `tutor/v13`: Small subset of templates from Tutor v13. Mostly as a proof con concept.

3. `tutor/v13`: Small subset of templates from Tutor v12. Mostly as a proof con concept.
