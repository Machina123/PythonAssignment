function getMpkStops() {
    $.ajax({
        url: "http://localhost:8080/mpk/stops",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            console.log(data)          
        }
    })
}