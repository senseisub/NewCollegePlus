function onLoad(){
    var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    if (isMobile) {
        $("footer").css({"position": "fixed", "bottom": "0"});
        // $("h1").css({"padding-top", "20%"});
    }
    checkCookie();
    $("#logout").click(function(){
        document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        document.cookie = "password=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        if(isMobile){
          document.location.href = "/mobile/logout";
        }
        else{
          document.location.href = "/logout";
        }
     
      });
      $("#logout").hover(function(){
        $("#logout").css("cursor", "pointer");
      });
}

  
  function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }
  function checkCookie() {
    var user=getCookie("username");
    if (user != "") {
      $("#setter").text(user);
      $("#set1").val(user);
    } else {
      $("#set1").val("log in");
    }
  }
window.onload = onLoad
