var ethnic = 0;
var engineering =0;
var communication=0;
var legal=0;
var english=0;
var biological=0;
var computer = 0;
var education = 0;
var political = 0;
var business = 0;
var economics;
var nursing = 0;
var finance = 0;
var history = 0;
var kinesiology = 0;
let finished = false;

var list1 = [ethnic, engineering, communication, legal, english, biological, computer, education, political, business, economics, nursing, finance, history];
var list2 = ["Ethnic and Gender Studies", "Engineering", "Communication", "Legal Studies", "English", "Biological Sciences", "Computer Science", "Education", "Political Science", "Business", "Economics", "Nursing", "Finance", "History"];

function arrayToString(array1, array2, array3){
  let returningString = "";
  for(let i =0; i < array1.length; i++){
      returningString += array1[i] + ",";
  }
  $("#majors").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array2.length; i++){
      returningString += array2[i] + ",";
  }
  $("#majorLinks").val(returningString.substring(0, returningString.length -1));
  returningString = "";
  for(let i =0; i < array3.length; i++){
      returningString += array3[i] + "^";
  }
  $("#descriptions").val(returningString.substring(0, returningString.length -1));
}

function arrayToString2(arr){
    let returningString = "";
    for(let i = 0; i < arr.length; i++){
        returningString += arr[i] + ",";
    }
    return returningString.substring(0, returningString.length-1);
}

