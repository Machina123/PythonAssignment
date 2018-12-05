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
            var right = document.getElementById("pogoda-right");
            var temp = document.getElementById("weather-temp");

            skycons.set("weatherCanvas",data.icon);

            temp.innerHTML = data.temperature +"<sup>&#x2103;</sup";

            right.innerHTML = "Odczuwalna Temperatura: "
            + data.apparentTemperature +"&deg;<br> Ciśnienie powietrza: " + data.pressure + " hPa ";
        }
    })
}

function initWeather() {
    skycons.add("weatherCanvas", Skycons.PARTLY_CLOUDY_DAY);
    skycons.play();
}