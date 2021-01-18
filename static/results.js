$( window ).resize(function() {
    let isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

    if(($( window ).height()/ $( window ).width()) > 1.5 || isMobile){
      $(".recbuttons").css({"font-size" : "1.2vh"});
      $(".urlButton").css({"font-size" : "1.2vh"});
      $(".cfq").css({"font-size" : "1.7vw"});
    }
    else{
        $(".recbuttons").css({"font-size" : "12pt"});
        $(".urlButton").css({"font-size" : "12pt"});
        $(".cfq").css({"font-size" : "2.4vw"});

    }
  });

  $( document ).ready(function() {
    let isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    if(isMobile){
        $(".recbuttons").css({"font-size" : "20pt"});
        $(".urlButton").css({"font-size" : "1.2vh"});
        $(".cfq").css({"font-size" : "1.7vw"});

    }
});