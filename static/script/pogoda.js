function getWeather() {
    $.ajax({
        url: "http://127.0.0.1:8080/pogoda/pogoda",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)
            var pogoda = document.getElementById("weather");
            pogoda.innerHTML = data.summary;         
        }
    })
}