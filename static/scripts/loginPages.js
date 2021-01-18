let isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
function signOut() {
        var auth2 = gapi.auth2.getAuthInstance();
        auth2.signOut().then(function () {
        });
    }

function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    // console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    // console.log('Name: ' + profile.getName());
    // console.log('Image URL: ' + profile.getImageUrl());
    // console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    $("#googleUsername").val(profile.getEmail());
    $("#googleImage").val(profile.getImageUrl());
    while($("#googleUsername").val().length == 0){

    }
    signOut();
    $("#google").submit();
}

var valUser = false;
var valPassword = false;
var passwordClicked = false;
function checkLegitmacy(){
    var x = $("#username").val();
    var indexOfAt = 0;
    var indexOfDot = 0;
    for(var i = 0; i < x.length; i++){
        if(x.charAt(i) == '@'){
            indexOfAt = i;
        }
        else if(x.charAt(i) == '.'){
            indexOfDot = i;
        }
    }
    if(indexOfAt == 0 || indexOfDot == 0 || indexOfAt > indexOfDot){
        $("#emailchecker").css("display", "block");
        $("#emailchecker").text("That is not a valid email");
        valUser= false;
    }
    else{
        valUser= true;
        $("#emailchecker").css("display", "none");
    }
}

function passwordLegitmacy(){
    var x = $("#password").val();
    var numNums = 0;
    var numLetters = 0;
    var numSpecials = 0;
    for(var i = 0; i < x.length; i++){
        if((x.charAt(i)>= 'a' && x.charAt(i) <= 'z') || (x.charAt(i)>= 'A' && x.charAt(i) <= 'Z')){
            numLetters++;
        }
        else if((x.charAt(i)>= '0' && x.charAt(i) <= '9')){
            numNums++;
        }
        else{
            numSpecials++;
        }
    }
    if(numNums > 0 && numLetters > 0 && numSpecials > 0 && x.length > 7){
        $("#error").css("display", "none");
        valPassword = true;
    }
    else{
        $("#error").css("display", "block");
        $("#error").text("That is not a valid password");
        valPassword = false;
    }
}
$(document).ready(() => {
    if(isMobile){
        $("#form input").css({"font-size" : "20pt"});
        $("#form label").css({"font-size" : "20pt"});
        $("#form m").css({"font-size" : "20pt"});
        $("#login").css({"font-size" : "20pt"});
        $(".banner").css({"font-size" : "28pt"});
        $(".alternative").css({"font-size" : "28pt"});
        $("#signUp").css({"font-size" : "20pt"});
    }
  });
function onLoad(){
    if($("#error").text() != "{{name}}"){
        $("#error").css("display", "block");
    }

    $("#password").focus(checkLegitmacy);
    if(passwordClicked){
        $("#username").focus(passwordLegitmacy);
    }
    $("#subButt").click(function(){
        console.log("click")

        checkLegitmacy();
        passwordLegitmacy();
        if(!valUser || !valPassword){
            $("#error").text("Invalid Username or Password");
            return;
        }
        else{
            $("#error").css("display", "none");
            $("#subButt").prop("disabled", false);
        }
        var x = $("#username").val();
        var y = $("#password").val();

        if(valUser && valPassword){
            $("#form").submit();
        }
        
    });
    $("#login").click(function(){
        document.location.href = "/login";
    });
    $("#signUp").click(function(){
        document.location.href = "/withGoogle";
    });

    $("#TextOn").click(function(){
        var x = document.getElementById("password");
        if (x.type === "password") {
            $("#password").prop("type", "text");
        } else {
            $("#password").prop("type", "password");
        }
    });
    $("#logo").click(function(){
        document.location.href = "/mobile/home";
    });
    $("#Privacy").change(() => {
        if($("#Privacy").is(':checked')){
            $("#subButt").prop('disabled', false);
        }
        else{
            $("#subButt").prop('disabled', true);
            if($(".banner").text() == "Log into CollegePlus!"){
                $("#subButt").prop('disabled', false);

            }
        }
    });
    if($("#Privacy").is(':checked')){
        $("#subButt").prop('disabled', false);
    }
    else{
        $("#subButt").prop('disabled', true);
        if($("#Privacy").length  == 0){
            $("#subButt").prop('disabled', false);

        }
    }

    $("#Privacy2").change(() => {
        if($("#Privacy2").is(':checked')){
            $("#googleSubmitter").prop('disabled', false);
        }
        else{
            $("#googleSubmitter").prop('disabled', true);
        }
    });
    if($("#Privacy2").is(':checked')){
        $("#googleSubmitter").prop('disabled', false);
    }
    else{
        $("#googleSubmitter").prop('disabled', true);
    }

    $("#forgotpassword").click(() => {document.location.href = "/ForgotPassword"});
}
window.onload = onLoad;
$( window ).resize(function() {
if(($( window ).height()/ $( window ).width()) > 1.5 || isMobile){
$("#form input").css({"font-size" : "20pt"});
$("#form m").css({"font-size" : "20pt"});
$("#form label").css({"font-size" : "20pt"});
$("#login").css({"font-size" : "20pt"});
$(".banner").css({"font-size" : "28pt"});
$(".alternative").css({"font-size" : "28pt"});
$("#signUp").css({"font-size" : "20pt"});

}
else{
$("#form m").css({"font-size" : "12pt"});
$("#form input").css({"font-size" : "12pt"});
$("#form label").css({"font-size" : "12pt"});
$("#login").css({"font-size" : "12pt"});
$("#signUp").css({"font-size" : "12pt"});
$(".banner").css({"font-size" : "24pt"});
$(".alternative").css({"font-size" : "24pt"});


}
});