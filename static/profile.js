var fileReader = new FileReader();
let nameBool = false;
var filterType = /^(?:image\/bmp|image\/cis\-cod|image\/gif|image\/ief|image\/jpeg|image\/jpeg|image\/jpeg|image\/pipeg|image\/png|image\/svg\+xml|image\/tiff|image\/x\-cmu\-raster|image\/x\-cmx|image\/x\-icon|image\/x\-portable\-anymap|image\/x\-portable\-bitmap|image\/x\-portable\-graymap|image\/x\-portable\-pixmap|image\/x\-rgb|image\/x\-xbitmap|image\/x\-xpixmap|image\/x\-xwindowdump)$/i;
let collegescities = [];
let collegestates = [];
let isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

let currentValue = 0;

async function tempcontrol(response){
  var json = response; 
  var celsius = json["main"]["temp"] - 273;
  var fahrenheit = (celsius*(9/5)) + 32;
  
  // for(let i = 0; i < collegestates.length; i++){
    // if(){
      await $("#collegeTemp"+(currentValue+1)).text(fahrenheit.toPrecision(2)+ "°");
    // }
    await $("#collegeWeather"+(currentValue+1)).text(json["weather"][0]["description"]);
  // }

}
async function temp(){
  for(var i = 0; i < collegestates.length; i++){
        currentValue = i;
        let url2 = "https://api.openweathermap.org/data/2.5/weather?q="+collegecities[i]+",USA&appid=01e2ab091c2e3a0ab1eaca9b7e15f159";
        await $.get(url2, null, tempcontrol);

  }
}
function stripExtras(str){
  if(str.length == 0){
    return [];
  }
  let tempString = str.substring(1, str.length-1).split(", ");

  for(let i = 0 ; i < tempString.length; i++){
    tempString[i] = tempString[i].substring(1, tempString[i].length-1);
  }
  return tempString;
}



function onLoad(){
  let profileImage = $("#imageUrl").text();
  let infoJSON = $("#totalInfo").text();
  infoJSON = JSON.parse(infoJSON);
  let colleges = infoJSON["main"]["colleges"];
  collegestates = infoJSON["main"]["collegeStates"];
  collegecities = infoJSON["main"]["collegeCities"];
  let collegeTemperatures = infoJSON["main"]["collegeTemperatures"];
  let collegeWeather = infoJSON["main"]["collegeWeather"];
  let collegeLinks = infoJSON["main"]["collegeLinks"];
  let majors = infoJSON["main"]["majors"];
  let devices = infoJSON["main"]["devices"];


  $("#nameSwitch").click(() => {nameBool = nameBool ? false : true; console.log(nameBool);
    if(nameBool){
      $("#nameChangeDiv").css({"margin-bottom": "10%;", "display" : "block", "margin-bottom" : "10%"});
  }
  else{
      $("#nameChangeDiv").css({"display": "none"});
  }
  });
    if(profileImage.indexOf("{imageUrl}") == -1){
        $("#person").css("display", "none");
        $("#personcenter").append("<div style = 'border-radius: 50%; margin-bottom: 5%; margin-top : 1%;'> <div style = 'max-width: 175px; max-height: 175px; width: 175px; height: 175px; overflow: hidden; border-radius: 50%; margin-left : auto; margin-right : auto;'><img style = 'display : inline; margin : 0 auto; height : 100%; width : auto;'  src = '"+profileImage+"' /></div><br><span class='material-icons' id = 'newImage1' style = 'color : black; cursor : pointer'>create</span></div>");
    }
    else{
      $("#personcenter").append("<i id='person' class='material-icons'>person</i><span class='material-icons' id = 'newImage2' style = 'color : black; cursor : pointer'>create</span>");

    }
    $("#newImage1").click(function(){window.document.location = "/changeProfilePicture"});
  $("#newImage2").click(function(){window.document.location = "/changeProfilePicture"});
    for(var i = 0; i < colleges.length; i++){

        $("#collegeList").append(renderHTML(colleges[i], collegecities[i], collegestates[i], collegeWeather[i], collegeTemperatures[i], collegeLinks[i], (i+1)));
    }
    for(var i = 0; i < majors.length; i++){
      $("#majorList").append(renderHTML2(majors[i], (i+1)));
    }
    for(var i = 0; i < devices.length; i++){
      $("#deviceList").append(renderHTML3(devices[i], (i+1)));
    }
    $("#logout").click(function(){
     
      document.location.href = "/logout";
    });
    $("#logout").hover(function(){
      $("#logout").css("cursor", "pointer");
    });
    if(isMobile){
      $(".infoRow2").css({"flex-direction" : "column", "align-items" : "center"});
      $(".infoRow2 p").css({"font-size" : "20pt"});
      $(".infoRow2 h2").css({"font-size" : "28pt"});
      $(".infoRow2 a").css({"font-size" : "20pt"});
      $(".infoRow div").css({"width" : "100%"});
      $("#listingsToggle").css({"font-size" : "28pt"})

    }
    temp();
}

function renderHTML(college, collegecity, collegestate, collegeweather, collegetemp, collegelink, num){
  let tempstring = "<div class = 'profilebigdiv' id = 'college"+num+"'>" +
        "<div style='border-bottom: 2px solid black; width: max-content; margin-left: auto; margin-right: auto; font-size: 14pt;'>" +
          "<a href = 'https://"+collegelink+"'> "+college+" </a>" +
        "</div>" +
        "<div>"+
        collegecity+ ", "+collegestate+" <i class='material-icons'>" +
            "wb_sunny" +
            "</i> <ml id = 'collegeTemp"+num+"'>"+collegetemp+"°</ml> <ml id = 'collegeWeather"+num+"'>"+collegeweather+"</ml>"+
        "</div>"+
     "</div>";
  return tempstring;
}

function renderHTML2(major, num){
  let tempstring = "<div class = 'profilebigdiv' style='font-size: 14pt;''><p>" +major+"</p></div>";
  return tempstring;
}

function renderHTML3(device, num){
  let tempstring = "<div class = 'profilebigdiv' ><p>" +device+"</p></div>";
  return tempstring;
}
window.onload = onLoad;
$( window ).resize(function() {
  if(($( window ).height()/ $( window ).width()) > 1.5 || isMobile){
    $(".infoRow2").css({"flex-direction" : "column", "align-items" : "center"});
      $(".infoRow2 p").css({"font-size" : "20pt"});
      $(".infoRow2 h2").css({"font-size" : "28pt"});
      $(".infoRow2 a").css({"font-size" : "20pt"});
      $("#listingsToggle").css({"font-size" : "28pt"})

  }
  else{
    $(".infoRow2").css({"flex-direction" : "row", "align-items" : "normal"});
    $(".infoRow2 p").css({"font-size" : "12pt"});
    $(".infoRow2 h2").css({"font-size" : "16pt"});
    $(".infoRow2 a").css({"font-size" : "12pt"});
    $("#listingsToggle").css({"font-size" : "16pt"})

  }
});