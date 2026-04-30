import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    from gvrender import render_graphviz

    render_graphviz(
        """
        digraph {
            Hello -> World
            Hello -> Name
        }
        """
    )
    return (render_graphviz,)


@app.cell
def _(render_graphviz):
    # (Optionally) Using graphviz library `pip install graphviz`
    import graphviz
    from gvrender import render_graphviz

    dot = graphviz.Digraph()
    dot.edge("Hello", "World")
    dot.edge("Hello", "Name")
    render_graphviz(dot)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
