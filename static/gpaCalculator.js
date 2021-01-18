var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    
var apClassesWeighted = [5.3, 5.0, 4.7, 4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 0.0];
var honorsClassesWeighted = [4.8, 4.5, 4.17, 3.8, 3.5, 3.17, 2.8, 2.5, 2.17, 1.8, 1.5, 1.17, 0.0]
var regularClassesWeighted = [4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, .07, 0.0];
var allUnweighted = [4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, .07, 0.0];
var gradeValues = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"];
var superSumOfCredits = 0;
var superGradePoints = 0;
var sumOfCreditsOne = 0;
var gradepointsOne = 0;
var sumOfCreditsTwo = 0;
var gradepointsTwo = 0;
var sumOfCreditsThree = 0;
var gradepointsThree = 0;
var sumOfCreditsFour = 0;
var gradepointsFour = 0;
var sumOfCreditsFive = 0;
var gradepointsFive = 0;
var sumOfCreditsSix = 0;
var gradepointsSix = 0;
var sumOfCreditsSeven = 0;
var gradepointsSeven = 0;
var sumOfCreditsEight = 0;
var gradepointsEight = 0;
var gpa = 0;
var weighted = true;
var unweighted = false;
var credit = "";
var clickedbyone = false;
var clickedbytwo = false;
var clickedbythree = false;
var clickedbyfour = false;
var clickedbyfive = false;
var clickedbysix = false;
var clickedbyseven = false;
var clickedbyeight = false;
let data1 = {
    "gradepoint" : 0,
    "sumOfCredits" : 0,
    "clicked" : false,
    "gradeName" : "#grades",
    "creditName" : "#credits"
}

let data2 = {
    "gradepoint" : 0,
    "sumOfCredits" : 0,
    "clicked" : false,
    "gradeName" : "#grades2",
    "creditName" : "#credits2"
}
let data3 = {
    "gradepoint" : 0,
    "sumOfCredits" : 0,
    "clicked" : false,
    "gradeName" : "#grades3",
    "creditName" : "#credits3"
}

let data4 = {
    "gradepoint" : 0,
    "sumOfCredits" : 0,
    "clicked" : false,
    "gradeName" : "#grades4",
    "creditName" : "#credits4"
}

let data5 = {
    "gradepoint" : 0,
    "sumOfCredits" : 0,
    "clicked" : false,
    "gradeName" : "#grades5",
    "creditName" : "#credits5"
}

let data6= {
    "gradepoint" : 0,
    "sumOfCredits" : 0,
    "clicked" : false,
    "gradeName" : "#grades6",
    "creditName" : "#credits6"
}

let data7 = {
    "gradepoint" : 0,
    "sumOfCredits" : 0,
    "clicked" : false,
    "gradeName" : "#grades7",
    "creditName" : "#credits7"
}

let data8 = {
    "gradepoint" : 0,
    "sumOfCredits" : 0,
    "clicked" : false,
    "gradeName" : "#grades8",
    "creditName" : "#credits8"
}

let mainWidth =  $( window ).width();


function onLoad(){
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
    $("#college").click(function(){
        document.location.href = "/mobile/home";
    });
    $("#weighted").click(function(){
        weighted= true; 
        unweighted = false;
        $("#weighted").css("border", "5px solid green");
        $("#unweighted").css("border", "5px solid gray");
    });
    
    $("#unweighted").click(function(){
        unweighted= true; 
        weighted = false;
        $("#unweighted").css("border", "5px solid green");
        $("#weighted").css("border", "5px solid gray");
    });

    
    $("#grades").change(() => {calcGPA(data1)});
    $("#credits").change(() => {calcGPA(data1)});
    $("#type").change(() => {calcGPA(data1)});
    $("#grades2").change(() => {calcGPA(data2)});
    $("#credits2").change(() => {calcGPA(data2)});
    $("#type2").change(() => {calcGPA(data2)});
    $("#grades3").change(() => {calcGPA(data3)});
    $("#credits3").change(() => {calcGPA(data3)});
    $("#type3").change(() => {calcGPA(data3)});
    $("#grades4").change(() => {calcGPA(data4)});
    $("#credits4").change(() => {calcGPA(data4)});
    $("#type4").change(() => {calcGPA(data4)});
    $("#grades5").change(() => {calcGPA(data5)});
    $("#credits5").change(() => {calcGPA(data5)});
    $("#type5").change(() => {calcGPA(data5)});
    $("#grades6").change(() => {calcGPA(data6)});
    $("#credits6").change(() => {calcGPA(data6)});
    $("#type6").change(() => {calcGPA(data6)});
    $("#grades7").change(() => {calcGPA(data7)});
    $("#credits7").change(() => {calcGPA(data7)});
    $("#type7").change(() => {calcGPA(data7)});
    $("#grades8").change(() => {calcGPA(data8)});
    $("#credits8").change(() => {calcGPA(data8)});
    $("#type8").change(() => {calcGPA(data8)});

    
}

