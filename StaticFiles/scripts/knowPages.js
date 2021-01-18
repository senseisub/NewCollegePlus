let isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
$(document).ready(() => {
if(isMobile){
    $("#knowdegree h2").css({"font-size" : "20pt"});
    $("#knowdegree button").css({"font-size" : "20pt"});
    $("#knowcollege h2").css({"font-size" : "20pt"});
    $("#knowcollege button").css({"font-size" : "20pt"});
}
});
$( window ).resize(function() {
    if(($( window ).height()/ $( window ).width()) > 1.5 || isMobile){
    $("#knowdegree h2").css({"font-size" : "20pt"});
    $("#knowdegree button").css({"font-size" : "20pt"});
    $("#knowcollege h2").css({"font-size" : "20pt"});
    $("#knowcollege button").css({"font-size" : "20pt"});
    }
    else{
    $("#knowdegree h2").css({"font-size" : "12pt"});
    $("#knowdegree button").css({"font-size" : "12pt"});
    $("#knowcollege h2").css({"font-size" : "12pt"});
    $("#knowcollege button").css({"font-size" : "12pt"});
    }
});
function onLoad(){
    $("#logout").click(function(){
    
    document.location.href = "/logout";
    });
    $("#logout").hover(function(){
    $("#logout").css("cursor", "pointer");
    });
}

window.onload = onLoad