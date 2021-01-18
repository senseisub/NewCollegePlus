// var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
// if (isMobile) {
//   document.location.href ="/mobile/";
// }

var arr2 = [];
var useract = 0;
var usersat = 0;
var userState = "";
var userCity= "";
let finished = false;
let superList= ["", "", "", "","","","","",""];
let index = 1;
let collegelinks = ["","","","","","","","",""];
let collegeprices = ["","","","","","","","",""];
let collegetemps = ["","","","","","","","",""];
let collegestates = ["","","","","","","","",""];
let collegecities = ["","","","","","","","",""];
let collegeweathers = ["","","","","","","","",""];
let collegepricecalculators = ["","","","","","","","",""];
let collegeBlacks = ["","","","","","","","",""];
let collegeWhites = ["","","","","","","","",""];
let collegeAsians = ["","","","","","","","",""];
let collegeHispanics = ["","","","","","","","",""];
let collegeACTS = ["","","","","","","","",""];
let collegeReadingSAT = ["","","","","","","","",""];
let collegeMathSAT = ["","","","","","","","",""];
let collegeNicheLinks = ["","","","","","","","",""];
let collegeNames = ["","","","","","","","",""];
let collegeTemp = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
let globalState = 0;
let ctxArray = ['#myChart', '#myChart2', '#myChart3', '#myChart4'];
let collegeObjs = [];
let allColleges = "";
class College{
  name;
  weather;
  city;
  state;
  price;
  link;
  blackPop;
  whitePop;
  asianPop;
  hispanicPop;
  ACTscore;
  SATMathscore;
  SATReadingscore;
  nicheLink;
  priceCalcURL;
  temp;

  constructor(collegeName){
    this.name = collegeName;
  }
}

