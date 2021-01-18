
async function calc(){
  let ques1 = $("#ques1").val();
  let ques2 = $("#ques2").val();
  let ques3 = $("#ques3").val();
  let ques4 = $("#ques4").val();
  let ques5 = $("#ques5").val();
  let ques6 = $("#ques6").val();
  let ques7 = $("#ques7").val();
  let ques8 = $("#ques8").val();
  let ques9 = $("#ques9").val();
  let ques10 = $("#ques10").val();

  // let url = "https://collegeplus.us/returnDeviceSelections?ques1="+ques1+"&ques2="+ques2+"&ques3="+ques3+"&ques4="+ques4+"&ques5="+ques5+"&ques6="+ques6+"&ques7=" +ques7 + "&ques8=" + ques8 + "&ques9=" + ques9 + "&ques10=" + ques10;
  // await $.get(url, null, handleresponse);
  
  let stringAnswer = ques1 + " " + ques2 + " " + ques3 + " " + ques4 + " " + ques5 + " " + ques6 + " " + ques7 + " " + ques8 + " " + ques9 + " " + ques10;

  $("#answers").val(stringAnswer);
  finished = true;
  if(finished)
    $("#myform").submit();
  
}

function arrayToString(array1, array2, array3){
  let returningString = "";
  for(let i =0; i < array1.length; i++){
      returningString += array1[i] + ",";
  }
  $("#devices").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array2.length; i++){
      returningString += array2[i] + ",";
  }
  $("#urls").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array3.length; i++){
      returningString += array3[i] + ",";
  }
  $("#images").val(returningString.substring(0, returningString.length -1));
}

function onLoad(){
  var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    if (isMobile) {
      $("#college").click(function(){
        document.location.href ="/mobile/home";
    });
    }
  if(valley<1){
      $("#submit").click(calc);
    }
    else{
      window.location.href ="/devicepicker";
    }
    checkCookie();
    $("#logout").click(function(){
      document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
      document.cookie = "password=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
      document.location.href = "/logout";
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
