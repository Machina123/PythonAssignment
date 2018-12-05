function getTvn() {
    $.ajax({
        url: "http://127.0.0.1:8080/info/tvn",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)
            document.getElementById("info").innerHTML = " ";

            var info = document.getElementById("info");
            for(var i = 0; i < 15; i++){
                var news = document.createElement("div");
                news.id = "news" + i;
                var title = document.createElement("h3");
                title.id = "title" + i;
                title.innerHTML = data[i].title;
                var desc = document.createElement("p");
                desc.id = "desc" + i;
                desc.innerHTML = data[i].desc;
                var link = document.createElement("a");
                link.setAttribute("href",data[i].link);
                link.innerHTML = data[i].link;
                news.appendChild(title);
                news.appendChild(desc);
                news.appendChild(link);
                info.appendChild(news);
            }
        
        }
    })
}

function getRmf() {
    $.ajax({
        url: "http://127.0.0.1:8080/info/rmf",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)   
            document.getElementById("info").innerHTML = " ";

            var info = document.getElementById("info");
            for(var i = 0; i < 15; i++){
                var news = document.createElement("div");
                news.id = "news" + i;
                var title = document.createElement("h3");
                title.id = "title" + i;
                title.innerHTML = data[i].title;
                var desc = document.createElement("p");
                desc.id = "desc" + i;
                desc.innerHTML = data[i].desc;
                var link = document.createElement("a");
                link.setAttribute("href",data[i].link);
                link.innerHTML = data[i].link;
                news.appendChild(title);
                news.appendChild(desc);
                news.appendChild(link);
                info.appendChild(news);
            }
        }
    })
}

function getInteria() {
    $.ajax({
        url: "http://127.0.0.1:8080/info/interia",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            //console.log(data)   
            document.getElementById("info").innerHTML = "";

            var info = document.getElementById("info");
            for(var i = 0; i < 15; i++){
                var news = document.createElement("div");
                news.id = "news" + i;
                var title = document.createElement("h3");
                title.id = "title" + i;
                title.innerHTML = data[i].title;
                var desc = document.createElement("p");
                desc.id = "desc" + i;
                desc.innerHTML = data[i].desc;
                var link = document.createElement("a");
                link.setAttribute("href",data[i].link);
                link.innerHTML = data[i].link;
                news.appendChild(title);
                news.appendChild(desc);
                news.appendChild(link);
                info.appendChild(news);
            }
        }
    })
}
