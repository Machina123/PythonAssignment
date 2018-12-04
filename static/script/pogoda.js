function getWeather() {
    $.ajax({
        url: "http://localhost:8080/pogoda/pogoda",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            console.log(data)          
        }
    })
}