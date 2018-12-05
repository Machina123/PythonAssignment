function initAll() {

    // Funkcje inicjujące wyszukiwanie
    document.getElementById("szukaj").addEventListener("click", search, false);

    // Funkcje inicjujące pogodę
    initWeather()
    getWeather()
    document.getElementById("weather_refresh").addEventListener("click", getWeather, false)

    // Funkcje inicjujące wiadomości
    getTvn()
    document.getElementById("btn_news_tvn").addEventListener("click", getTvn, false);
    document.getElementById("btn_news_rmf").addEventListener("click", getRmf, false);
    document.getElementById("btn_news_interia").addEventListener("click", getInteria, false);
    document.getElementById("news_next").addEventListener("click", nextNews, false);
    document.getElementById("news_prev").addEventListener("click", prevNews, false);

    // Funkcje inicjujące kupony
    getKuponyMac();
    getKuponySubway();
    getKuponyDagrasso();

    // Funkcje inicjujące rozkłady jazdy tramwajów
    getMpkStops()
    document.getElementById("btn_mpk_rozklad").addEventListener("click", getMpkSchedule, false);

    // Funkcje inicjujące Spotify
    spotifyInit();
    document.getElementById("btn_spoti_prev").addEventListener("click", spotifyPrevTrack, false);
    document.getElementById("btn_spoti_play").addEventListener("click", spotifyPlayPause, false);
    document.getElementById("btn_spoti_next").addEventListener("click", spotifyNextTrack, false);

}

window.addEventListener("DOMContentLoaded", initAll, false);