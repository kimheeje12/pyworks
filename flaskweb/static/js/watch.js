
var watch = setInterval(myWatch, 1000)

function myWatch(){
    var date = new Date();
    var now = date.toLocaleTimeString(); //년월일은 빼고, 시, 분, 초만 표시
    document.getElementById("demo").innerHTML = now
}