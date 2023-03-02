	//Skript pro časovač 
    // Nastavení datumu pro časovač (1. května 2023)
    
    var countDownDate = new Date("May 1, 2023 00:00:00").getTime();

    // Aktualizace časovače každou sekundu
    var x = setInterval(function () {

        // Výpočet zbývajícího času
        var now = new Date().getTime();
        var distance = countDownDate - now;

        // Výpočet zbývajících dní, hodin, minut a sekund
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Zobrazení zbývajícího času v HTML
        document.getElementById("days").innerHTML = days;
        document.getElementById("hours").innerHTML = hours;
        document.getElementById("minutes").innerHTML = minutes;
        document.getElementById("seconds").innerHTML = seconds;

        // Pokud je časovač ukončen, zobrazit text
        if (distance < 0) {
            clearInterval(countdownInterval);
            countdownText.textContent = "Maturita začíná!";
        }
    });