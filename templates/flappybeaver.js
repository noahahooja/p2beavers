var dam = document.getElementById("dam");
var opening = document.getElementById("opening");
var beaver = document.getElementById("beaver);
var jumping = 0;
var counter = 0;

opening.addEventListener('animationiteration', () => {
    var random = -((Math.random()*300)+150);
    var top = (random*100)+150;
    opening.style.top = -(top) + "px";
    counter++;
});

setInterval(function(){
    var characterTop =
    parseInt(window.getComputedStyle(beaver).getPropertyValue("top"));
    if(jumping==0){
        beaver.style.top = (characterTop+3)+"px";
    }
    var blockLeft = parseInt(window.getComputedStyle(dam).getPropertyValue("left"));
    var holeTop = parseInt(window.getComputedStyle(opening).getPropertyValue("top"));
    var cTop = characterTop-500;
    if(characterTop>480)||((blockLeft<20)&&(blockleft>-50)&&((cTop<holeTop)||(cTop>holeTop+130))){
        alert("Game over. Score: "+counter);
        beaver.style.top = 100px;
        counter=0;
    }
    });

document.addEventListener('keyup', event => {
    if (event.code === 'Space') {
        jumping = 1;
        let jumpCount = 0;
        var jumpInterval = setInterval(function(){
            var characterTop =
            parseInt(window.getComputedStyle(beaver).getPropertyValue("top"));
            if((characterTop>6)&&(counter<15)){
                beaver.style.top = (characterTop-5)+"px";
            }

            if(jumpCount>20){
                clearInterval(jumpInterval);
                jumping=0;
                jumpCount=0;
            }
            jumpCount++;
        })
        }
    });