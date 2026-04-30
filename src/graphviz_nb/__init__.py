import importlib.metadata
import pathlib

import anywidget
import traitlets

try:
    __version__ = importlib.metadata.version("graphviz-nb")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


def get_source(variable):
    if isinstance(variable, str):
        return variable
    
    try:
        import graphviz

        if isinstance(variable, (graphviz.graphs.Digraph, graphviz.graphs.Graph)):
            return variable.source

    except ImportError:
        print("Warning: graphviz is not installed. Run: pip install graphviz")

    return f"unknown: {type(variable).__name__}"


class render_graphviz(anywidget.AnyWidget):
    '''Widget to render graphviz string or a graphviz Digraph/Graph object.

    Examples:
        ```python
        from graphviz_nb import render_graphviz

        dot = render_graphviz("""
                  digraph {
                      Hello -> World
                      Hello -> Name
                  }
              """)
        dot
        ```
    '''
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"
    source = traitlets.Unicode('digraph {\n}\n').tag(sync=True)

    def __init__(
        self,
        source: str = "digraph {\n}\n",
        **kwargs
    ):
        """Render a graphviz string or a graphviz Digraph/Graph object.

        Args:
            source (Union[str, graphviz.graphs.Digraph, graphviz.graphs.Graph]): source string or a graphviz Digraph/Graph object.
            **kwargs: Forwarded to ``anywidget.AnyWidget``.
        """

        super().__init__(
            source=get_source(source),
            **kwargs
        )
