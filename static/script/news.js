const NEWS_ENDPOINT_BASE = window.location.protocol + "//" + window.location.host + "/info"
const NEWS_ENDPOINTS = {
    tvn: NEWS_ENDPOINT_BASE + "/tvn",
    rmf: NEWS_ENDPOINT_BASE + "/rmf",
    interia: NEWS_ENDPOINT_BASE + "/interia"
}

var x = 0;
function getTvn() {
    $.ajax({
        url: NEWS_ENDPOINTS.tvn,
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)
            document.getElementById("info").innerHTML = " ";

            var info = document.getElementById("info");
            for(var i = 0; i < 10; i++){
                var news = document.createElement("div");
                news.id = "news" + i;
                var title = document.createElement("h3");
                title.innerHTML = data[i].title;
                var desc = document.createElement("p");
                desc.innerHTML = data[i].desc;
                var link = document.createElement("a");
                link.setAttribute("href",data[i].link);
                link.innerHTML = data[i].link;
                news.appendChild(title);
                news.appendChild(desc);
                news.appendChild(link);
                info.appendChild(news);
            }
         document.getElementById("news0").style.display = "block";
        
        }
    })
}

function getRmf() {
    $.ajax({
        url: NEWS_ENDPOINTS.rmf,
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)   
            document.getElementById("info").innerHTML = " ";

            var info = document.getElementById("info");
            for(var i = 0; i < 10; i++){
                var news = document.createElement("div");
                news.id = "news" + i;
                var title = document.createElement("h3");
                title.innerHTML = data[i].title;
                var desc = document.createElement("p");
                desc.innerHTML = data[i].desc;
                var link = document.createElement("a");
                link.setAttribute("href",data[i].link);
                link.innerHTML = data[i].link;
                news.appendChild(title);
                news.appendChild(desc);
                news.appendChild(link);
                info.appendChild(news);
            }
        document.getElementById("news0").style.display = "block";
        }
    })
}

function getInteria() {
    $.ajax({
        url: NEWS_ENDPOINTS.interia,
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)   
            document.getElementById("info").innerHTML = "";

            var info = document.getElementById("info");
            for(var i = 0; i < 10; i++){
                var news = document.createElement("div");
                news.id = "news" + i;
                var title = document.createElement("h3");
                title.innerHTML = data[i].title;
                var desc = document.createElement("p");
                desc.innerHTML = data[i].desc;
                var link = document.createElement("a");
                link.setAttribute("href",data[i].link);
                link.innerHTML = data[i].link;
                news.appendChild(title);
                news.appendChild(desc);
                news.appendChild(link);
                info.appendChild(news);
            }
        document.getElementById("news0").style.display = "block";
        }
    })
}

function prevNews(){
    if(x == 0){
        document.getElementById("news0").style.display = "none";
        x = 9;
        document.getElementById("news"+x).style.display = "block";
    }
    else{
        document.getElementById("news"+x).style.display = "none";
        x--;
        document.getElementById("news"+x).style.display = "block";
        
    }
    console.log(x)
}

function nextNews(){
    document.getElementById("news0").style.display = "none";
    if(x == 9){
        document.getElementById("news9").style.display = "none";
        x = 0;
        document.getElementById("news"+x).style.display = "block";
    }
    else{
        document.getElementById("news"+x).style.display = "none";
        x++;
        document.getElementById("news"+x).style.display = "block";
    }
}

