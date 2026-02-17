# graphviznb

## Render DOT language graphs in notebooks without installing graphviz

## Installation

To install the package, run the following command in your environment:
```sh
pip install graphviznb
```

or with [uv](https://github.com/astral-sh/uv):

```sh
uv pip install graphviznb
```

## Getting Started

In your notebook, run the following command:
```
import graphviznb

w = graphviznb.Widget()
w.source = 'digraph {\n\tHello -> World\n\tHello -> Antonia\n}\n'
w
```

