"""
These hooks are stored in a separate module. If they were included in plugin.py, then
the pod-autoscaling hooks would be created in the context of some other plugin that imports
them.
"""

from __future__ import annotations

from tutor.core.hooks import Filter

SYNC_WAVES_ORDER_ATTRS_TYPE = dict[str, int]

SYNC_WAVES_ORDER: Filter[SYNC_WAVES_ORDER_ATTRS_TYPE, tuple] = Filter()
