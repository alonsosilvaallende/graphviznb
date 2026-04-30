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

(Optionally) Using graphviz library `pip install graphviz`:
```python
import graphviz
from gvrender import render_graphviz

dot = graphviz.Digraph()
dot.edge("Hello", "World")
dot.edge("Hello", "Name")
render_graphviz(dot)
```

<img width="284" height="184" alt="image" src="https://github.com/user-attachments/assets/10b97699-550f-4983-b4f5-2e600f21ee6f" />

## Render it in a Jupyter notebook

<img width="515" height="334" alt="graphviznb" src="https://github.com/user-attachments/assets/2162bab0-02e1-4f8f-85dd-5335f03cda95" />

## Render it in a JupyterLite notebook

<img width="482" height="301" alt="graphviznb_jupyterlite" src="https://github.com/user-attachments/assets/d0d065aa-2ee9-41b2-a8cf-fa6ad50855e0" />

## Render it in a marimo notebook or a marimo WebAssembly (WASM) notebook

<img width="272" height="295" alt="image" src="https://github.com/user-attachments/assets/af045ccb-cb42-45fa-87e7-1f6244ec12b8" />

Here is a [basic example](https://marimo.app/?slug=p4ka73) of a marimo WebAssembly (WASM) notebook.
