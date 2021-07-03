const seconds_str = document.querySelector(".seconds").innerHTML;
let points = parseInt(document.querySelector(".points").innerHTML);
const duration = parseInt(document.querySelector(".duration").innerHTML);
if (seconds_str != "") {
    let seconds = parseInt(seconds_str);
    const setClock = () => {
        hours_left = Math.floor(seconds/3600);
        minutes_left = (Math.floor(seconds/60))%60;
        seconds_left = seconds%60;
        document.querySelector(".hours_left").innerHTML = hours_left;
        document.querySelector(".minutes_left").innerHTML = minutes_left;
        document.querySelector(".seconds_left").innerHTML = seconds_left;
    }
    setClock();
    points_available = Math.floor((points * seconds)/(duration * 60));
    document.querySelector(".points").innerHTML = points_available;
    window.setInterval(() => {
        setClock();
        seconds = seconds - 1;
    }, 1000)
}