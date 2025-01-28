"""
=========================================================

Data I/O (:mod:`rheedium.sim`)

=========================================================

This package contains the modules for simulating RHEED patterns.
"""

from .simulator import *  # This will expose all functions from data_io.py

# Get all functions defined in data_io.py for __all__
import inspect
import sys
from . import simulator

__all__ = [
    name for name, obj in inspect.getmembers(sys.modules["rheedium.sim.simulator"])
    if inspect.isfunction(obj) and not name.startswith("_")
]
