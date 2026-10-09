### Fixed

- Remove the per-MFE paths from the LMS and CMS ingresses. They were a leftover
  from the removed Caddy bypass, all of them pointed to the same backend as the
  `/` path, and they generated duplicated paths such as `/learning`.
