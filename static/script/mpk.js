function getMpkStops() {
    $.ajax({
        url: "http://localhost:8080/mpk/stops",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            var stopPicker = document.getElementById("przystanek");
            stopPicker.innerHTML = "";
            for(var key in data) {
                var stopObject = document.createElement("option");
                stopObject.innerText = key;
                stopObject.setAttribute("value", data[key]);
                stopPicker.appendChild(stopObject);
            }        
        }
    })
}

function getMpkSchedule() {
    var stopId = $("#przystanek").val()
    $.ajax({
        url: "http://localhost:8080/mpk/departures?stop=" + stopId,
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            var departuresPlaceholder = document.getElementById("mpk_rozklad");
            departuresPlaceholder.innerHTML = "";
            for(var i = 0; i < data.actual.length; i++) {
                var departData = data.actual[i];
                var departure = document.createElement("p")
                departure.innerHTML = departData.patternText + " &rarr; " + departData.direction + ": " + departData.mixedTime
                departuresPlaceholder.appendChild(departure);
            }       
        }
    })
}