function onLoad(){
  checkCookie();
  $("#logout").click(function(){
    document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.cookie = "password=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.location.href = "/logout";
  });
  $("#logout").hover(function(){
    $("#logout").css("cursor", "pointer");
  });
  try{
    $("#dropbtnsub").click(onButtonClick);

    $("#errorthrower").append("");
  }
  catch(err){
    $("#errorthrower").append("error");
  }
  var smallArr = [5, 6, 7, 8];
  let stateArr = [$("#collegestate2").text()];
  if($("#dummy").length != 0){
    var ctx = $('#myChart');
    var ctx2 = $("#myChart2");
    var ctx3 = $("#myChart3");
    var ctx4 = $("#myChart4");

    collegeNames = $("#colleges").text().split(",");
    collegelinks = $("#collegeLinks").text().split(",");
    collegetemps = $("#collegeTemperature").text().split(",");
    collegeweathers = $("#collegeWeather").text().split(",");
    collegeACTS = $("#collegeACTS").text().split(",");
    collegeReadingSAT = $("#collegeSATReading").text().split(",");
    collegeMathSAT = $("#collegeSATMath").text().split(",");
    collegeprices = $("#collegePrices").text().split(",");
    collegepricecalculators = $("#collegePriceCalculators").text().split(",");
    collegeNicheLinks = $("#collegeNiche").text().split(",");
    collegeBlacks = $("#blackPop").text().split(",");
    collegeWhites = $("#whitePop").text().split(",");
    collegeAsians = $("#asianPop").text().split(",");
    collegeHispanics = $("#hispanicPop").text().split(",");
    collegestates = $("#collegeStates").text().split(",");

  
    var tempInt = 2;
    $("#recs").append("<h1 style = 'font-size: 32pt;color:#000000'>"+collegestates[0] +"</h1>");
    for(var i = 0; i < collegeNames.length; i++){
      if(i != 0){
        if(collegestates[i] != collegestates[i-1]){
          $("#recs").append("<h1 style = 'font-size: 32pt;color:#000000'>"+collegestates[i] +"</h1>");
          stateArr.push(collegestates[i-1]);
        }
        
      }
      if($("#colleges").text() != undefined && $("#colleges").text().length != 0 ){
        let tempString = makeHTML(collegelinks[i], collegeNames[i], collegeprices[i], collegepricecalculators[i], collegeACTS[i], collegeReadingSAT[i], collegeMathSAT[i], collegeNicheLinks[i], i*4+1, i*4+2, i*4+3, i*4+4, i+1, i+1);
        $("#recs").append(tempString);
            let race = ["#black"+i, "#white"+i, "#asian"+i, "#hispanic"+i];
            let stringName = ["Black Population", "White Population", "Asian Population", "Hispanic Population"];
            let length = i*4+1;
            let place = 0;
            for(var j = length; j < length+4; j++){
              ctxArray.push('#myChart'+j.toString());
              if(place == 0)
                makeGraphs(ctxArray[ctxArray.length - 1], collegeBlacks[i], stringName[place], i);
              if(place == 1)
                makeGraphs(ctxArray[ctxArray.length - 1], collegeWhites[i], stringName[place], i);
              if(place == 2)
                makeGraphs(ctxArray[ctxArray.length - 1], collegeAsians[i], stringName[place], i);
              if(place == 3)
                makeGraphs(ctxArray[ctxArray.length - 1], collegeHispanics[i], stringName[place], i);
              place++;
            }
            tempInt++;
            smallArr[0] = smallArr[0]+4;
            smallArr[1] = smallArr[1]+4;
            smallArr[2] = smallArr[2]+4;
            smallArr[3] = smallArr[3]+4;
            collegeACTS[i-1] = $("#act"+i).text();
            var sum= parseInt($("#getscore"+i+"1").text()) + parseInt($("#getcollegeact"+i).text());
            useract = parseInt($("#getscore"+i+"1").text());
            act1 = parseInt($("#getcollegeact"+i).text());
            if(isNaN(parseInt(collegeACTS[i]))){
              $(".scoresfor"+(i+1)).css("display", "none");
              $("#bigdiv"+(i+1)).css("width", "80%");
              $("#bigdiv"+ (i+1)).css("margin-left", "auto");
              $("#bigdiv"+(i+1)).css("margin-right", "auto");
              $("#yesornoact"+(i+1)).text("Oops we have no info on this school's ACT scores!");
            }
            else{
              if(useract > act1){
                $("#yesornoact"+(i+1)).text("You score better than the average student at this school!");
                $("#actimage"+(i+1)).attr("src","https://collegeplus2.wn.r.appspot.com/StaticFiles/pictures/greenlight.png");
                $("#actimage"+(i+1)).css("max-width", "50%");
              }
              else if(useract < act1){
                $("#yesornoact"+(i+1)).text("You didn't score better than the average student at this school!");
                $("#actimage"+(i+1)).attr("src","https://collegeplus2.wn.r.appspot.com/StaticFiles/pictures/redlight.png");
                $("#actimage"+(i+1)).css("max-width", "48%");
              }
              else{
                $("#yesornoact"+(i+1)).text("You score about the same to the average student at this school!");
                $("#actimage"+(i+1)).attr("src","https://collegeplus2.wn.r.appspot.com/StaticFiles/pictures/yellowlight.png");
                $("#actimage"+(i+1)).css("max-width", "48%");
              }
            }
            var satcumulative1 = parseInt(collegeReadingSAT[i])+parseInt(collegeMathSAT[i]);
            usersat = parseInt($("#getscore"+(i+1)+"2").text());
            if(isNaN(parseInt(satcumulative1))){
              $(".scoresfor"+(i+1)).css("display", "none");
              $("#bigdiv"+(i+1)).css("width", "80%");
              $("#bigdiv"+(i+1)).css("margin-left", "auto");
              $("#bigdiv"+(i+1)).css("margin-right", "auto");
              $("#yesornosat"+(i+1)).text("Oops we have no info on this school's SAT scores!");
            }
            else{
              if(usersat > satcumulative1){
                $("#yesornosat"+(i+1)).text("You score better than the average student at this school!");
                $("#satimage"+(i+1)).attr("src","https://collegeplus2.wn.r.appspot.com/StaticFiles/pictures/greenlight.png");
                $("#satimage"+(i+1)).css("max-width", "50%");
              }
              else if(usersat < satcumulative1){
                $("#yesornosat"+(i+1)).text("You didn't score better than the average student at this school!");
                $("#satimage"+(i+1)).attr("src","https://collegeplus2.wn.r.appspot.com/StaticFiles/pictures/redlight.png");
                $("#satimage"+(i+1)).css("max-width", "48%");
              }
              else{
                $("#yesornosat"+(i+1)).text("You score about the same to the average student at this school!");
                $("#satimage"+(i+1)).attr("src","https://collegeplus2.wn.r.appspot.com/StaticFiles/pictures/yellowlight.png");
                $("#satimage"+(i+1)).css("max-width", "48%");
              }
            }
      }

  
    }

  }
  else{
    
  }
  $("#homebutt1").click(function(){
    document.location.href  = "/knowdegree";
  });
  $("#homebutt2").click(function(){
    document.location.href  = "/knowcollege";
  });
  $("#homebutt3").click(function(){
    document.location.href  = "/gpaCalculator";
  });

  $("#backy").click(function(){
    window.history.back();
  });

  $("#morecolleges").click(function(){
  
    $("#morecollegestext").css("display", "block");

  });

  $('option').mousedown(function(e) {
    e.preventDefault();
    $(this).prop('selected', !$(this).prop('selected'));
    return false;
  });
  var last_valid_selection = null;
 
  $("#states").click(() => {
    if($("#states option:selected").length <= 3) {
    }
    else{
      $("#states").val($("#states").val().pop());

    }
});

}


