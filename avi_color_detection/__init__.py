"""Package entry for Automated Visual Inspection demo."""

from .color_detection import load_color_db, get_color_name, run_interactive, main

__all__ = [
    "load_color_db",
    "get_color_name",
    "run_interactive",
    "main",
]
