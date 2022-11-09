function createGraphs(logsData) {
    const jsonData = JSON.parse(logsData);

    let mainContainer = document.getElementById("content-container");

    for (let i=0; i<jsonData.length; i++) {
        const day = jsonData[i].day;
        const data = jsonData[i].data;

        const container = createGraphContainer(day);
        mainContainer.appendChild(container);

        const datasets = createDatasetFromData(data);

        createGraph(day, datasets);
    }
}


function createGraphContainer(date) {
    let container = document.createElement("div");
    container.classList.add("content-item");

    let containerHeader = document.createElement("div");
    containerHeader.classList.add("item-header")
    let header = document.createElement("h2");
    header.innerHTML = date;

    containerHeader.appendChild(header);

    let containerContent = document.createElement("div");
    containerContent.classList.add("item-content")
    containerContent.id = date;

    container.appendChild(containerHeader);
    container.appendChild(containerContent);

    return container;
}


function createDatasetFromData(data) {
    let datasetY = [];
    let datasetX = [];

    for (let i=0; i<data.length; i++) {
        datasetX.push(data[i].time);
        datasetY.push(data[i].value);
    }

    return {
        x: datasetX,
        y: datasetY
    };
}


function createGraph(date, datasets) {
    const graphContainer = document.getElementById(date);

    let graphCanvas = document.createElement("canvas");
    graphCanvas.id = date;

    graphContainer.appendChild(graphCanvas);

    new Chart(graphCanvas.getContext("2d"), {
          type: "line",
          data: {
            labels: datasets.x,
            datasets: [{
              fill: false,
              lineTension: 0,
              backgroundColor: "#FB8122",
                  borderColor: "#1D2228",
              data: datasets.y
            }]
          },
          options: {
            plugins: {
                legend: {
                    display: false
                },
            }
          }
        });
}