function makeHTML(collegeLink, collegeName, collegePrice, priceCalculator, collegeACT, collegeReading, collegeMath, LinkOfCollege, firstGraph, secondGraph, thirdGraph, fourthGraph, num, header){
  tempString =       "<div style='margin-bottom: 5%;'>" +
  "<a class = 'c' href='https://www.niche.com/colleges/"+collegeLink+"' style='color:#ff6347; margin-bottom: 5%;'> "+header+". "+collegeName+"</a>" + 
  "</div>" +
  "<div style='margin-bottom: 5%; text-align: center;'>" +
    "<p style='color: black; font-size: 18pt;'>" +
      "Average cost of attendence for your household income:" +
    "</p>" +
    "<p style='color: black; margin-top: 0%; font-size: 28pt; font-weight: 700;'>" +
      "$" + collegePrice + "" +
    "</p>" +
    "<form action='https://"+priceCalculator+"' >" +
      "<input type='submit' value='Check out " + collegeName + "s Price Calculator' class = 'collegewebsitebutton'  />" +
    "</form>" +
  "</div>" +
  "<div style='display: flex; flex-direction: row;''>"+
    "<div style='width: 20%;' class='scoresfor"+num+"'>" + 
        "<p class='describer'>"+
          "Average ACT score:" +
        "</p>" +
        "<p id='getcollegeact"+num+"' class='para'>" +
          "" + collegeACT + "" +
        "</p>" +
    "</div style='width: 33%;'>" +
    "<div style='width: 20%;' class='scoresfor"+num+"'>"+
        "<p class='describer'>"+
          "Average SAT Reading score:" +
        "</p>" +
        "<p id='satreading"+num+"' class='para'>" +
          "" + collegeReading + "" +
        "</p>" +
        "<p class='describer'>" +
          "Average SAT Math score:" +
        "</p>" +
        "<p id='satmath"+num+"' class='para'>" +
          "" + collegeMath + "" +
        "</p>" +
    "</div style='width: 33%;'>" +
    "<div>"+

    "</div>" +
    "<div style='width: 60%;' style='display: flex; flex-direction: column;' id='bigdiv3'>" +
      "<div style='display: flex; flex-direction: row;'>" +
        "<div style='width: 50%;'>" +
          "<img src='https://collegeplus2.wn.r.appspot.com/StaticFiles/pictures/greenlight.png' style='max-width: 50%;' id='actimage3"+num+"'>" +
          "<p id='yesornoact"+num+"' class='columnitems'>" +

          "</p id='yesorno2'>" +
        "</div>" +
        "<div style='width: 50%;'>" +
          "<img src='https://collegeplus2.wn.r.appspot.com/StaticFiles/pictures/greenlight.png' style='max-width: 50%;' id='satimage"+num+"'>" +
          "<p id='yesornosat"+num+"' class='columnitems'>" +

          "</p id='yesorno2'>" +
        "</div>" +
      "</div>" +
      "<div style='display: flex; flex-direction: row;'>" +
        "<div style='width: 50%;'>" +
          "<div style='width: 75%; margin-left: auto; margin-right: auto;'>" +
            "<p id = 'getscore31' class='para'>" +
              $('#getscore11').text() +
            "</p>" +
          "</div>" +
          
        "</div>" +
        "<div style='width: 50%;'>" +
          "<div style='width: 75%; margin-left: auto; margin-right: auto;'>" +
            "<p id = 'getscore32' class='para'>" +
            $('#getscore12').text() +
            "</p>" +
          "</div>" +
          
        "</div>" +

      "</div style='width: 33%;'>" +
    "</div>" +

  "</div>" +
  "<div style = 'display: flex; flex-direction: column; width: 100%; margin-bottom: 5%; margin-top: 5%;'>" +
    "<div style='width: 100%; display: flex; flex-direction: row; height: fit-content;'>" +
      "<div style= 'width: 50%; height: 22vh'>"+
        "<canvas id=myChart" + firstGraph + " width='width: 75%'' height='400'  style='width: 75%; max-width: 60%; max-height: 50vh; margin-left: auto; margin-right: auto;''></canvas>" +
        "<h5 id = 'black"+num+"text' style = 'margin-top: -32%; margin-left: 2%; font-size: 3vw; color : black'>20%</h5>" +
      "</div>" +
      "<div style= 'width: 50%; height: 22vh'>" +
        "<canvas id=myChart" + secondGraph + " width='width: 75%' height='400'  style='width: 75%; max-width: 60%; max-height: 50vh; margin-left: auto; margin-right: auto;'></canvas>"+
        "<h5 id = 'white"+num+"text' style = 'margin-top: -32%; margin-left: 2%; font-size: 3vw; color : black'>20%</h5>"+
      "</div>" +
    "</div>" +
    "<div style= 'width: 100%; display: flex; flex-direction: row;''>"+
      "<div style= 'width: 50%; height: 22vh'>"+
        "<canvas id=myChart" + thirdGraph + " width='width: 75%' height='400'  style='width: 75%; max-width: 60%; max-height: 50vh; margin-left: auto; margin-right: auto;'></canvas>"+
        "<h5 id = 'asian"+num+"text' style = 'margin-top: -32%; margin-left: 2%; font-size: 3vw; color : black'>20%</h5>" +
      "</div>"+
      "<div style= 'width: 50%; height: 22vh'>"+
        "<canvas id=myChart" + fourthGraph + " width='width: 75%' height='400'  style='width: 75%; max-width: 60%; max-height: 50vh; margin-left: auto; margin-right: auto;'></canvas>" +
        "<h5 id = 'hispanic"+num+"text' style = 'margin-top: -32%; margin-left: 2%; font-size: 3vw; color : black'>20%</h5>" +
      "</div>" +
    "</div>" +
  "</div>" +
  "<div style = 'width: 100%; margin-right: auto; margin-left: auto; display: flex; flex-direction: column; margin-bottom: 5%; text-align: center;'>"+
    "<div style='width: 100%; text-align: center; margin-right: auto; margin-left: auto;'>" +
      "<form action='https://"+LinkOfCollege+"' style='width: 100%;'>" +
        "<input type='submit' value='Go to " + collegeName + "\'s website' class = 'collegewebsitebutton' style='background-color: tomato;"+
        "padding: 16px;" +
        "font-size: 16pt;" +
        "cursor: pointer;" +
        "border-radius: 10px;" +
        "opacity: 1;" +
        "border: none;'/>" +
      "</form>" +
    "</div style='width: 50%;'>" +
    "<div style='width: 100%; margin-right: auto; margin-left: auto;'>"+
      "<form action='"+LinkOfCollege+"'>"+
        "<input type='submit' value='More Info on " + collegeName + "' class = 'collegewebsitebutton' style='background-color: tomato;"+
        "padding: 16px;" +
        "font-size: 16pt;" +
        "cursor: pointer;" +
        "border-radius: 10px;" +
        "opacity: 1;" +
        "border: none;'/>"+
      "</form>"+
    "</div style='width: 50%;'>"+
  "</div>"
  return tempString;
  tempString = "<div style='margin-bottom: 5%;'>" +
  "<a class = 'c' href='https://www.niche.com/colleges/" + collegeLink + " style='color:#ff6347; margin-bottom: 5%;'> "+header+". " + collegeName + "</a>"+
"</div>"+
"<div style='margin-bottom: 5%; text-align: center;'>"+
  "<p style='color: black; font-size: 18pt;'>"+
    "Average cost of attendence for your household income:"+
  "</p>"+
  "<p style='color: black; margin-top: 0%; font-size: 28pt; font-weight: 700;'>"+
    "$" + collegePrice +
  "</p>" +
  "<form action='https://" + priceCalculator + "' >"+
    "<input type='submit' value='Check out " + collegeName + "'s Price Calculator class = 'collegewebsitebutton' />" +
  "</form>"+
"</div>"+
"<div style='display: flex; flex-direction: row;'>" +
  "<div style='width: 20%;' class='scoresfor"+num+"'>" +
      "<p class='describer'>" +
        "Average ACT score:" +
      "</p>" +
      "<p id='getcollegeact"+num+"' class='para'>"+
        "" + collegeACT + "" +
      "</p>"+
  "</div style='width: 33%;'>" +
  "<div style='width: 20%;' class='scoresfor"+num+"'>" +
      "<p class='describer'>" +
        "Average SAT Reading score:" +
      "</p>"+
      "<p id='satreading"+num+ "' class='para'>" +
        "" + collegeReading + "" +
      "</p>"+
      "<p class='describer'>"+
        "Average SAT Math score:"+
      "</p>" +
      "<p id='satmath"+num+"' class='para'>" +
        "" + collegeMath + ""+
      "</p>" +
  "</div style='width: 33%;'>" +
  "<div>" +
  "</div>" + 
  "<div style='width: 60%;' style='display: flex; flex-direction: column;' id='bigdiv'"+num+">" +
    "<div style='display: flex; flex-direction: row;'>" +
      "<div style='width: 50%;'>" +
        "<img src='StaticFiles//pictures/greenlight.png' style='max-width: 50%;' id='actimage3'>" +
        "<p id='yesornoact3' class='columnitems'>" + 

        "</p id='yesorno2'>" + 
      "</div>" +
      "<div style='width: 50%;'>" +
        "<img src='StaticFiles//pictures/greenlight.png' style='max-width: 50%;' id='satimage3'>" +
        "<p id='yesornosat3' class='columnitems'> " +

        "</p id='yesorno2'>" +
      "</div>" +
    "</div>" +
    "<div style='display: flex; flex-direction: row;'>" +
      "<div style='width: 50%;'>" +
        "<p id = 'getscore31' class='para'>" +
          $("#getscore11").text()+
        "</p>" +
      "</div>" +
      "<div style='width: 50%;'>" +
        "<p id = 'getscore32' class='para'>" +
        $("#getscore12").text() +
        "</p>" +
      "</div>" +

    "</div style='width: 33%;'>"+
  "</div>"+

"</div>"+
"<div style = 'display: flex; flex-direction: row; width: 100vw; margin-bottom: 5%; margin-top: 5%;'>"+
  "<div style= 'width: 25%; '>"+
    "<canvas id='myChart"+ firstGraph +"' width='width: 75%' height='400'  style='width: 75%; max-width: 75%; max-height: 50vh; margin-left: auto; margin-right: auto;'></canvas>" +
    "<h5 id = 'black"+num+"text' style = 'margin-top: -47%; margin-left: 2%; font-size: 3vw; color : black'>20%</h5>"+
  "</div>"+
  "<div style= 'width: 25%''>"+
    "<canvas id='myChart"+ secondGraph +"' width='width: 75%' height='400'  style='width: 75%; max-width: 75%; max-height: 50vh; margin-left: auto; margin-right: auto;'></canvas>"+
    "<h5 id = 'white"+num+"text' style = 'margin-top: -47%; margin-left: 2%; font-size: 3vw; color : black'>20%</h5>"+
  "</div>"+
  "<div style= 'width: 25%'>"+
    "<canvas id='myChart"+ thirdGraph +"' width='width: 75%' height='400'  style='width: 75%; max-width: 75%; max-height: 50vh; margin-left: auto; margin-right: auto;'></canvas>"+
    "<h5 id = 'asian"+num+"text' style = 'margin-top: -47%; margin-left: 2%; font-size: 3vw; color : black'>20%</h5>"+
  "</div>"+
  "<div style= 'width: 25%'>"+
    "<canvas id='myChart"+ fourthGraph +"' width='width: 75%' height='400'  style='width: 75%; max-width: 75%; max-height: 50vh; margin-left: auto; margin-right: auto;'></canvas>"+
    "<h5 id = 'hispanic"+num+"text' style = 'margin-top: -47%; margin-left: 2%; font-size: 3vw; color : black'>20%</h5>"+
  "</div>"+
"</div>"+
"<div style = 'width: 80%; margin-right: auto; margin-left: auto; display: flex; flex-direction: row; margin-bottom: 5%;'>"+
  "<div style='width: 50%; text-align: center;''>"+
    "<form action='https://" + LinkOfCollege + "'>"+
      "<input type='submit' value='Go to " + collegeName + "\'s website' class = 'collegewebsitebutton'/>"+
    "</form>"+
  "</div style='width: 50%;'>"+
  "<div style='width: 50%;'>"+
    "<form action='https://www.niche.com/colleges/" + collegeLink + "'>"+
      "<input type='submit' value='More Info on "+ collegeName + "' class = 'collegewebsitebutton'/>"+
    "</form>"+
  "</div style='width: 50%;'>"+
"</div>"
return tempString;
}

