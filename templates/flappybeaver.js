var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

class Beaver {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.w = 40;
    this.h = 40;
    this.ySpeed = 3;
  }
  show() {
    ctx.fillStyle = "yellow";
    ctx.fillRect(this.x, this.y, this.w, this.h);
  }
  update() {
    this.y += this.ySpeed;
    this.ySpeed += gravity;
  }
}

var p;

var gravity = 0.1;

window.onload = function () {
  start();
  setInterval(update, 10);
};

function start() {
  p = new Beaver(0, 400);
}

function update() {
  canvas.width = canvas.width;
  //Beaver
  p.show();
  p.update();
}