function getTvn() {
    $.ajax({
        url: "http://localhost:8080/info/tvn",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            console.log(data)          
        }
    })
}

function getRmf() {
    $.ajax({
        url: "http://localhost:8080/info/rmf",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            console.log(data)          
        }
    })
}

function getInteria() {
    $.ajax({
        url: "http://localhost:8080/info/interia",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            console.log(data)          
        }
    })
}