function makeGraphs(ctxType, race, stringName, num){
    let element = stringName.split(" ")[0].toLowerCase();
    try{
      var myChart = new Chart($(ctxType), {
        type: 'doughnut',
        data: {
            labels: [stringName, 'Other Demographics'],
            datasets: [{
                label: stringName,
                data: [parseFloat(race), (1  - parseFloat(race))],
                backgroundColor: [
                  'tomato',
                  '#343434',
                ],
                borderColor: [
                  '#343434',
                  'tomato',
                ],
                borderWidth: 1
            }]
        },
        options : {
          cutoutPercentage: 70,
          title : {text: stringName,        
                  display : true,
                  fontColor: '#000'
                  },
        }
    });
    $("#"+ element  + (num+1).toString() +"text").text(parseFloat(race).toFixed(2).toString().substr(2, 2) + "%");
    }
    catch(e){
      var myChart = new Chart($(ctxType), {
        type: 'doughnut',
        data: {
            labels: [stringName, 'Other Demographics'],
            datasets: [{
                label: stringName,
                data: [0, 1],
                backgroundColor: [
                  'tomato',
                  '#343434',
                ],
                borderColor: [
                  '#343434',
                  'tomato',
                ],
                borderWidth: 1
            }]
        },
        options : {
          cutoutPercentage: 70,
          title : {text: stringName,        
                  display : true,
                  fontColor: '#000'
                  },
        }
      });
      $("#"+ element  + (num+1).toString() +"text").text("N/A");

    }
  
}

