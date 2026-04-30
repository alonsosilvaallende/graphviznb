[![PyPI version](https://badge.fury.io/py/graphviz-nb.svg)](https://badge.fury.io/py/graphviz-nb)
[![License: MIT](https://img.shields.io/badge/License-Apache2.0-yellow.svg)](https://opensource.org/licenses/Apache2.0)

# graphviz-nb

## Render DOT language graphs in notebooks

## Installation

To install the package, run the following command in your environment:
```sh
pip install graphviz-nb
```

or with [uv](https://github.com/astral-sh/uv):

```sh
uv add graphviz-nb
```

## Getting Started

In your notebook, run the following command:
```python
from graphviz_nb import render_graphviz

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
from graphviz_nb import render_graphviz

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

<img width="528" height="296" alt="graphviznb_marimo" src="https://github.com/user-attachments/assets/acf74c6d-1542-4d2c-b506-74fecda60c76" />

Here is a [basic example](https://marimo.app/?slug=p4ka73) of a marimo WebAssembly (WASM) notebook.
