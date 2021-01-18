$( window ).resize(function() {
    let isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

    if(($( window ).height()/ $( window ).width()) > 1.5 || isMobile){
      $(".drop").css({"font-size" : "20pt", "padding" : "16px"});
      $(".form_input").css({"font-size" : "28pt"});
      $("#dropbtnsub").css({"font-size" : "1.2vh"});
      $("#submit").css({"font-size" : "1.2vh"});
    }
    else{
        $(".drop").css({"font-size" : "16px", "padding" : "16px"});
        $(".form_input").css({"font-size" : "16px"});
        $("#dropbtnsub").css({"font-size" : "12pt"});
        $("#submit").css({"font-size" : "12pt"});

    }
  });

  $( document ).ready(function() {
    let isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    if(isMobile){
        $(".drop").css({"font-size" : "20pt", "padding" : "16px"});
        $(".form_input").css({"font-size" : "28pt"});
        $("#dropbtnsub").css({"font-size" : "1.2vh"});
        $("#submit").css({"font-size" : "1.2vh"});

    }
});