function arrayToString(array){
  let returningString = "";
  for(let i = 0; i < array.length; i++){
    returningString += array[i] + ", ";
  }
  return returningString;
}

function arrayToString2(array){
  let returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].name + ",";
  }
  $("#colleges").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].price + ",";
  }
  $("#collegecost").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].state + ",";
  }
  $("#collegestates").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].city + ",";
  }
  $("#collegecities").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].temp + ",";
  }
  $("#collegetemperatures").val(returningString.substring(0, returningString.length -1));  
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].weather + ",";
  }
  $("#collegeweather").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].ACTscore + ",";
  }
  $("#collegeact").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].link + ",";
  }
  $("#collegelinks").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].priceCalcURL + ",";
  }
  $("#collegepricecalculator").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].nicheLink + ",";
  }
  $("#collegenicheurl").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].ACTscore + ",";
  }
  $("#collegeact").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].SATReadingscore + ",";
  }
  $("#collegesatreading").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].SATMathscore + ",";
  }
  $("#collegesatmath").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].blackPop + ",";
  }
  $("#collegeblackpop").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].whitePop + ",";
  }
  $("#collegewhitepop").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].asianPop + ",";
  }
  $("#collegeasianpop").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array.length; i++){
      returningString += array[i].hispanicPop + ",";
  }
  $("#collegehispanicpop").val(returningString.substring(0, returningString.length -1));
}

async function printAllSchools(response){
  var json = response;
  var length = json["results"].length;
  for(let i = 0; i < length; i++){
    allColleges+= json["results"][i]["school.name"];
  }
  $("#morecolleges").val(allColleges);
}

