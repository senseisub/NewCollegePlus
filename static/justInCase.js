function printSchool(response){
  var json = response;
  var arr = [];

  try{

    school = json["results"][0]["school.name"];
    console.log(json["results"][0]["school.name"]);
    console.log(json["results"][0]["school.city"]);
    console.log(json["results"][0]["school.state"]);
    console.log(json["results"][0]["school.school_url"]);
      $("#errorthrower").text("");
  }
  catch(err){
    $("#errorthrower").text("Your paramaters were too specific, try broadening your horizons by selecting less filters");
  }
  for(i=0; i<json["results"].length; i++){
    school = json["results"][i]["school.name"];
    school = json["results"][i]["school.city"];
    school = json["results"][i]["school.zip"];
    // console.log(school);
  }

  if(json["results"].length>3){
    // var Collegelist ="";
    for(var g =0; g<json["results"].length; g++){
      arr2.push(json["results"][g]["school.name"]);
      // arr2.push(json["results"][g]["school.city"]);
      // arr2.push(json["results"][g]["school.state"]);

    }
    console.log(arr2.join("\n"));
    $("#allcolleges").val(arr2.join(" | "));
    $("#morecollegestext").text(arr2.join("\n"));
  
  }

  if(json["results"].length>=3){
    console.log("there's 3");
    for(var a =0; a<3; a++){
      var randy = Math.floor(Math.random() * (json["results"].length-1))
      if(!arr.includes(json["results"][randy]["school.name"])){
        arr.push(json["results"][randy]["school.name"]);
        if(a==0){
          act1 = json["results"][randy]["2017.admissions.act_scores.midpoint.cumulative"];
          satreading1 = json["results"][randy]["2017.admissions.sat_scores.midpoint.critical_reading"];
          satmath1 = json["results"][randy]["2017.admissions.sat_scores.midpoint.math"];
          collegelink1 = json["results"][randy]["school.school_url"];
          collegecity1 = json["results"][randy]["school.city"];
          collegestate1 = json["results"][randy]["school.state"];
          blacks1 = json["results"][randy]["2017.student.demographics.race_ethnicity.black"];
          whites1 = json["results"][randy]["2017.student.demographics.race_ethnicity.white"];
          asians1 = json["results"][randy]["2017.student.demographics.race_ethnicity.asian"];
          hispanics1 = json["results"][randy]["2017.student.demographics.race_ethnicity.hispanic"];
          console.log(json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"])
          console.log(json["results"][randy]["2017.cost.net_price.private.by_income_level.110001-plus"]);
          if($("#incomelevel").val() == "0-30000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.0-30000"];
            }
          }
          if($("#incomelevel").val() == "30001-48000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.30001-48000"];
            }
          }
          if($("#incomelevel").val() == "48001-75000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.48001-75000"];
            }
          }
          if($("#incomelevel").val() == "75001-110000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.75001-110000"];
            }
          }
          if($("#incomelevel").val() == "110001"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.110001-plus"];
            }
          }
          pricecalc1 = json["results"][randy]["school.price_calculator_url"]
         
        }
        else if(a == 1){
          act2 = json["results"][randy]["2017.admissions.act_scores.midpoint.cumulative"];
          satreading2 = json["results"][randy]["2017.admissions.sat_scores.midpoint.critical_reading"];
          satmath2 = json["results"][randy]["2017.admissions.sat_scores.midpoint.math"];
          collegelink2 = json["results"][randy]["school.school_url"];
          collegecity2 = json["results"][randy]["school.city"];
          collegestate2 = json["results"][randy]["school.state"];
          blacks2 = json["results"][randy]["2017.student.demographics.race_ethnicity.black"];
          whites2 = json["results"][randy]["2017.student.demographics.race_ethnicity.white"];
          asians2 = json["results"][randy]["2017.student.demographics.race_ethnicity.asian"];
          hispanics2 = json["results"][randy]["2017.student.demographics.race_ethnicity.hispanic"];
          console.log(json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"]);
          console.log(json["results"][randy]["2017.cost.net_price.private.by_income_level.0-30000"]);
          if($("#incomelevel").val() == "0-30000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"] != null){
              collegeprice2 = json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"];
            }
            else{
              collegeprice2 = json["results"][randy]["2017.cost.net_price.private.by_income_level.0-30000"];
            }
          }
          if($("#incomelevel").val() == "30001-48000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"] != null){
              collegeprice2 = json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"];
            }
            else{
              collegeprice2 = json["results"][randy]["2017.cost.net_price.private.by_income_level.30001-48000"];
            }
          }
          if($("#incomelevel").val() == "48001-75000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"] != null){
              collegeprice2 = json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"];
            }
            else{
              collegeprice2 = json["results"][randy]["2017.cost.net_price.private.by_income_level.48001-75000"];
            }
          }
          if($("#incomelevel").val() == "75001-110000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"] != null){
              collegeprice2 = json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"];
            }
            else{
              collegeprice2 = json["results"][randy]["2017.cost.net_price.private.by_income_level.75001-110000"];
            }
          }
          if($("#incomelevel").val() == "110001"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"] != null){
              collegeprice2 = json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"];
            }
            else{
              collegeprice2 = json["results"][randy]["2017.cost.net_price.private.by_income_level.110001-plus"];
            }
          }
          pricecalc2 = json["results"][randy]["school.price_calculator_url"]
        }
        else if(a == 2){
          act3 = json["results"][randy]["2017.admissions.act_scores.midpoint.cumulative"];
          satreading3 = json["results"][randy]["2017.admissions.sat_scores.midpoint.critical_reading"];
          satmath3 = json["results"][randy]["2017.admissions.sat_scores.midpoint.math"];
          collegelink3 = json["results"][randy]["school.school_url"];
          collegecity3 = json["results"][randy]["school.city"];
          collegestate3 = json["results"][randy]["school.state"];
          blacks3 = json["results"][randy]["2017.student.demographics.race_ethnicity.black"];
          whites3 = json["results"][randy]["2017.student.demographics.race_ethnicity.white"];
          asians3 = json["results"][randy]["2017.student.demographics.race_ethnicity.asian"];
          hispanics3 = json["results"][randy]["2017.student.demographics.race_ethnicity.hispanic"];
          console.log(json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"]);
          console.log(json["results"][randy]["2017.cost.net_price.private.by_income_level.0-30000"]);
          finished = true;
          console.log(collegelink3);
          if($("#incomelevel").val() == "0-30000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"] != null){
              collegeprice3 = json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"];
            }
            else{
              collegeprice3 = json["results"][randy]["2017.cost.net_price.private.by_income_level.0-30000"];
            }
          }
          if($("#incomelevel").val() == "30001-48000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"] != null){
              collegeprice3 = json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"];
            }
            else{
              collegeprice3 = json["results"][randy]["2017.cost.net_price.private.by_income_level.30001-48000"];
            }
          }
          if($("#incomelevel").val() == "48001-75000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"] != null){
              collegeprice3 = json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"];
            }
            else{
              collegeprice3 = json["results"][randy]["2017.cost.net_price.private.by_income_level.48001-75000"];
            }
          }
          if($("#incomelevel").val() == "75001-110000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"] != null){
              collegeprice3 = json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"];
            }
            else{
              collegeprice3 = json["results"][randy]["2017.cost.net_price.private.by_income_level.75001-110000"];
            }
          }
          if($("#incomelevel").val() == "110001"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"] != null){
              collegeprice3 = json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"];
            }
            else{
              collegeprice3 = json["results"][randy]["2017.cost.net_price.private.by_income_level.110001-plus"];
            }
          }
          pricecalc3 = json["results"][randy]["school.price_calculator_url"]
        }
      }
      else{
        a--;
      }
    }
  $("#col1").val(arr[0]);
  $("#col2").val(arr[1]);
  $("#col3").val(arr[2]);
  $("#act1").val(act1);
  $("#act2").val(act2);
  $("#act3").val(act3);
  $("#satreading1").val(satreading1);
  $("#satreading2").val(satreading2);
  $("#satreading3").val(satreading3);
  $("#satmath1").val(satmath1);
  $("#satmath2").val(satmath2);
  $("#satmath3").val(satmath3);
  $("#college1link").val(collegelink1);
  $("#college2link").val(collegelink2);
  $("#college3link").val(collegelink3);
  collegecity1 =  collegecity1.replace(/\s/g, '+');
  collegecity2 =  collegecity2.replace(/\s/g, '+');
  collegecity3 =  collegecity3.replace(/\s/g, '+');
  $("#collegecity1").val(collegecity1);
  $("#collegecity2").val(collegecity2);
  $("#collegecity3").val(collegecity3);
  $("#collegestate1").val(collegestate1);
  $("#collegestate2").val(collegestate2);
  $("#collegestate3").val(collegestate3);
  $("#collegeprice1").val(collegeprice1);
  $("#collegeprice2").val(collegeprice2);
  $("#collegeprice3").val(collegeprice3);
  $("#pricecalc1").val(pricecalc1);
  $("#pricecalc2").val(pricecalc2);
  $("#pricecalc3").val(pricecalc3);
  $("#black1").val(blacks1);
  $("#white1").val(whites1);
  $("#asian1").val(asians1);
  $("#hispanic1").val(hispanics1);
  $("#black2").val(blacks2);
  $("#white2").val(whites2);
  $("#asian2").val(asians2);
  $("#hispanic2").val(hispanics2);
  $("#black3").val(blacks3);
  $("#white3").val(whites3);
  $("#asian3").val(asians3);
  $("#hispanic3").val(hispanics3);
  $("#userState").val($("#userstate").val());
  $("#usercity").val($("#usercity").val());
  var url2 = "https://api.openweathermap.org/data/2.5/weather?q="+collegecity1+",USA&appid=01e2ab091c2e3a0ab1eaca9b7e15f159";
  $.get(url2, null, tempcontrol);
  url2 = "https://api.openweathermap.org/data/2.5/weather?q="+collegecity2+",USA&appid=01e2ab091c2e3a0ab1eaca9b7e15f159";
  $.get(url2, null, tempcontrol);
  url2 = "https://api.openweathermap.org/data/2.5/weather?q="+collegecity3+",USA&appid=01e2ab091c2e3a0ab1eaca9b7e15f159";
  $.get(url2, null, tempcontrol);
  linkcollege = arr[0];
  if(linkcollege.includes("-")){
    linkcollege = linkcollege.replace("-", "---");
  }
  if(linkcollege.includes(" at ")){
    linkcollege = linkcollege.replace(" at ", "-");
  }
  linkcollege = linkcollege.replace(/ /g, "-");

  if(linkcollege.includes("'")){
    linkcollege = linkcollege.replace( "'", "");
  }
    
    linkcollege1 = arr[1];
    if(linkcollege1.includes("-")){
      linkcollege1 = linkcollege1.replace("-", "---");
    }
    if(linkcollege1.includes(" at ")){
      linkcollege1 = linkcollege1.replace(" at ", "-");
    }
    linkcollege1 = linkcollege1.replace(/ /g, "-");
      
    if(linkcollege1.includes("'")){
      linkcollege1 = linkcollege1.replace( "'", "");
    }
      
      linkcollege2 = arr[2];
      if(linkcollege2.includes("-")){
        linkcollege2 = linkcollege2.replace("-", "---");
      }
      if(linkcollege2.includes(" at ")){
        linkcollege2 = linkcollege2.replace( " at ", "-");
      }
      linkcollege2 = linkcollege2.replace(/ /g, "-");

      if(linkcollege2.includes("'")){
        linkcollege2 = linkcollege2.replace( "'", "");
      }
        
    $("#linkcollege1").val(linkcollege);
    $("#linkcollege2").val(linkcollege1);
    $("#linkcollege3").val(linkcollege2);
    // $("#col2").val(arr[1]);
    // $("#col3").val(arr[2]);
    console.log(linkcollege);
    console.log(linkcollege1);
    console.log(linkcollege2);
    finished = true;
  }

  else if(json["results"].length==2){
    for(var a =0; a<2; a++){
      var randy = Math.floor(Math.random() * (json["results"].length-1))
      if(!arr.includes(json["results"][randy]["school.name"])){
        arr.push(json["results"][randy]["school.name"]);
        if(a==0){
          act1 = json["results"][randy]["2017.admissions.act_scores.midpoint.cumulative"];
          satreading1 = json["results"][randy]["2017.admissions.sat_scores.midpoint.critical_reading"];
          satmath1 = json["results"][randy]["2017.admissions.sat_scores.midpoint.math"];
          collegelink1 = json["results"][randy]["school.school_url"];
          collegecity1 = json["results"][randy]["school.city"];
          collegestate1 = json["results"][randy]["school.state"];
          blacks1 = json["results"][randy]["2017.student.demographics.race_ethnicity.black"];
          whites1 = json["results"][randy]["2017.student.demographics.race_ethnicity.white"];
          asians1 = json["results"][randy]["2017.student.demographics.race_ethnicity.asian"];
          hispanics1 = json["results"][randy]["2017.student.demographics.race_ethnicity.hispanic"];
          if($("#incomelevel").val() == "0-30000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.0-30000"];
            }
          }
          if($("#incomelevel").val() == "30001-48000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.30001-48000"];
            }
          }
          if($("#incomelevel").val() == "48001-75000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.48001-75000"];
            }
          }
          if($("#incomelevel").val() == "75001-110000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.75001-110000"];
            }
          }
          if($("#incomelevel").val() == "110001"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.110000-plus"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.110001-plus"];
            }
          }
          pricecalc1 = json["results"][randy]["school.price_calculator_url"]
        }
        else if(a == 1){
          act2 = json["results"][randy]["2017.admissions.act_scores.midpoint.cumulative"];
          satreading2 = json["results"][randy]["2017.admissions.sat_scores.midpoint.critical_reading"];
          satmath2 = json["results"][randy]["2017.admissions.sat_scores.midpoint.math"];
          collegelink2 = json["results"][randy]["school.school_url"];
          collegecity2 = json["results"][randy]["school.city"];
          collegestate2 = json["results"][randy]["school.state"];
          blacks2 = json["results"][randy]["2017.student.demographics.race_ethnicity.black"];
          whites2 = json["results"][randy]["2017.student.demographics.race_ethnicity.white"];
          asians2 = json["results"][randy]["2017.student.demographics.race_ethnicity.asian"];
          hispanics2 = json["results"][randy]["2017.student.demographics.race_ethnicity.hispanic"];
          finished = true;
          if($("#incomelevel").val() == "0-30000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"] != null){
              collegeprice2 = json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"];
            }
            else{
              collegeprice2 = json["results"][randy]["2017.cost.net_price.private.by_income_level.0-30000"];
            }
          }
          if($("#incomelevel").val() == "30001-48000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"] != null){
              collegeprice2 = json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"];
            }
            else{
              collegeprice2 = json["results"][randy]["2017.cost.net_price.private.by_income_level.30001-48000"];
            }
          }
          if($("#incomelevel").val() == "48001-75000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"] != null){
              collegeprice2 = json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"];
            }
            else{
              collegeprice2 = json["results"][randy]["2017.cost.net_price.private.by_income_level.48001-75000"];
            }
          }
          if($("#incomelevel").val() == "75001-110000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"] != null){
              collegeprice2 = json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"];
            }
            else{
              collegeprice2 = json["results"][randy]["2017.cost.net_price.private.by_income_level.75001-110000"];
            }
          }
          if($("#incomelevel").val() == "110001"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.110000-plus"] != null){
              collegeprice2 = json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"];
            }
            else{
              collegeprice2 = json["results"][randy]["2017.cost.net_price.private.by_income_level.110001-plus"];
            }
          }
          pricecalc2 = json["results"][randy]["school.price_calculator_url"]
        }
      }
      else{
        a--;
      }
    }
    $("#col1").val(arr[0]);
    $("#col2").val(arr[1]);
    $("#act1").val(act1);
    $("#act2").val(act2);
    $("#satreading1").val(satreading1);
    $("#satreading2").val(satreading2);
    $("#satmath1").val(satmath1);
    $("#satmath2").val(satmath2);
    $("#college1link").val(collegelink1);
    $("#college2link").val(collegelink2);
    collegecity1 =  collegecity1.replace(/\s/g, '+');
    collegecity1 =  collegecity1.replace(/\s/g, '+');
    $("#collegecity1").val(collegecity1);
    $("#collegecity2").val(collegecity2);
    $("#collegestate1").val(collegestate1);
    $("#collegestate2").val(collegestate2);
    $("#collegeprice1").val(collegeprice1);
    $("#collegeprice2").val(collegeprice2);
    $("#pricecalc1").val(pricecalc1);
    $("#pricecalc2").val(pricecalc2);
    $("#black1").val(blacks1);
    $("#white1").val(whites1);
    $("#asian1").val(asians1);
    $("#hispanic1").val(hispanics1);
    $("#black2").val(blacks2);
    $("#white2").val(whites2);
    $("#asian2").val(asians2);
    $("#hispanic2").val(hispanics2);
    linkcollege = arr[0];
    var url2 = "https://api.openweathermap.org/data/2.5/weather?q="+collegecity1+",USA&appid=01e2ab091c2e3a0ab1eaca9b7e15f159";
    $.get(url2, null, tempcontrol);
    url2 = "https://api.openweathermap.org/data/2.5/weather?q="+collegecity2+",USA&appid=01e2ab091c2e3a0ab1eaca9b7e15f159";
    $.get(url2, null, tempcontrol);
    if(linkcollege.includes("-")){
      linkcollege = linkcollege.replace("-", "---");
    }
    if(linkcollege.includes(" at ")){
      linkcollege = linkcollege.replace(" at ", "-");
    }
    linkcollege = linkcollege.replace(/ /g, "-");

    if(linkcollege.includes("'")){
      linkcollege = linkcollege.replace( "'", "");
    }
      
      linkcollege1 = arr[1];
      if(linkcollege1.includes("-")){
        linkcollege1 = linkcollege1.replace("-", "---");
      }
      if(linkcollege1.includes(" at ")){
        linkcollege1 = linkcollege1.replace(" at ", "-");
      }
      linkcollege1 = linkcollege1.replace(/ /g, "-");

      if(linkcollege1.includes("'")){
        linkcollege1 = linkcollege1.replace( "'", "");
      }
        $("#linkcollege1").val(linkcollege);
        $("#linkcollege2").val(linkcollege1);
        superList.push(top);
        finished = true;

  }

  else if(json["results"].length==1){
    for(var a =0; a<1; a++){
      var randy = Math.floor(Math.random() * (json["results"].length-1))
      if(!arr.includes(json["results"][randy]["school.name"])){
        arr.push(json["results"][randy]["school.name"]);
        if(a==0){
          act1 = json["results"][randy]["2017.admissions.act_scores.midpoint.cumulative"];
          satreading1 = json["results"][randy]["2017.admissions.sat_scores.midpoint.critical_reading"];
          satmath1 = json["results"][randy]["2017.admissions.sat_scores.midpoint.math"];
          collegelink1 = json["results"][randy]["school.school_url"];
          collegecity1 = json["results"][randy]["school.city"];
          collegestate1 = json["results"][randy]["school.state"];
          blacks1 = json["results"][randy]["2017.student.demographics.race_ethnicity.black"];
          whites1 = json["results"][randy]["2017.student.demographics.race_ethnicity.white"];
          asians1 = json["results"][randy]["2017.student.demographics.race_ethnicity.asian"];
          hispanics1 = json["results"][randy]["2017.student.demographics.race_ethnicity.hispanic"];
          finished = true;
          if($("#incomelevel").val() == "0-30000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.0-30000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.0-30000"];
            }
          }
          if($("#incomelevel").val() == "30001-48000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.30001-48000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.30001-48000"];
            }
          }
          if($("#incomelevel").val() == "48001-75000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.48001-75000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.48001-75000"];
            }
          }
          if($("#incomelevel").val() == "75001-110000"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.75001-110000"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.75001-110000"];
            }
          }
          if($("#incomelevel").val() == "110001"){
            if(json["results"][randy]["2017.cost.net_price.public.by_income_level.110000-plus"] != null){
              collegeprice1 = json["results"][randy]["2017.cost.net_price.public.by_income_level.110001-plus"];
            }
            else{
              collegeprice1 = json["results"][randy]["2017.cost.net_price.private.by_income_level.110001-plus"];
            }
          }
          pricecalc1 = json["results"][randy]["school.price_calculator_url"]
        }
      }
      else{
        a--;
      }
    }
    $("#col1").val(arr[0]);
    $("#act1").val(act1);
    $("#satreading1").val(satreading1);
    $("#satmath1").val(satmath1);
    $("#college1link").val(collegelink1);
    collegecity1 =  collegecity1.replace(/\s/g, '+');
    $("#collegecity1").val(collegecity1);
    $("#collegestate1").val(collegestate1);
    $("#collegeprice1").val(collegeprice1);
    $("#pricecalc1").val(pricecalc1);
    $("#black1").val(blacks1);
    $("#white1").val(whites1);
    $("#asian1").val(asians1);
    $("#hispanic1").val(hispanics1);
    linkcollege = arr[0];
    var url2 = "https://api.openweathermap.org/data/2.5/weather?q="+collegecity1+",USA&appid=01e2ab091c2e3a0ab1eaca9b7e15f159";
    $.get(url2, null, tempcontrol);
    if(linkcollege.includes("-")){
      linkcollege = linkcollege.replace("-", "---");
    }
    if(linkcollege.includes(" at ")){
      linkcollege = linkcollege.replace(" at ", "-");
    }
    linkcollege = linkcollege.replace(/ /g, "-");

    if(linkcollege.includes("'")){
      linkcollege = linkcollege.replace( "'", "");
    }
      
      $("#linkcollege1").val(linkcollege);
      finished = true;

  }

  console.log(arr);
  
  if(finished){
    $("#myform").submit();
  }
  // $("#dropbtnsub").css("display", "none");

  // $("#dropbtnnxt").css("display", "block");

  let url3 = "https://serpapi.com/playground?engine=google&q=smu&google_domain=google.com&ijn=0&tbm=isch";
    $.get(url3, null, collegeimage);
    console.log(url3);

}