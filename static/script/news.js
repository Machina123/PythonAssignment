var x = 0;
function getTvn() {
    $.ajax({
        url: "http://localhost:8080/info/tvn",
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
        url: "http://localhost:8080/info/rmf",
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
        url: "http://localhost:8080/info/interia",
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

function prev(){
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

function next(){
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