async function printSchool2(response){
  var json = response;
  var arr = [];
  var og = index;
  var length = json["results"].length > 3 ? 3 : json["results"].length;
  if(length == 0){
    $("#errorthrower").text("Your paramaters were too specific, try broadening your horizons by selecting less filters");
  }
  else{
    $("#errorthrower").text("");
  }
  for(var i =0; i < length; i++){
    var randy = Math.floor(Math.random() * (json["results"].length))
    if(!arr.includes(randy)){
      arr.push(randy);
      currentCollege = null;
      collegeNames[index] = json["results"][randy]["school.name"];
      currentCollege = new College(json["results"][randy]["school.name"]);
      currentCollege.ACTscore = json["results"][randy]["2017.admissions.act_scores.midpoint.cumulative"];
      currentCollege.SATReadingscore = json["results"][randy]["2017.admissions.sat_scores.midpoint.critical_reading"];
      currentCollege.SATMathscore = json["results"][randy]["2017.admissions.sat_scores.midpoint.math"];
      currentCollege.link = json["results"][randy]["school.school_url"];
      currentCollege.city = json["results"][randy]["school.city"];
      currentCollege.state = json["results"][randy]["school.state"];
      currentCollege.blackPop = json["results"][randy]["2017.student.demographics.race_ethnicity.black"];
      currentCollege.whitePop = json["results"][randy]["2017.student.demographics.race_ethnicity.white"];
      currentCollege.asianPop = json["results"][randy]["2017.student.demographics.race_ethnicity.asian"];
      currentCollege.hispanicPop = json["results"][randy]["2017.student.demographics.race_ethnicity.hispanic"];
      if($("#incomelevel").val() == "0-30000"){
        if(json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"] != null){
          currentCollege.price = json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"];
        }
        else{
          currentCollege.price = json["results"][randy]["2017.cost.net_price.private.by_income_level.0-30000"];
        }
      }
      if($("#incomelevel").val() == "30001-48000"){
        if(json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"] != null){
          currentCollege.price = json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"];
        }
        else{
          currentCollege.price = json["results"][randy]["2017.cost.net_price.private.by_income_level.30001-48000"];
        }
      }
      if($("#incomelevel").val() == "48001-75000"){
        if(json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"] != null){
          currentCollege.price = json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"];
        }
        else{
          currentCollege.price = json["results"][randy]["2017.cost.net_price.private.by_income_level.48001-75000"];
        }
      }
      if($("#incomelevel").val() == "75001-110000"){
        if(json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"] != null){
          currentCollege.price = json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"];
        }
        else{
          currentCollege.price = json["results"][randy]["2017.cost.net_price.private.by_income_level.75001-110000"];
        }
      }
      if($("#incomelevel").val() == "110001"){
        if(json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"] != null){
          currentCollege.price = json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"];
        }
        else{
          currentCollege.price = json["results"][randy]["2017.cost.net_price.private.by_income_level.110001-plus"];
        }
      }
      currentCollege.priceCalcURL = json["results"][randy]["school.price_calculator_url"];
      collegeNicheLinks[index] = collegeNames[index];
      currentCollege.nicheLink = currentCollege.name;

      if(currentCollege.nicheLink.includes("-")){
        currentCollege.nicheLink = currentCollege.nicheLink.replace("-", "---");
      }
      if(currentCollege.nicheLink.includes(" at ")){
        currentCollege.nicheLink = currentCollege.nicheLink.replace(" at ", "-");
      }
      currentCollege.nicheLink = currentCollege.nicheLink.replace(/ /g, "-");
    
      if(currentCollege.nicheLink.includes("'")){
        currentCollege.nicheLink = currentCollege.nicheLink.replace( "'", "");
      }

      currentCollege.nicheLink = "https://www.niche.com/colleges/" + currentCollege.nicheLink;
      index++;
      collegeObjs.push(currentCollege);
      let url2 = "https://api.openweathermap.org/data/2.5/weather?q="+currentCollege.city+",USA&appid=01e2ab091c2e3a0ab1eaca9b7e15f159";
      $.get(url2, null, tempcontrol);

    }
    else{$("#col"+index.toString()).val(collegeNames[index]);
      $("#useract").val(useract);
      $("#usersat").val(usersat);
      i--;
    }
  }
  arrayToString2(collegeObjs);
  index = og+3;
  if(globalState.length == 1 && index >= 3){
    await temp();
    if(finished){
      $("morecolleges").val(allColleges);
      $("#myform").submit();
    }
  }
  else if(globalState.length == 2 && index >= 6){
    await temp();
    if(finished){
      $("morecolleges").val(allColleges);
      $("#myform").submit();
    }
  }
  else if(globalState.length == 3 && index >= 9){
    await temp();
    if(finished){
      $("morecolleges").val(allColleges);
      $("#myform").submit();
    }
  }
}


 var state;
 var degree;