function calc(){
  //first question
  for(let i=0; i<list1.length; i++){
    if($("#ques1").val() == list2[i]){
      list1[i]++;
    }
    if($("#ques2").val() == list2[i]){
      list1[i]++;
    }
    if($("#ques3").val() == list2[i]){
      list1[i]++;
    }
    if($("#ques4").val() == list2[i]){
      list1[i]++;
    }
    if($("#ques5").val() == list2[i]){
      list1[i]++;
    }
    if($("#ques6").val() == list2[i]){
      list1[i]++;
    }
    if($("#ques7").val() == list2[i]){
      list1[i]++;
    }
    if($("#ques8").val() == list2[i]){
      list1[i]++;
    }
    if($("#ques9").val() == list2[i]){
      list1[i]++;
    }
    if($("#ques10").val() == list2[i]){
      list1[i]++;
    }
  }
  var top3 = [];
  var descriptions = [];
  var urlslist = [];
  var list2clone = ["Ethnic and Gender Studies", "Engineering", "Communication", "Legal Studies", "English", "Biological Sciences", "Computer Science", "Education", "Political Science", "Business", "Economics", "Nursing", "Finance", "History"];
  var list1clone = [ethnic, engineering, communication, legal, english, biological, computer, education, political, business, economics, nursing, finance, history];
  let description = ["The ethnic studies field explores theories of race, migration, social policy and historical instances regarding various ethnic groups. Gender studies focuses on how the different sexes handle various issues and includes feminist and masculinity theory, as well as theories regarding sexuality, gender roles and various types of gender social systems.",
          "An Engineer applies science and mathematics to technical problems. They help develop new products by recording and analyzing performance and material parts for testing. Engineers play an essential role in your business during the processes of product development and maintenance.",
          "A communications major is a major designed to teach you about effective communication and how to apply it to fields like media, law and business. Coursework for this major is very similar to coursework for related majors such as public relations, advertising and journalism.",
          "Legal studies is an undergraduate major that focuses on how law impacts and interacts with many areas of our lives. Its goal is to empower students to pursue work in the many jobs that deal with law, whether inside or outside the legal field, apart from being a lawyer.",
          "An English major is a humanities degree option that comes with plenty of opportunities for students to explore different styles of expression. An undergraduate background in English is useful for graduate and professional programs in fields like journalism, law and business.",
          "A general program of biology at the introductory, basic level or a program in biology or the biological sciences that is undifferentiated as to title or content. Includes instruction in general biology and programs covering a variety of biological specializations.",
          "A program that focuses on computer theory, computing problems and solutions, and the design of computer systems and user interfaces from a scientific perspective. Includes instruction in the principles of computational science, computer development and programming, and applications to a variety of end-use situations.",
          "An education major is designed to help college students develop the skills to teach others. Combining the ability to create engaging lessons with the desire to spread knowledge, this major is all about learning the most effective ways to become an educator.",
          "A political science major is a social science degree path that requires students to study government in theory and practice. Majors will explore topics related to political theory, international relations, comparative politics and more. ",
          "Generally, business degrees are designed to help students prepare for a wide range of positions and industries by introducing them to the fundamental aspects of business knowledge in accounting, finance, international business, marketing, human resources, operations and project management.",
          "An economics major is a degree option that examines questions related to resource allocation, incentives and wealth, among others. Economics is relevant to graduate and professional study in fields like business management, law and public affairs, as well as undergraduate degrees that are useful for many career paths. Students often begin their studies by developing a solid foundation in microeconomics, macroeconomics and calculus, which they can use to pursue more advanced coursework and research opportunities.",
          "Most of the classes in a BSN program are grounded in the biological sciences and liberal arts. In addition to classroom lectures, nursing students participate in clinical training where they work in healthcare facilities under the supervision of a licensed nurse.",
          "A program that generally prepares individuals to plan, manage, and analyze the financial and monetary aspects and performance of business enterprises, banking institutions, or other organizations. Includes instruction in principles of accounting, financial instruments, capital planning, funds acquisition, asset and debt management, budgeting, financial analysis, and investments and portfolio management.",
          "A program that focuses on the general study and interpretation of the past, including the gathering, recording, synthesizing and criticizing of evidence and theories about past events. Includes instruction in historiography; historical research methods; studies of specific periods, issues and cultures; and applications to areas such as historic preservation, public policy, and records administration."
        ];
  let urls = ["https://study.com/directory/category/Liberal_Arts_and_Humanities/Ethnic_and_Gender_Studies.html#:~:text=Ethnic%20and%20gender%20studies%20are,opportunities%20in%20these%20interdisciplinary%20fields.",
        "https://www.indeed.com/hire/job-description/engineer",
        "https://www.wayup.com/guide/what-is-a-communications-major-and-is-it-right-for-me/#:~:text=A%20communications%20major%20is%20a,public%20relations%2C%20advertising%20and%20journalism.",
        "https://www.bestcolleges.com/careers/law/legal-studies/#:~:text=Legal%20studies%20is%20an%20undergraduate,apart%20from%20being%20a%20lawyer.",
        "https://www.usnews.com/education/best-colleges/english-major-overview",
        "https://www.mymajors.com/college-majors/biology-biological-sciences/",
        "https://www.mymajors.com/college-majors/computer-science/",
        "wayup.com/guide/what-is-an-education-major-and-is-it-right-for-me/#:~:text=An%20education%20major%20is%20designed,the%20skills%20to%20teach%20others.&text=Typical%20classes%20in%20this%20major,education%20and%20public%20policy%20classes.",
        "https://www.usnews.com/education/best-colleges/political-science-major-overview",
        "https://www.aiuniv.edu/degrees/business/articles/majoring-in-business#:~:text=Generally%2C%20business%20degrees%20are%20designed,resources%2C%20operations%20and%20project%20management.",
        "https://www.usnews.com/education/best-colleges/economics-major-overview#:~:text=An%20economics%20major%20examines%20resource,management%2C%20law%20and%20public%20affairs.&text=Majoring%20in%20economics%20can%20provide,methods%2C%20quantitative%20analysis%20and%20more.",
        "https://study.com/articles/Bachelor_of_Nursing_Degree_Overview.html",
        "https://www.mymajors.com/college-majors/finance/",
        "https://www.mymajors.com/college-majors/history/#:~:text=History%20Major-,History%20Major,and%20theories%20about%20past%20events."
      ];
  while(top3.length < 3){
    var tempIndex = 0;
    for(var i = 0 ; i < list1clone.length; i++){
      if(list1clone[i] > list1clone[tempIndex]){
        tempIndex = i;
      }
      if(i == list1clone.length-1){
        top3.push(list2clone[tempIndex]);
        descriptions.push(description[list2.indexOf(list2clone[tempIndex])]);
        urlslist.push(urls[list2.indexOf(list2clone[tempIndex])]);
        list2clone.splice(tempIndex,1);
        list1clone.splice(tempIndex,1);
      }
    }
  }
  finished = true;
var sent;
let listOfMajors = [];
let listOfUrls = [];
let listOfDescriptions = [];

if(top3.length>0){
  listOfMajors.push(top3[0]);
  listOfDescriptions.push(descriptions[0]);
  listOfUrls.push(urlslist[0]);
  $("#togo").val(top3[0]);
  $("#firstPickDescription").val(descriptions[0]);
  $("#firstPickURL").val(urlslist[0]);
}
if(top3.length>1){
  listOfMajors.push(top3[1]);
  listOfDescriptions.push(descriptions[1]);
  listOfUrls.push(urlslist[1]);
  $("#toge").val(top3[1]);
  $("#secondPickDescription").val(descriptions[1]);
  $("#secondPickURL").val(urlslist[1]);


}
if(top3.length>2){
  listOfMajors.push(top3[2]);
  listOfDescriptions.push(descriptions[2]);
  listOfUrls.push(urlslist[2]);
  $("#togl").val(top3[2]);
  $("#thirdPickDescription").val(descriptions[2]);
  $("#thirdPickURL").val(urlslist[2]);
}

arrayToString(listOfMajors, listOfUrls, listOfDescriptions);

  
  if(finished){
    $("#myform").submit();
  }

}

