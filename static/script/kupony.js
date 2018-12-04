function getKuponyMac() {
    $.ajax({
        url: "http://localhost:8080/coupons/mac",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            console.log(data)          
        }
    })
}

function getKuponySubway() {
    $.ajax({
        url: "http://localhost:8080/coupons/subway",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            console.log(data)          
        }
    })  
}

function getKuponyMac() {
    $.ajax({
        url: "http://localhost:8080/coupons/dagrasso",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            console.log(data)          
        }
    })
}