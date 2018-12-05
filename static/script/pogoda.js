function getWeather() {
    $.ajax({
        url: "http://127.0.0.1:8080/pogoda/pogoda",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)  
            var top = document.getElementById("pogoda-top");
            var bot = document.getElementById("pogoda-bottom");

            var icon = document.createElement("div")
            icon.className = "float-left";
            icon.innerHTML = data.icon;

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