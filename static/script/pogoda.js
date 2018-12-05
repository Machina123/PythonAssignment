const POGODA_ENDPOINT_BASE = window.location.protocol + "//" + window.location.host + "/pogoda"
const POGODA_ENDPOINTS = {
    pogoda: POGODA_ENDPOINT_BASE + "/pogoda"
}

var skycons = new Skycons({"color": "white"});

function getWeather() {
    $.ajax({
        url: POGODA_ENDPOINTS.pogoda,
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)  
            var top = document.getElementById("pogoda-top");
            var bot = document.getElementById("pogoda-bottom");

            skycons.set("weatherCanvas",data.icon);

            var summary = document.createElement("p");
            summary.className = "float-right";
            summary.innerHTML = data.summary;

            bot.innerHTML = "Temperatura: " + data.temperature +"&deg;<br>Odczuwalna Temperatura: "
            + data.apparentTemperature +"&deg;<br> Ciśnienie powietrza: " + data.pressure + " hPa";

            top.appendChild(icon);
            top.appendChild(summary);
        }
    })
}

function initWeather() {
    skycons.add("weatherCanvas", Skycons.PARTLY_CLOUDY_DAY);
    skycons.play();
}