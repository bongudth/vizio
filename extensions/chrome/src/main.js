import { default as Viz } from "@viz-js/viz";

document.addEventListener("mouseup", function (event) {
  let selectedText = window.getSelection().toString();

  if (selectedText !== "" && document.getElementById("vizio-button") === null) {
    createButton(event, selectedText);
  }
});

document.addEventListener("mousedown", function (event) {
  let button = document.getElementById("vizio-button");
  if (button && event.target !== button) {
    removeButton();
  }
});

function createButton(event, code) {
  let button = document.createElement("button");
  button.id = "vizio-button";
  button.innerText = "View flowchart";

  button.style.position = "absolute";
  button.style.top = event.clientY + "px";
  button.style.left = event.clientX + "px";
  button.style.zIndex = "9999";
  button.style.backgroundColor = "white";
  button.style.color = "#1877f2";
  button.style.border = "1px solid #1877f2";
  button.style.borderRadius = "4px";
  button.style.padding = "4px 8px";
  button.style.cursor = "pointer";

  document.body.appendChild(button);

  button.onclick = function () {
    generateFlowchart(code);
    removeButton();
  };
}

window.onload = function () {
  const vizioGenerateBtn = document.getElementById("vizio-generate");
  if (vizioGenerateBtn) {
    vizioGenerateBtn.onclick = function () {
      const vizioCode = document.getElementById("vizio-code").value;
      generateFlowchart(vizioCode);
    };
  }
};

function removeButton() {
  let button = document.getElementById("vizio-button");
  if (button) {
    button.remove();
  }
}

async function generateFlowchart(code) {
  let url =
    "https://b3rmosfql9.execute-api.ap-southeast-1.amazonaws.com/generate_viz_devs";
  let payload = {
    source_code: code,
  };
  await fetch(url, {
    method: "POST",
    body: JSON.stringify(payload),
  })
    .then((response) => response.json())
    .then((data) => {
      const dotContent = data.results;
      createImage(dotContent);
    })
    .catch((error) => {
      console.log("error", error);
    });
}

function createImage(dotContent) {
  const viz = Viz.instance();
  viz.then(function (viz) {
    const svg = viz.renderSVGElement(dotContent);
    const w = window.open("");
    w.document.body.appendChild(svg);

    const buttonDownload = document.createElement("button");
    buttonDownload.id = "vizio-download";
    buttonDownload.innerText = "Download SVG";

    buttonDownload.style.backgroundColor = "white";
    buttonDownload.style.color = "#1877f2";
    buttonDownload.style.border = "1px solid #1877f2";
    buttonDownload.style.borderRadius = "4px";
    buttonDownload.style.padding = "4px 8px";
    buttonDownload.style.cursor = "pointer";
    buttonDownload.style.marginBottom = "10px";

    w.document.body.appendChild(buttonDownload);

    buttonDownload.onclick = function () {
      const svgContent = new XMLSerializer().serializeToString(svg);
      const blob = new Blob([svgContent], {
        type: "image/svg+xml;charset=utf-8",
      });
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = "flowchart.svg";
      link.click();
    };
  });
}
