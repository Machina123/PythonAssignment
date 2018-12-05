const KUPONY_ENDPOINT_BASE = window.location.protocol + "//" + window.location.host + "/coupons"
const KUPONY_ENDPOINTS = {
    mac: KUPONY_ENDPOINT_BASE + "/mac",
    subway: KUPONY_ENDPOINT_BASE + "/subway",
    dagrasso: KUPONY_ENDPOINT_BASE + "/dagrasso"
}


function getKuponyMac() {
    $.ajax({
        url: KUPONY_ENDPOINTS.mac,
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)
			var imgInWeb = document.getElementById("imgMc");
            var imgInWebInd = document.getElementById("olMac");
			var classTxt = '<div class="carousel-caption d-none d-md-block text-right kuponImg">';
			imgInWebInd.innerHTML='';
            for(var j = 0; j < data.length; j++){
                if(j == 0)
                    imgInWebInd.innerHTML += '<li data-target="#carouselExampleIndicatorsMac" data-slide-to="'+j+'" class="active"></li>';
                else 
                    imgInWebInd.innerHTML += '<li data-target="#carouselExampleIndicatorsMac" data-slide-to="'+j+'"></li>';
            }

            for(var i = 0; i < data.length; i++){
                var div = document.createElement("div");
                if(i == 0)
                    div.className = "carousel-item active";
                else
                    div.className = "carousel-item";
                
                div.innerHTML = 
				'<img class="d-block w-75 image mx-auto" src="' +data[i].picture+'" alt="Picture Mc">'+
                classTxt+'<h5>'+data[i].name+'</h5><p>'+data[i].price+'</p></div>';	
				imgInWeb.appendChild(div);
            
			}
            $("#carouselExampleIndicatorsMac").carousel();
        }
    })
}

function getKuponySubway() {
    $.ajax({
        url: KUPONY_ENDPOINTS.subway,
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)
			var imgInWeb = document.getElementById("imgSub");
            var imgInWebInd = document.getElementById("olSub");
			var classTxt = '<div class="carousel-caption d-none d-md-block text-right kuponImg">';
			imgInWebInd.innerHTML='';
			            for(var j = 0; j < data.length; j++){
                if(j == 0)
                    imgInWebInd.innerHTML += '<li data-target="#carouselExampleIndicatorsMac" data-slide-to="'+j+'" class="active"></li>';
                else 
                    imgInWebInd.innerHTML += '<li data-target="#carouselExampleIndicatorsMac" data-slide-to="'+j+'"></li>';
            }

            for(var i = 0; i < data.length; i++){
                var div = document.createElement("div");
                if(i == 0)
                    div.className = "carousel-item active";
                else
                    div.className = "carousel-item";
                
                div.innerHTML = 
				'<img class="d-block w-75 image mx-auto" src="' +data[i].picture+'" alt="Picture Mc">'+
                classTxt+'<h5>'+data[i].name+'</h5></div>';	
				imgInWeb.appendChild(div);
            
			}
            $("#carouselExampleIndicatorsMac").carousel();
        }
    })  
}

function getKuponyDagrasso() {
    $.ajax({
        url: KUPONY_ENDPOINTS.dagrasso,
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)  
			var imgInWeb = document.getElementById("imgDag");
            var imgInWebInd = document.getElementById("olDag");
			var classTxt = '<div class="carousel-caption d-none d-md-block text-right kuponImg">';
			imgInWebInd.innerHTML='';
			            for(var j = 0; j < data.length; j++){
                if(j == 0)
                    imgInWebInd.innerHTML += '<li data-target="#carouselExampleIndicatorsMac" data-slide-to="'+j+'" class="active"></li>';
                else 
                    imgInWebInd.innerHTML += '<li data-target="#carouselExampleIndicatorsMac" data-slide-to="'+j+'"></li>';
            }

            for(var i = 0; i < data.length; i++){
                var div = document.createElement("div");
                if(i == 0)
                    div.className = "carousel-item active";
                else
                    div.className = "carousel-item";
                
                div.innerHTML = 
				'<img class="d-block w-75 image mx-auto" src="' +data[i].picture+'" alt="Picture Mc">'+
                classTxt+'<h5>'+data[i].name+'</h5></div>';	
				imgInWeb.appendChild(div);
            
			}
            $("#carouselExampleIndicatorsMac").carousel();
        }
    })
}