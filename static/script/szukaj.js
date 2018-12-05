function search() {
    var searchData = encodeURIComponent(document.getElementById("inputSzukaj").value)
    window.location.href = "http://google.com/search?q=" + searchData;
}

//document.getElementById("szukaj").addEventListener("click", search,false)