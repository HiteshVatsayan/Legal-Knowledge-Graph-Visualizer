// script.js

function getNodeInfo() {
    var nodeInput = document.getElementById("nodeInput");
    var nodeLabel;
    
    if (nodeInput.value === "custom") {
        nodeLabel = document.getElementById("customNodeLabel").value;
    } else {
        nodeLabel = nodeInput.value;
    }
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/get_node_info", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            displayResult(response);
        }
    };
    var data = JSON.stringify({ label: nodeLabel });
    xhr.send(data);
}

function displayResult(data) {
    var resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "<h2>Node Information</h2>";
    if (data.length === 0) {
        resultDiv.innerHTML += "<p>No information found for this node label.</p>";
    } else {
        var table = "<table><tr><th>Label</th><th>Definition</th><th>Superclass</th></tr>";
        for (var i = 0; i < data.length; i++) {
            table += "<tr><td>" + data[i].label + "</td><td>" + data[i].definition + "</td><td>" + data[i].superclass + "</td></tr>";
        }
        table += "</table>";
        resultDiv.innerHTML += table;
    }
}

// Function to show/hide custom node label input field
document.getElementById("nodeInput").addEventListener("change", function() {
    var customInput = document.getElementById("customNodeLabel");
    if (this.value === "custom") {
        customInput.style.display = "block";
    } else {
        customInput.style.display = "none";
    }
});
