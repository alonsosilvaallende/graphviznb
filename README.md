[![PyPI version](https://badge.fury.io/py/gvrender.svg)](https://badge.fury.io/py/gvrender)
[![License: MIT](https://img.shields.io/badge/License-Apache2.0-yellow.svg)](https://opensource.org/licenses/Apache2.0)

# gvrender

## Render DOT language graphs in notebooks

## Installation

To install the package, run the following command in your environment:
```sh
pip install gvrender
```

or with [uv](https://github.com/astral-sh/uv):

```sh
uv add gvrender
```

## Getting Started

In your notebook, run the following command:
```python
from gvrender import render_graphviz

render_graphviz(
    """
    digraph {
        Hello -> World
        Hello -> Name
    }
    """
)
```
<img width="284" height="184" alt="image" src="https://github.com/user-attachments/assets/10b97699-550f-4983-b4f5-2e600f21ee6f" />


(Optionally) Using graphviz library `pip install graphviz`:
```python
from graphviz import Digraph
from gvrender import render_graphviz

dot = Digraph()
dot.edge("Hello", "World")
dot.edge("Hello", "Name")
render_graphviz(dot)
```

<img width="284" height="184" alt="image" src="https://github.com/user-attachments/assets/10b97699-550f-4983-b4f5-2e600f21ee6f" />

## Render it in a Jupyter notebook

<img width="274" height="275" alt="image" src="https://github.com/user-attachments/assets/2f17a62c-68d3-42ca-a6ce-7aed698fbefe" />

## Render it in a JupyterLite notebook

<img width="287" height="337" alt="image" src="https://github.com/user-attachments/assets/214c1398-ab21-49f4-bdff-6de2cc1da20e" />

## Render it in a marimo notebook or a marimo WebAssembly (WASM) notebook

<img width="272" height="295" alt="image" src="https://github.com/user-attachments/assets/af045ccb-cb42-45fa-87e7-1f6244ec12b8" />

Here is a [basic example](https://marimo.app/?slug=zza2j4) of a marimo WebAssembly (WASM) notebook.
