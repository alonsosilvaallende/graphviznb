import warnings
import importlib.metadata
import pathlib

import anywidget
import traitlets

warnings.warn(
    "The package 'graphviznb' has been renamed to 'graphviz-nb'. "
    "Please update your dependencies.",
    DeprecationWarning,
    stacklevel=2,
)

from graphviz_nb import *

try:
    __version__ = importlib.metadata.version("graphviznb")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class Widget(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"
    source = traitlets.Unicode('digraph {\n}\n').tag(sync=True)
