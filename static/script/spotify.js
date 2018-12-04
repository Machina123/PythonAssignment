function spotifyInit() {
    $.ajax({
        url: "http://localhost:8080/spotify/refresh_token",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            if(!data.success) {
               document.getElementById("spoti_loggedin").innerHTML = "<i class='fab fa-spotify'></i> Nie zalogowano do Spotify. <a href='./spotify/authcode'>Zaloguj się</a>";
            }
        }
    })
}

function spotifyGetLoggedIn() {

}

function spotifyGetNowPlaying() {
    $.ajax({
        url: "http://localhost:8080/spotify/now_playing",
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            if(data.hasOwnProperty("success") && !data.success) {
                alert("Nie zalogowano do Spotify");
                return;
            }  
            
            console.log(data)

            var spotiTitleElem = document.getElementById("spoti_title")
            var spotiArtistElem = document.getElementById("spoti_artist")
            var spotiAlbumElem = document.getElementById("spoti_albumname")
            var spotiAlbumArtElem = document.getElementById("spoti_album")

            if(data.isPlaying) {
                document.getElementById("btn_spoti_play").innerHTML = "<i class='fas fa-pause'></i>";
            } else {
                document.getElementById("btn_spoti_play").innerHTML = "<i class='fas fa-play'></i>";
            }

            spotiTitleElem.innerText = data.item.name;
            spotiArtistElem.innerText = ""
            if(data.item.artists.length > 1) {
                for(var i = 0; i < data.item.artists.length; i++) {
                    spotiArtistElem.innerText += data.item.artists[i].name
                    if(i < data.item.artists.length - 1) {
                        spotiArtistElem.innerText += ", "
                    }
                }
            } else spotiArtistElem.innerText = data.item.artists[0].name

            spotiAlbumElem.innerText = data.item.album.name

            spotiAlbumArtElem.src = data.item.album.images[0].url
        } 
    })
}