async function onButtonClick(){
  state = $("#states").val();
  globalState = state;
  degree = $("#degrees").val();
  hbcu = $("#hbcus").val();
  women = $("#womens").val();
  size = $("#sizes").val();
  field = $("#fields").val();
  $("#dropbtnsub").html(". . .");
  $("#cityOfUser").val($("#usercity").val());
  $("#stateOfUser").val($("#userstate").val());
  $("#houseHoldIncome").val($("#incomelevel").val());


let url1;

  let apikey = "BqsZbBBbY15kmLgw7gqce40EaoTpG0C0soJbpAen";
  switch (degree){
    case "1": 
      field = field.replace("bachelors", "certificate_lt_4_yr");
      break;
    case "2":
      field = field.replace("bachelors", "assoc");
      break;
    case "3":
      break;
    case "4":
      field = field.replace("bachelors", "bachelors");
      break;
    default:
      break;
  }
  if (field == "1" ){
    url1 = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.state_fips=" + state + "&school.degrees_awarded.predominant="+degree+"&school.minority_serving.historically_black="+hbcu +"&school.women_only="+ women +"&2017.student.size__range="+ size +"&_fields=id,school.name,2017.student.size,school.state,school.city,school.school_url,2017.admissions.act_scores.midpoint.cumulative,2017.admissions.sat_scores.midpoint.critical_reading,2017.admissions.sat_scores.midpoint.math,2017.cost.net_price.private.by_income_level.75001-110000,2017.cost.net_price.private.by_income_level.48001-75000,2017.cost.net_price.private.by_income_level.30001-48000,2017.cost.net_price.private.by_income_level.0-30000,2017.cost.net_price.public.by_income_level.75001-110000,2017.cost.net_price.public.by_income_level.48001-75000,2017.cost.net_price.public.by_income_level.30001-48000,2017.cost.net_price.public.by_income_level.0-30000,2017.cost.net_price.private.by_income_level.110001-plus,2017.cost.net_price.public.by_income_level.110001-plus,2017.student.demographics.race_ethnicity.black,2017.student.demographics.race_ethnicity.white,2017.student.demographics.race_ethnicity.asian,2017.student.demographics.race_ethnicity.hispanic,school.price_calculator_url&api_key=KpR5yoDP2jV5lIr5F4yA91Y8YnFLk3BBM8qdfkhi";
  }else {
    url1 =
    "https://api.data.gov/ed/collegescorecard/v1/schools.json?2017.academics."+ field +"=1&school.state_fips=" + state + "&school.degrees_awarded.predominant="+degree+"&school.minority_serving.historically_black="+hbcu +"&school.women_only="+ women +"&2017.student.size__range="+ size +"&_fields=id,school.name,2017.student.size,school.state,school.city,school.school_url,2017.admissions.act_scores.midpoint.cumulative,2017.admissions.sat_scores.midpoint.critical_reading,2017.admissions.sat_scores.midpoint.math,2017.cost.net_price.private.by_income_level.75001-110000,2017.cost.net_price.private.by_income_level.48001-75000,2017.cost.net_price.private.by_income_level.30001-48000,2017.cost.net_price.private.by_income_level.0-30000,2017.cost.net_price.public.by_income_level.75001-110000,2017.cost.net_price.public.by_income_level.48001-75000,2017.cost.net_price.public.by_income_level.30001-48000,2017.cost.net_price.public.by_income_level.0-30000,2017.cost.net_price.private.by_income_level.110001-plus,2017.cost.net_price.public.by_income_level.110001-plus,2017.student.demographics.race_ethnicity.black,2017.student.demographics.race_ethnicity.white,2017.student.demographics.race_ethnicity.asian,2017.student.demographics.race_ethnicity.hispanic,school.price_calculator_url&api_key=KpR5yoDP2jV5lIr5F4yA91Y8YnFLk3BBM8qdfkhi";
  }

  useract = $("#act").val();
  usersat = $("#sat").val();
  $("#useract1").val(useract);
  $("#useract2").val(useract);
  $("#useract3").val(useract);
  $("#usersat1").val(usersat);
  $("#usersat2").val(usersat);
  $("#usersat3").val(usersat);


  if(state.length == 0){
    if (field == "1" ){
      url1 = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.state_fips=48&school.degrees_awarded.predominant="+degree+"&school.minority_serving.historically_black="+hbcu +"&school.women_only="+ women +"&2017.student.size__range="+ size +"&_fields=id,school.name,2017.student.size,school.state,school.city,school.school_url,2017.admissions.act_scores.midpoint.cumulative,2017.admissions.sat_scores.midpoint.critical_reading,2017.admissions.sat_scores.midpoint.math,2017.cost.net_price.private.by_income_level.75001-110000,2017.cost.net_price.private.by_income_level.48001-75000,2017.cost.net_price.private.by_income_level.30001-48000,2017.cost.net_price.private.by_income_level.0-30000,2017.cost.net_price.public.by_income_level.75001-110000,2017.cost.net_price.public.by_income_level.48001-75000,2017.cost.net_price.public.by_income_level.30001-48000,2017.cost.net_price.public.by_income_level.0-30000,2017.cost.net_price.private.by_income_level.110001-plus,2017.cost.net_price.public.by_income_level.110001-plus,2017.student.demographics.race_ethnicity.black,2017.student.demographics.race_ethnicity.white,2017.student.demographics.race_ethnicity.asian,2017.student.demographics.race_ethnicity.hispanic,school.price_calculator_url&api_key=KpR5yoDP2jV5lIr5F4yA91Y8YnFLk3BBM8qdfkhi";
    }
    else {
      url1 =
      "https://api.data.gov/ed/collegescorecard/v1/schools.json?2017.academics."+ field +"=1&school.state_fips=48&school.degrees_awarded.predominant="+degree+"&school.minority_serving.historically_black="+hbcu +"&school.women_only="+ women +"&2017.student.size__range="+ size +"&_fields=id,school.name,2017.student.size,school.state,school.city,school.school_url,2017.admissions.act_scores.midpoint.cumulative,2017.admissions.sat_scores.midpoint.critical_reading,2017.admissions.sat_scores.midpoint.math,2017.cost.net_price.private.by_income_level.75001-110000,2017.cost.net_price.private.by_income_level.48001-75000,2017.cost.net_price.private.by_income_level.30001-48000,2017.cost.net_price.private.by_income_level.0-30000,2017.cost.net_price.public.by_income_level.75001-110000,2017.cost.net_price.public.by_income_level.48001-75000,2017.cost.net_price.public.by_income_level.30001-48000,2017.cost.net_price.public.by_income_level.0-30000,2017.cost.net_price.private.by_income_level.110001-plus,2017.cost.net_price.public.by_income_level.110001-plus,2017.student.demographics.race_ethnicity.black,2017.student.demographics.race_ethnicity.white,2017.student.demographics.race_ethnicity.asian,2017.student.demographics.race_ethnicity.hispanic,school.price_calculator_url&api_key=KpR5yoDP2jV5lIr5F4yA91Y8YnFLk3BBM8qdfkhi";
      $.get(url1, null, printSchool2);
    }
    finished = true;
  }
  else{
    for(var i = 0; i < state.length; i++){
      if (field == "1" ){
        url1 = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.state_fips=" + state[i] + "&school.degrees_awarded.predominant="+degree+"&school.minority_serving.historically_black="+hbcu +"&school.women_only="+ women +"&2017.student.size__range="+ size +"&_fields=id,school.name,2017.student.size,school.state,school.city,school.school_url,2017.admissions.act_scores.midpoint.cumulative,2017.admissions.sat_scores.midpoint.critical_reading,2017.admissions.sat_scores.midpoint.math,2017.cost.net_price.private.by_income_level.75001-110000,2017.cost.net_price.private.by_income_level.48001-75000,2017.cost.net_price.private.by_income_level.30001-48000,2017.cost.net_price.private.by_income_level.0-30000,2017.cost.net_price.public.by_income_level.75001-110000,2017.cost.net_price.public.by_income_level.48001-75000,2017.cost.net_price.public.by_income_level.30001-48000,2017.cost.net_price.public.by_income_level.0-30000,2017.cost.net_price.private.by_income_level.110001-plus,2017.cost.net_price.public.by_income_level.110001-plus,2017.student.demographics.race_ethnicity.black,2017.student.demographics.race_ethnicity.white,2017.student.demographics.race_ethnicity.asian,2017.student.demographics.race_ethnicity.hispanic,school.price_calculator_url&api_key=KpR5yoDP2jV5lIr5F4yA91Y8YnFLk3BBM8qdfkhi";
        await $.get(url1, null, printSchool2);
      }else {
        url1 =
        "https://api.data.gov/ed/collegescorecard/v1/schools.json?2017.academics."+ field +"=1&school.state_fips=" + state[i] + "&school.degrees_awarded.predominant="+degree+"&school.minority_serving.historically_black="+hbcu +"&school.women_only="+ women +"&2017.student.size__range="+ size +"&_fields=id,school.name,2017.student.size,school.state,school.city,school.school_url,2017.admissions.act_scores.midpoint.cumulative,2017.admissions.sat_scores.midpoint.critical_reading,2017.admissions.sat_scores.midpoint.math,2017.cost.net_price.private.by_income_level.75001-110000,2017.cost.net_price.private.by_income_level.48001-75000,2017.cost.net_price.private.by_income_level.30001-48000,2017.cost.net_price.private.by_income_level.0-30000,2017.cost.net_price.public.by_income_level.75001-110000,2017.cost.net_price.public.by_income_level.48001-75000,2017.cost.net_price.public.by_income_level.30001-48000,2017.cost.net_price.public.by_income_level.0-30000,2017.cost.net_price.private.by_income_level.110001-plus,2017.cost.net_price.public.by_income_level.110001-plus,2017.student.demographics.race_ethnicity.black,2017.student.demographics.race_ethnicity.white,2017.student.demographics.race_ethnicity.asian,2017.student.demographics.race_ethnicity.hispanic,school.price_calculator_url&api_key=KpR5yoDP2jV5lIr5F4yA91Y8YnFLk3BBM8qdfkhi";
        await $.get(url1, null, printSchool2);
        await $.get(url1, null, printAllSchools);
      }
    }
    arrayToString2(collegeObjs);
  }

}

