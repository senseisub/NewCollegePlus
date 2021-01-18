$( window ).resize(function() {
    let isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

    if(($( window ).height()/ $( window ).width()) > 1.5 || isMobile){
      $(".menuElements").css({"font-size" : "32pt", "padding-top" : "2vh", "padding-bottom" : "2vh"});
      $("#navbar").css({"min-height" : "4vh"});
      $("#setter").css({"display" : "none"});
      $("#personIcon").css({"font-size" : "48pt" , "margin-top" : ".2vh"});
      $(".bigTitle").css("font-size", "6vw")

    }
    else{
      $(".menuElements").css({"font-size" : "18pt", "padding-top" : ".5vh", "padding-bottom" : ".5vh"});
      $("#navbar").css({"min-height" : "10vh"});
      $("#navbar").css({"max-height" : "10vh"});
      $("#setter").css({"display" : "block"});
      $("#personIcon").css({"font-size" : "24pt", "margin-top" : "2vh"});
      $(".bigTitle").css("font-size", "6vh")

    }
  });
    let bool = false;
    let boxClick = ()=>{
      $("#check").click();
      console.log("clicked2");
      if(bool){
        $("#menuToggle span").css("background-color", "#cdcdcd")
        bool = !bool;
      }
      else{
        $("#menuToggle span").css("background-color", "#232323")
        bool = !bool;
      }
    };

    let logoClick = (place) => {
        document.location.href= "/home";
      };

$( document ).ready(function() {
    let isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    if(isMobile){
      $(".menuElements").css({"font-size" : "32pt", "padding-top" : "2vh", "padding-bottom" : "2vh"});
      $("#navbar").css({"min-height" : "4vh"});
      $("#setter").css({"display" : "none"});
      $("#personIcon").css({"font-size" : "48pt" , "margin-top" : ".2vh"});
      $(".bigTitle").css("font-size", "6vw")

    }
});

let goToSave = () => {
  document.location.href= "/login_page";
}