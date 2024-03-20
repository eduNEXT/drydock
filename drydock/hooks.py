"""
These hooks are stored in a separate module. If they were included in plugin.py, then
the pod-autoscaling hooks would be created in the context of some other plugin that imports
them.
"""

from __future__ import annotations

import typing as t

from tutor.core.hooks import Filter

SYNC_WAVES_ORDER_ATTRS_TYPE = t.Dict[str, int]

SYNC_WAVES_ORDER: Filter[dict[str, SYNC_WAVES_ORDER_ATTRS_TYPE], []] = Filter()