function engineeringSubCategories(){
  let civil = 0;
  let electrical = 0; 
  let chemical = 0;
  let petroleum = 0;
  let environmental = 0;
  let biomedical = 0;
  let computer = 0;
  let nuclear =  0;
  let engineeringlist = [civil, electrical, chemical, environmental, biomedical, computer, nuclear];
  let engineeringlist2 = ["Civil Engineering", "Electrical Engineering", "Chemical Engineering", "Petroleum Engineering", "Environmental Engineering", "Biomedical Engineering", "Computer Engineering", "Nuclear Engineering"];
    
  for(let i=0; i<engineeringlist.length; i++){
    if($("#ques1").val() == engineeringlist2[i]){
      engineeringlist[i]+=1;
    }
    if($("#ques2").val() == engineeringlist2[i]){
      engineeringlist[i]+=1;
    }
    if($("#ques3").val() == engineeringlist2[i]){
      engineeringlist[i]+=1;
    }
    if($("#ques4").val() == engineeringlist2[i]){
      engineeringlist[i]+=1;
    }
    if($("#ques5").val() == engineeringlist2[i]){
      engineeringlist[i]+=1;
    }
    if($("#ques6").val() == engineeringlist2[i]){
      engineeringlist[i]+=1;
    }
    if($("#ques7").val() == engineeringlist2[i]){
      engineeringlist[i]+=1;
    }
    if($("#ques8").val() == engineeringlist2[i]){
      engineeringlist[i]+=1;
    }
    if($("#ques9").val() == engineeringlist2[i]){
      engineeringlist[i]+=1;
    }
    if($("#ques10").val() == engineeringlist2[i]){
      engineeringlist[i]+= 1;
    }
  }
  var top3engineering = [];
  var list2clone = engineeringlist2;
  var list1clone = engineeringlist;
  var max=0;
  var val;
  var value;
  while(top3engineering.length < 3){
    var tempIndex = 0;
    for(var i = 0 ; i < list1clone.length; i++){
      if(list1clone[i] > list1clone[tempIndex]){
        tempIndex = i;
      }
      if(i == list1clone.length-1){
        top3engineering.push(list2clone[tempIndex]);
        list2clone.splice(tempIndex,1);
        list1clone.splice(tempIndex,1);
      }
    }
  }
    list2clone.splice(val,1);
  var sent;
  let listOfMajors = [];
  let listOfUrls = [];
  let listOfDescriptions = [];
  if(top3engineering.length>0){
    listOfMajors.push(top3engineering[0]);
    $("#engineering1").val(top3engineering[0]);
  }
  if(top3engineering.length>1){
    listOfMajors.push(top3engineering[1]);
    $("#engineering2").val(top3engineering[1]);
  }
  if(top3engineering.length>2){
    listOfMajors.push(top3engineering[2]);
    $("#engineering3").val(top3engineering[2]);
  }
  finished = true;
  $("#engineering").val(arrayToString2(top3engineering));

  if(finished){
    $("#myForm").submit();
  }
}

function communicationSubCategories(){

}

function legalSubCategories(){

}

function biologicalSubCategories(){

}

function onLoad(){
  var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    if (isMobile) {
      $("#college").click(function(){
        document.location.href ="/mobile/home";
    });
    }
  $("#submit").click(calc);
  $("#submitengineering").click(engineeringSubCategories);
  if($("#firstmajor").text() == "Engineering"){
    $("#firstmajor").click(function(){
      document.location.href = "/engineeringSubQuestions";
    });
    $("#engineeringbutton").css("display", "block");
  }
  $("#logout").click(function(){

      document.location.href = "/logout";
    
  });
  $("#logout").hover(function(){
    $("#logout").css("cursor", "pointer");
  });
}


window.onload = onLoad
