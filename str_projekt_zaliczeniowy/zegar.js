function czas() {
    var data = new Date(); //tworzymy obiekt typu data
    var godzina = data.getHours(); //pobieramy godzinę
    var minuta = data.getMinutes(); //pobieramy minutę
    var sekunda = data.getSeconds(); //pobieramy sekundy
 
    // przypisanie zera do godziny, minuty i sekundy, czyli np. 05 a nie 5
    if (godzina < 10) {
        godzina = "0" + godzina;
    }
    if (minuta < 10) {
        minuta = "0" + minuta;
    }
    if (sekunda < 10) {
        sekunda = "0" + sekunda;
    }
 
    //wyświetlenie zegarka w divie o id zegar
    document.querySelector("#zegar").innerHTML = godzina + " : " + minuta + " : " + sekunda;
 
    setTimeout(czas, 1000); //samowywołanie się funkcji po 1s
}
window.addEventListener("load", czas); //wywołanie funkcji czas po załadowaniu strony
