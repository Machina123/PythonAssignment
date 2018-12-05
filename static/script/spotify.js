const SPOTIFY_ENDPOINT_BASE = window.location.protocol + "//" + window.location.host + "/spotify"
const SPOTIFY_ENDPOINTS = {
    token: SPOTIFY_ENDPOINT_BASE + "/token",
    refreshToken: SPOTIFY_ENDPOINT_BASE + "/refresh_token",
    user: SPOTIFY_ENDPOINT_BASE + "/user",
    nowPlaying: SPOTIFY_ENDPOINT_BASE + "/now_playing",
    pause: SPOTIFY_ENDPOINT_BASE + "/pause",
    play: SPOTIFY_ENDPOINT_BASE + "/play",
    next: SPOTIFY_ENDPOINT_BASE + "/next",
    prev: SPOTIFY_ENDPOINT_BASE + "/prev"
}

function spotifyRefreshToken() {
    $.ajax({
        url: SPOTIFY_ENDPOINTS.refreshToken,
        type: 'GET',
        dataType: 'json',
        success: function(data, status, xhr) {
            if(!data.success) {
               document.getElementById("spoti_loggedin").innerHTML = "<i class='fab fa-spotify'></i> Nie zalogowano do Spotify. <a href='./spotify/authcode'>Zaloguj się</a>";
            }
        }, 
        error: function(xhr, status, error) {
            document.getElementById("spoti_loggedin").innerHTML = "<i class='fab fa-spotify'></i> Nie zalogowano do Spotify. <a href='./spotify/authcode'>Zaloguj się</a>";
        }
    })
}

function spotifyGetLoggedIn() {
    $.ajax({
        url: SPOTIFY_ENDPOINTS.user,
        type: "GET",
        dataType: "json",
        success: function(data, status, xhr) {
            if(data.id != null) {
                document.getElementById("spoti_loggedin").innerHTML = "<i class='fab fa-spotify'></i> Zalogowano jako <a href='"+ data.external_urls.spotify +"' target='_blank'>"+ data.display_name +"</a>";
            }
        }
    })
}

function spotifyGetToken() {
    try {
        $.ajax({
            url: SPOTIFY_ENDPOINTS.token,
            type: "GET",
            dataType: "json",
            success: function(data, status, xhr) {
                if(data.hasOwnProperty("error")) {
                    document.getElementById("spoti_loggedin").innerHTML = "<i class='fab fa-spotify'></i> Nie zalogowano do Spotify. <a href='./spotify/authcode'>Zaloguj się</a>";
                }
            },
            error: function(xhr, status, error) {
                console.error(status, error);
            }
        })
    } catch(err) {
        console.error(err);
        document.getElementById("spoti_loggedin").innerHTML = "<i class='fab fa-spotify'></i> Nie zalogowano do Spotify. <a href='./spotify/authcode'>Zaloguj się</a>";
    }
}

function spotifyGetNowPlaying() {
    $.ajax({
        url: SPOTIFY_ENDPOINTS.nowPlaying,
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
        },
        error: function(xhr, status, error) {
            document.getElementById("spoti_loggedin").innerHTML = "<i class='fab fa-spotify'></i> Nie zalogowano do Spotify. <a href='./spotify/authcode'>Zaloguj się</a>";
        }
    })
}
