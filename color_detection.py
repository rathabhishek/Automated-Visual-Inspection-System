"""Thin compatibility wrapper re-exporting the packaged API.

This file keeps `import color_detection` working for backwards compatibility
with existing code/tests while the real implementation lives in the
`avi_color_detection` package.
"""

from avi_color_detection import load_color_db, get_color_name, run_interactive, main

__all__ = ["load_color_db", "get_color_name", "run_interactive", "main"]


if __name__ == "__main__":
    main()
