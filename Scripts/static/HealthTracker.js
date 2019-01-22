var heartrate_list = JSON.parse(localStorage.getItem('list')) || [];

function Multiply() {
    var x = document.getElementById("bpm").value;
    if (typeof(Storage) !== "undefined") {
        localStorage.setItem("bpm", x);
        localStorage.setItem("date", new Date().toLocaleDateString());
        document.getElementById("record").innerHTML = localStorage.getItem("bpm");
        document.getElementById("date").innerHTML = localStorage.getItem("date");
        localStorage.setItem("bpm1", JSON.stringify(heartrate_list[1]));
        localStorage.setItem("bpm2", JSON.stringify(heartrate_list[2]));
        localStorage.setItem("bpm3", JSON.stringify(heartrate_list[3]));
        localStorage.setItem("bpm4", JSON.stringify(heartrate_list[4]));
        setList();
        Condition();
        location.reload();
        }
}

function Condition(){
    var y = localStorage.getItem("bpm");
    if (y < 60){
        localStorage.setItem("condition", "Poor");
        localStorage.setItem("recommend", "Adjusting or discontinuing your medical regimens, Using a pacemaker. You may not need treatment if you don't have symptoms.")
        document.getElementById("condition").innerHTML = localStorage.getItem("condition");
        document.getElementById("recommend").innerHTML = localStorage.getItem("recommend");
    } else if (y >= 60, y <= 100) {
        localStorage.setItem("condition", "Good");
        localStorage.setItem("recommend", "Having a mixture of sedentary, vigorous and moderate intensity activities/exercises to ensure that your heart rate stays in this condition. You will not need treatment unless your heart condition changes.")
        document.getElementById("condition").innerHTML = localStorage.getItem("condition");
        document.getElementById("recommend").innerHTML = localStorage.getItem("recommend");
    } else if (y > 100, y <= 140) {
        localStorage.setItem("condition", "Critical");
        localStorage.setItem("recommend", "Carotid sinus massage, Pressing gently on the eyeballs with eyes closed under the supervision of a healthcare physician, Valsalva manoeuvre, Using the dive reflex, Sedation, Cutting down on coffee or caffeinated substances, Cutting down on alcohol, Quitting tobacco use, Getting more rest")
        document.getElementById("condition").innerHTML = localStorage.getItem("condition");
        document.getElementById("recommend").innerHTML = localStorage.getItem("recommend");
    } else if (y > 140) {
        localStorage.setItem("condition", "Hazardous");
        localStorage.setItem("recommend", "Carotid sinus massage, Taking medication including digoxin, verapamil and beta blockers, Electric shock treatment, Catheter ablation, Valsalva manoeuvre, Dipping your face into cold water during an attack. In many cases, the symptoms stop quickly and no treatment is needed.")
        document.getElementById("condition").innerHTML = localStorage.getItem("condition");
        document.getElementById("recommend").innerHTML = localStorage.getItem("recommend");
    }
}


function setList() {
    heartrate_list.push(parseInt(localStorage.getItem("bpm")));
    if (heartrate_list.length > 5) {
        heartrate_list.shift();
    }
    localStorage.setItem('list', JSON.stringify(heartrate_list));
}

window.onload = function () {
    localStorage.getItem("list");
    document.getElementById("record").innerHTML = localStorage.getItem("bpm");
    document.getElementById("date").innerHTML = localStorage.getItem("date");
    document.getElementById("condition").innerHTML = localStorage.getItem("condition");
    document.getElementById("recommend").innerHTML = localStorage.getItem("recommend");

    var options = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        theme: "light2",
        title: {
            //text: "Health Tracker"
        },
        axisX: {
            valueFormatString: "DD MMM"
        },
        axisY: {
            title: "Heart Rates (Beats per Minute)",
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
            name: "Heart Rate",
            markerType: "square",
            xValueFormatString: "DD MMM YYYY",
            color: "#F08080",
            yValueFormatString: "#,##0BPM",
            dataPoints: [
                {x: new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate() - 4), y: parseInt(localStorage.getItem("bpm1"))},
                {x: new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate() - 3), y: parseInt(localStorage.getItem("bpm2"))},
                {x: new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate() - 2), y: parseInt(localStorage.getItem("bpm3"))},
                {x: new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate() - 1), y: parseInt(localStorage.getItem("bpm4"))},
                {x: new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate()), y: parseInt(localStorage.getItem("bpm"))},
            ]
        }]
    });
    options.render();

function toogleDataSeries(e) {
    if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
        e.dataSeries.visible = false;
    } else {
        e.dataSeries.visible = true;
    }
    e.chart.render();
}

}