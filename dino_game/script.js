var dino = document.getElementById("dino");
var cactus = document.getElementById("cactus");
var msg = document.getElementById("msg");

dino.style.bottom = "0px";
cactus.style.left = "600px";

var gameOver = false;

document.onkeydown = function () {
    if (gameOver) return;

    dino.style.bottom = "100px";

    setTimeout(function () {
        dino.style.bottom = "0px";
    }, 300);
};

setInterval(function () {

    if (gameOver) return;

    var cactusLeft = parseInt(cactus.style.left);
    cactus.style.left = (cactusLeft - 5) + "px";

    if (cactusLeft < -30) {
        cactus.style.left = "600px";
    }

    var dinoBottom = parseInt(dino.style.bottom);

    if (cactusLeft < 90 && cactusLeft > 50 && dinoBottom == 0) {
        gameOver = true;
    }

}, 20);


