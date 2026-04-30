import * as Viz from "https://esm.sh/@viz-js/viz";

function render({ model, el }) {
  let getSource = () => model.get("source");
  // container for the graph
  let graphContainer = document.createElement("div");
  el.appendChild(graphContainer);
  // load Viz instance & render
  Viz.instance().then(viz => {
    const svgElement = viz.renderSVGElement(`${getSource()}`);
    graphContainer.appendChild(svgElement);
  }).catch(err => {
    console.error("Viz render error:", err);
  });
}
export default { render };