async function temp(){
  for(var i = 0; i < collegeTemp.length; i++){
      if(collegecities[i] != undefined && collegecities[i] != ""){
        let url2 = "https://api.openweathermap.org/data/2.5/weather?q="+collegecities[i]+",USA&appid=01e2ab091c2e3a0ab1eaca9b7e15f159";
        index = i+1;
        await $.get(url2, null, tempcontrol);
      }
      else{
        $("#collegetemp"+index).val("NULL");
      }
      if(i == 8){
        finished = true;
      }
  }
}

async function tempcontrol(response){
  var json = response; 
  var celsius = json["main"]["temp"] - 273;
  var fahrenheit = (celsius*(9/5)) + 32;
  for(let i = 0; i < collegeObjs.length; i++){
      if(collegeObjs[i].city == json["name"]){
        collegeObjs[i].temp = parseInt(fahrenheit, 10);
        collegeObjs[i].weather = json["weather"][0]["description"];
        arrayToString2(collegeObjs);
      }
  }

}

function collegeimage(response){
  var json = response;
  var pic = json[4]["0"][1];
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
  // if (user != "") {
  //   $("#setter").text(user);
  //   $("#set1").val(user);
  // } else {
  //   $("#set1").val("log in");
  // }
}


window.onload= onLoad;
