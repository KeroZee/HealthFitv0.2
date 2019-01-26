var weight_list = JSON.parse(localStorage.getItem('wlist')) || [];

function setList() {
    weight_list.push(parseInt(localStorage.getItem("weight")));
    if (weight_list.length > 5) {
        weight_list.shift();
    }
    localStorage.setItem('wlist', JSON.stringify(weight_list));
}



function set_weight() {
    var weight = document.getElementById('weight').value;
    if (typeof(Storage) !== "undefined") {
        localStorage.setItem("weight", weight);
        localStorage.setItem("date", new Date().toLocaleDateString());
        localStorage.setItem("weight1", JSON.stringify(weight_list[0]));
        localStorage.setItem("weight2", JSON.stringify(weight_list[1]));
        localStorage.setItem("weight3", JSON.stringify(weight_list[2]));
        localStorage.setItem("weight4", JSON.stringify(weight_list[3]));
        setList();
        location.reload();
    }
}

window.onload = function () {
        localStorage.getItem("wlist");

        var options = new CanvasJS.Chart("chartContainer", {
            animationEnabled: true,
            theme: "light2",
            title: {
                text: "Your Weight records"
            },
            axisX: {
                valueFormatString: "DD MMM"
            },
            axisY: {
                title: "Your Weight (KG)",
                minimum: 0
            },
            toolTip: {
                shared: true
            },
            legend: {
                cursor: "pointer",
                verticalAlign: "bottom",
                horizontalAlign: "left",
                dockInsidePlotArea: true,
                itemclick: toogleDataSeries
            },
            data: [{
                type: "line",
                cursor: "pointer",
                showInLegend: true,
                name: "Weight",
                markerType: "square",
                xValueFormatString: "DD MMM YYYY",
                color: "#F08080",
                yValueFormatString: "#,##0KG",
                dataPoints: [
                    {
                        x: new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate() - 3),
                        y: parseInt(localStorage.getItem("weight3"))
                    }, //124
                    {
                        x: new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate() - 2),
                        y: parseInt(localStorage.getItem("weight2"))
                    },
                    {
                        x: new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate() - 1),
                        y: parseInt(localStorage.getItem("weight1"))
                    },
                    {
                        x: new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate()),
                        y: parseInt(localStorage.getItem("weight"))
                    },
                ]
            }]
        });
        options.render();
    }

function toogleDataSeries(e) {
    if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
        e.dataSeries.visible = false;
    }
    else {
        e.dataSeries.visible = true;
    }
    e.chart.render();
}

