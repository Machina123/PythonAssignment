function getKuponyMac() {
    $.ajax({
        url: "http://localhost:8080/coupons/mac",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            console.log(data)
           /* var imgInWeb = document.getElementById("imgMc");
            var imgInWebInd = document.getElementById("olMac");
            for(var j = 0; j < data.lenght; j++){
                if(j == 0)
                    imgInWebInd.innerHTML = '<li data-target="#carouselExampleIndicatorsMac" data-slide-to="'+j+'" class="active"></li>';
                else 
                    imgInWebInd.innerHTML = '<li data-target="#carouselExampleIndicatorsMac" data-slide-to="'+j+'"></li>';
            }

            for(var i = 0; i < data.lenght; i++){
                var div = document.createElement("div");
                if(i == 0)
                    div.className = "carousel-item active";
                else
                    div.className = "carousel-item";
                
                div.innerHTML = '<img src="' +data[i].picture+'" alt="Picture Mc">';
                imgInWeb.appendChild(div);
            }
            $("#carouselExampleIndicatorsMac").carousel();*/
            //for(var i = 0; i < data.name.length; i++){
             //   console.log(data.name[i])
           // }
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

function getKuponyDagrasso() {
    $.ajax({
        url: "http://localhost:8080/coupons/dagrasso",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            console.log(data)          
        }
    })
}