function calcGPA(data){
    console.log(data);
    credit= parseInt($(data["creditName"]).val());
    if(data["clicked"] == true){
        data["gradepoint"] = 0;
        data["sumOfCredits"]=0;
    }
    data["clicked"] = true;
    for(var i = 0; i < gradeValues.length; i++){
        if($(data["gradeName"]).val() == gradeValues[i]){
            if($("#type").val() == "AP"){
                if(weighted == true){
                    data["gradepoint"] += apClassesWeighted[i]*credit;
                    data["sumOfCredits"] += credit;
                }
                else{
                    data["gradepoint"] += allUnweighted[i]*credit;
                    data["sumOfCredits"] += credit;
                }
            }
            else if($("#type").val() == "IB"){
                if(weighted == true){
                    data["gradepoint"] += apClassesWeighted[i]*credit;
                    data["sumOfCredits"] += credit;
                }
                else{
                    data["gradepoint"] += allUnweighted[i]*credit;
                    data["sumOfCredits"] += credit;
                }
            }
            else if($("#type").val() == "Dual-Credit"){
                if(weighted == true){
                    data["gradepoint"] += honorsClassesWeighted[i]*credit;
                    data["sumOfCredits"] += credit;
                }
                else{
                    data["gradepoint"] += allUnweighted[i]*credit;
                    data["sumOfCredits"] += credit;
                }
            }
            else if($("#type").val() == "Honors"){
                if(weighted == true){
                    data["gradepoint"] += honorsClassesWeighted[i]*credit;
                    data["sumOfCredits"] += credit;
                }
                else{
                    data["gradepoint"] += allUnweighted[i]*credit;
                    data["sumOfCredits"] += credit;
                }
            }
            else if($("#type").val() == "Regular"){
                if(weighted == true){
                    data["gradepoint"] += regularClassesWeighted[i]*credit;
                    data["sumOfCredits"] += credit;
                }
                else{
                    data["gradepoint"] += allUnweighted[i]*credit;
                    data["sumOfCredits"] += credit;
                }
            }
            break;
        }
    }
    gpa = (data1["gradepoint"] + data2["gradepoint"]+ data3["gradepoint"]+ data4["gradepoint"]+ data5["gradepoint"]+ data6["gradepoint"]+ data7["gradepoint"] + data8["gradepoint"])/(data1["sumOfCredits"] + data2["sumOfCredits"] + data3["sumOfCredits"] + data4["sumOfCredits"] + data5["sumOfCredits"] +data6["sumOfCredits"] +data7["sumOfCredits"] +data8["sumOfCredits"]);
    $("#gpaOutput").text(gpa.toFixed(2));
    $("#gpaholder").val(gpa.toFixed(2));
}



window.onload = onLoad;


$( window ).resize(function() {
    if(($( window ).height()/ $( window ).width()) > 1.5 || isMobile){
      $(".rowSection").css({"min-width" : (mainWidth * .9) + "px"});
      $(".drop").css({"font-size" : "20pt"});
      $(".form__input").css({"font-size" : "20pt"});
      $("#weighted").css({"font-size" : "20pt", "width" : "40%"});
      $("#unweighted").css({"font-size" : "20pt", "width" : "40%"});
      $(".cfq").css({"font-size" : "20pt"});
      $("#question").css({"font-size" : "28pt"});
      $("#submitter").css({"font-size" : "20pt"});

    }
    else{
      $(".rowSection").css({"min-width" : "400px"});
      $(".drop").css({"font-size" : "12pt"});
      $(".form__input").css({"font-size" : "12pt"});
      $("#weighted").css({"font-size" : "12pt"});
      $("#unweighted").css({"font-size" : "12pt"});
      $(".cfq").css({"font-size" : "12pt"});
      $("#question").css({"font-size" : "24pt"});
      $("#submitter").css({"font-size" : "12pt"});

    }
  });


  $(document).ready(() => {
    if(isMobile){
        $(".rowSection").css({"min-width" : (mainWidth * .9) + "px"});
        $(".drop").css({"font-size" : "20pt"});
        $(".form__input").css({"font-size" : "20pt"});
        $("#weighted").css({"font-size" : "20pt", "width" : "40%"});
        $("#unweighted").css({"font-size" : "20pt", "width" : "40%"});
        $(".cfq").css({"font-size" : "20pt"});
        $("#question").css({"font-size" : "28pt"});
        $("#submitter").css({"font-size" : "20pt"});
    }
  });