"""Single source of truth for the package version.

`pyproject.toml` reads it from here (hatchling ``version.path``), and the
``User-Agent`` the SDK sends is built from it.
"""

__version__ = "0.1.0"

__all__ = ["__version__"]
