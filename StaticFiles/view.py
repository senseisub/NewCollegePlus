from django.http import HttpResponse, HttpResponseRedirect, JsonResponse # noqa: 401
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, path
from django.views import generic
from google.cloud import firestore, storage
from django.core.mail import send_mail
from django.conf import settings 
import threading
import random
import datetime
from .models import Upload
from PIL import Image, ImageDraw, ImageFilter
import json
from urllib.parse import unquote
import io

db = firestore.Client()
client = storage.Client()
bucket = client.get_bucket('collegeplus2.appspot.com')
bucket2 = client.get_bucket('private.collegeplus.us')
def arrayToString(arr):
        returningStr = ""
        for element in arr:
                returningStr += element + ","
        return returningStr[0 : len(returningStr)-1]

def device_rec(request):
    if request.method == 'GET':
        user = request.COOKIES.get("CPUSVAL")  
        password = request.COOKIES.get("CPPWVAL")  
        where = db.collection(u'users').where(u'username', u'==', user)
        where2 = where.where(u'password', u'==', password).stream()
        finalObj = None
        template_vars = {}
        for doc in where2:
                
                finalObj = doc.to_dict()
        #user variable holds value of current user
        #if there is user
        if finalObj:
            #nickname variable holds user nickname string
            nickname = finalObj.get("name")
            #template variables to fill in
            template_vars={
                "name": nickname
            }
            #home_template variable get html file
            template_name = 'devicepicker.html'
            return render(request, template_name, template_vars)
        else:
            #template variables to fill in
            template_vars={
                "name": "log in"
            }

        template_name = 'devicepicker.html'
        return render(request, template_name, template_vars)
    else:
        user = request.COOKIES.get("CPUSVAL")  
        password = request.COOKIES.get("CPPWVAL")  
        #variable to hold string values from the inputs in the html pages
        devices= request.POST.get("devices")
        urls = request.POST.get("urls")
        images = request.POST.get("images")
        answers = request.POST.get("answers")
        answersList = answers.split(" ")
        devicesList = returnDeviceSelections2(answersList)
        devices = devicesList["devices"]
        urls = devicesList["url"]
        images = devicesList["image"]
        if devices:
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        nickname = finalObj.get("name")
                        #nickname variable holds user nickname string
                        finalObj = db.collection(u'users').document(user)
                        deviceList = devices.split(",")
                        finalObj.set({
                                u'devices' : deviceList,
                                        
                        },  merge=True)
                        #template variables to fill in
                        template_vars={
                                "devices" : devices,
                                "urls" : arrayToString(urls), 
                                "images" : arrayToString(images),
                                "name": arrayToString(nickname),
                        }
                        #home_template variable get html file
                        template_name = "device_rec.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "devices" : arrayToString(devices),
                                "urls" : arrayToString(urls), 
                                "images" : arrayToString(images),
                                "name": "log in",
                        }
                        #home_template variable get html file
                        template_name = 'device_rec.html'
                        return render(request, template_name, template_vars)
        else:
                return HttpResponseRedirect("/devicepicker")
        template_name = 'LasCrucesNM/LyfeHere/LasCrucesDirectory.html'
        return render(request, template_name)

def login_page(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL") 

                #user variable holds value of current user
                #if there is user
                if user:
                        return HttpResponseRedirect("/save")
                        if user: 
                                #nickname variable holds user nickname string
                                nickname = "Seun"
                        #template variables to fill in
                        template_vars={
                                "name": user
                        }
                        #home_template variable get html file
                        template_name = "index.html"
                        
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #if there is not user, redirect to no user handler
                        return HttpResponseRedirect("/withGoogle")
                        template_name = 'index.html'
                        return render(request, template_name)
                # website_template = the_jinja_env.get_template("golog.html"
                # self.response.write(website_template.render(user))

        else:
                return HttpResponseRedirect("/withGoogle")

def NoUserHandler(request):
        if request.method == "GET":
                return HttpResponseRedirect("/home")
                template_name = 'Map.html'
                return render(request, template_name, {"name" : bigString.get("events")})

def resources(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname
                        }
                        #home_template variable get html file
                        template_name = "resources.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        #home_template variable get html file
                        template_name = "resources.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)

def MainHandler(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname
                        }
                        template_name = 'index.html'
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        template_name = 'index.html'
                        return render(request, template_name, template_vars)
        template_name = 'index.html'
        return render(request, template_name)

def Logout(request):
        response = HttpResponseRedirect('/')
        response.delete_cookie('CPUSVAL')
        response.delete_cookie('CPPWVAL')
        return response

def collegeQ(request):
        if request.method == "GET": 
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname strin
                        #template variables to fill in
                        template_vars={
                                "name": finalObj.get("name")
                        }
                        #home_template variable get html file
                        template_name = "fakewebsite.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        template_name = 'fakewebsite.html'
                        return render(request, template_name, template_vars)
        else:
                colleges = request.POST.get("colleges")
                collegeStates = request.POST.get("collegestates")
                collegeCities = request.POST.get("collegecities")
                collegeTemperatures = request.POST.get("collegetemperatures")
                collegeWeather = request.POST.get("collegeweather")
                collegeLinks = request.POST.get("collegelinks")
                collegeACTs = request.POST.get("collegeact")
                collegeSATReading = request.POST.get("collegesatreading")
                collegeSATMath = request.POST.get("collegesatmath")
                collegecost = request.POST.get("collegecost")
                collegeBlackPop = request.POST.get("collegeblackpop")
                collegeWhitePop = request.POST.get("collegewhitepop")
                collegeAsianPop = request.POST.get("collegeasianpop")
                collegeHispanicPop = request.POST.get("collegehispanicpop")
                collegePrices = request.POST.get("collegecost")
                collegePriceCalculator = request.POST.get("collegepricecalculator")
                collegeNicheURL = request.POST.get("collegenicheurl")
                userACT = request.POST.get("useract")
                userSAT = request.POST.get("usersat")
                userCity = request.POST.get("cityOfUser")
                userState = request.POST.get("stateOfUser")
                houseHoldIncome = request.POST.get("houseHoldIncome")
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                
                if colleges:
                        #user variable holds value of current user
                        # user = "Seun"
                        where = db.collection(u'users').where(u'username', u'==', user)
                        where2 = where.where(u'password', u'==', password).stream()
                        finalObj = None
                        template_vars = {}
                        for doc in where2:
                                
                                finalObj = doc.to_dict()
                        #user variable holds value of current user
                        #if there is user
                        if finalObj:
                                nickname =  finalObj.get("name")   
                                finalObj = db.collection(u'users').document(user)
                                #nickname variable holds user nickname string
                                #sets incrementor to 0
                                i=0
                                #while there are more objects in the datastore with the same nickname
                                collegesList = colleges.split(',')
                                collegeStatesList= collegeStates.split(',')
                                collegeCitiesList = collegeCities.split(',')
                                collegeTemperaturesList = collegeTemperatures.split(',')
                                collegeWeatherList = collegeWeather.split(',')
                                collegeACTList = collegeACTs.split(',')
                                collegeSATReadingList = collegeSATReading.split(',')
                                collegeSATMathList = collegeSATMath.split(',')
                                collegeBlackPopList = collegeBlackPop.split(',')
                                collegeWhitePopList = collegeWhitePop.split(',')
                                collegeAsianPopList = collegeAsianPop.split(',')
                                collegeHispanicPopList = collegeHispanicPop.split(',')
                                collegeLinksList = collegeLinks.split(',')
                                collegePricesList = collegePrices.split(',')
                                collegeNicheURLList = collegeNicheURL.split(',')
                                collegePriceCalculatorList = collegePriceCalculator.split(',')
                                finalObj.set({
                                        u'colleges' : collegesList,
                                        u'collegeLinks' : collegeLinksList,
                                        u'collegeCities' : collegeCitiesList,
                                        u'collegeStates' : collegeStatesList,
                                        u'collegeTemperatures' : collegeTemperaturesList,
                                        u'collegeWeather' : collegeWeatherList,
                                        u'userACT' : userACT,
                                        u'userSAT' : userSAT,
                                        u'userCity' : userCity,
                                        u'userState' : userState ,
                                        u'houseHoldIncome' : houseHoldIncome
                                        
                                },  merge=True)
                                #creates new object and sets variables
                                #template variables to fill in
                                template_vars={
                                        "colleges" : colleges,
                                        "collegeStates" : collegeStates,
                                        "collegeLinks" : collegeLinks,
                                        "collegeWeather" : collegeWeather,
                                        "collegeCities" : collegeCities,
                                        "collegeACTS" : collegeACTs,
                                        "collegeSATMath" : collegeSATMath,
                                        "collegeSATReading" : collegeSATReading,
                                        "collegePrices" : collegePrices,
                                        "collegePriceCalculators" : collegePriceCalculator,
                                        "collegeNiche" : collegeNicheURL,
                                        "collegeTemperature" : collegeTemperatures,
                                        "blackPop" : collegeBlackPop,
                                        "whitePop" : collegeWhitePop,
                                        "asianPop" : collegeAsianPop,
                                        "hispanicPop" : collegeHispanicPop,
                                        "name": nickname


                                }
                                #home_template variable get html file
                                template_name = "college_rec.html"
                                #writes to the webpage file
                                return render(request, template_name, template_vars)

                        else:
                                template_vars={
                                        "colleges" : colleges,
                                        "collegeStates" : collegeStates,
                                        "collegeLinks" : collegeLinks,
                                        "collegeWeather" : collegeWeather,
                                        "collegeCities" : collegeCities,
                                        "collegeACTS" : collegeACTs,
                                        "collegeSATMath" : collegeSATMath,
                                        "collegeSATReading" : collegeSATReading,
                                        "collegePrices" : collegePrices,
                                        "collegePriceCalculators" : collegePriceCalculator,
                                        "collegeNiche" : collegeNicheURL,
                                        "collegeTemperature" : collegeTemperatures,
                                        "blackPop" : collegeBlackPop,
                                        "whitePop" : collegeWhitePop,
                                        "asianPop" : collegeAsianPop,
                                        "hispanicPop" : collegeHispanicPop,
                                        "name": "log in"

                                }
                                #home_template variable get html file
                                template_name = "college_rec.html"
                                #writes to the webpage file
                                return render(request, template_name, template_vars)
                else:
                        self.redirect("/college_questions")
def updateTemplateVars(template_vars, inputString, list):
        place = 1
        template_vars.update({inputString : list})


def updateTemplateVars2(template_vars, inputString, list, collegesList):
        place = 1
        template_vars.update({inputString : list})
        
def saver(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        majors = finalObj.get("majors")
                        updateTemplateVars(template_vars, "majors", majors)
                        colleges = finalObj.get("colleges")
                        updateTemplateVars(template_vars, "colleges", colleges)
                        collegeCities = finalObj.get("collegeCities")
                        updateTemplateVars(template_vars, "collegeCities", collegeCities)
                        collegeStates = finalObj.get("collegeStates")
                        updateTemplateVars2(template_vars, "collegeStates", collegeStates, colleges)
                        collegeTemperatures = finalObj.get("collegeTemperatures")
                        updateTemplateVars2(template_vars, "collegeTemperatures", collegeTemperatures, colleges)
                        collegeWeather = finalObj.get("collegeWeather")
                        updateTemplateVars2(template_vars, "collegeWeather", collegeWeather, colleges)
                        collegeLinks = finalObj.get("collegeLinks")
                        updateTemplateVars2(template_vars, "collegeLinks", collegeLinks, colleges)
                        devices = finalObj.get("laptops")
                        updateTemplateVars(template_vars, "devices", devices)
                        template_vars.update({"usersat" : finalObj.get("userSAT")})
                        template_vars.update({"useract" : finalObj.get("userACT")})
                        template_vars.update({"gpa" : finalObj.get("GPA")})
                        template_vars.update({"usercity" : finalObj.get("userCity")})
                        template_vars.update({"userState" : finalObj.get("userState")})
                        template_vars.update({"name" : finalObj.get("name")})
                        template_vars["totalInfo"] = json.dumps({
                                "main" : {
                                        "majors" : finalObj.get("majors"),
                                        "devices" : finalObj.get("devices"),
                                        "colleges" : finalObj.get("colleges"),
                                        "collegeLinks" : finalObj.get("collegeLinks"),
                                        "collegeWeather" : finalObj.get("collegeWeather"),
                                        "collegeTemperatures" : finalObj.get("collegeTemperatures"),
                                        "collegeStates" : finalObj.get("collegeStates"),
                                        "collegeCities" : finalObj.get("collegeCities")
                                }
                        })
                        if finalObj.get("imageUrl"):
                               template_vars.update({"imageUrl" : "https://storage.googleapis.com/collegeplus2.appspot.com"+finalObj.get("imageUrl")}) 
                        template_name = "profile.html"
                        template_vars["items"] = json.dumps({"main" : finalObj.get("listings") if finalObj.get("listings") else []})
                        # writes to the webpage file
                        return render(request, template_name, template_vars)
                        return HttpResponseRedirect("/home")
              
                else:
                        return HttpResponseRedirect("/withGoogle")
        elif request.method == 'POST':
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                newName = request.POST.get("newName")
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        finalObj = db.collection(u'users').document(user)
                        finalObj.set({
                                u'name' : newName
                                        
                        },  merge=True)
                return HttpResponseRedirect("/save")
                # avatar = request.POST.get('img')
                # avatar = images.resize(avatar, 32, 32)
                # ourUser = request.COOKIES.get("CPUSVAL")
                # #user variable holds value of current user
                # user = "Seun"
                # if user:
                #         #nickname variable holds user nickname string
                #         nickname = "Seun"
                #         userinfo.query().filter(userinfo.namer==nickname).fetch()[0].avatar = avatar
                #         userinfo.query().filter(userinfo.namer==nickname).fetch()[0].put()
                #         self.redirect("/save")
                # elif ourUser != None:
                #         userinfo.query().filter(userinfo.namer==ourUser).fetch()[0].avatar = avatar
                #         userinfo.query().filter(userinfo.namer==ourUser).fetch()[0].put()
                #         self.redirect("/save")
                return HttpResponseRedirect("/home")
def degree(request):
        if request.method == "GET":
                        user = request.COOKIES.get("CPUSVAL")
                        password = request.COOKIES.get("CPPWVAL")
                        where = db.collection(u'users').where(u'username', u'==', user)
                        where2 = where.where(u'password', u'==', password).stream()
                        finalObj = None
                        template_vars = {}
                        for doc in where2:
                                
                                finalObj = doc.to_dict()
                        if finalObj:
                                #nickname variable holds user nickname string
                                nickname = finalObj.get("name")
                                #template variables to fill in
                                template_vars={
                                        "name": nickname
                                }
                                #home_template variable get html file
                                template_name = "degree_questions.html"
                                return render(request, template_name, template_vars)
                        else:
                                #template variables to fill in
                                template_vars={
                                        "name": "log in"
                                }
                                #home_template variable get html file
                                template_name = "degree_questions.html"
                                #writes to the webpage file
                                return render(request, template_name, template_vars)
                        template_name = 'LasCrucesNM/TheRange/LasCrucesTheRange.html'
                        return render(request, template_name)
        else:
                #variable stores majors from website template 
                majors = request.POST.get("majors")
                majorLinks = request.POST.get("majorLinks")
                majorDescriptions = request.POST.get("descriptions")

                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")

                #user variable holds value of current user
                # user = "Seun"
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        nickname = finalObj.get("name") 
                        finalObj = db.collection(u'users').document(user)
                        majorList = majors.split(",")
                        finalObj.set({
                                u'majors' : majorList,
                                        
                        },  merge=True)
                        #nickname variable holds user nickname string
                        #sets incrementor to 0
                        i=0
                        #while there are more objects in the datastore with the same nickname
                
                        #template variables to fill in
                        template_vars={
                                "majors" : majors,
                                "majorLinks" : majorLinks,
                                "majorDescriptions" : majorDescriptions,
                                "name": nickname,
                        }
                        #home_template variable get html file
                        template_name = "degree_rec.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "majors" : majors,
                                "majorLinks" : majorLinks,
                                "majorDescriptions" : majorDescriptions,
                                "name": "log in",
                        }
                        #home_template variable get html file
                        template_name = "degree_rec.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                

def knowdegree(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname
                        }
                        #home_template variable get html file
                        template_name = "knowdegree.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        #home_template variable get html file
                        template_name = "knowdegree.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
        template_name = 'LasCrucesNM/TheRange/mLasCrucesTheRange.html'
        return render(request, template_name)

def knowdevice(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname
                        }
                        #home_template variable get html file
                        template_name = "knowdevice.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        #home_template variable get html file
                        template_name = "knowdevice.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)

def knowcollege(request):
        if request.method  == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname
                        }
                        #home_template variable get html file
                        template_name = "knowcollege.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        #home_template variable get html file
                        template_name = "knowcollege.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)

def mobileMain(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "iconcolor" : "tomato"
                        }
                        template_name = 'mindex.html'
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        template_name = 'mindex.html'
                        return render(request, template_name, template_vars)
        template_name = 'mindex.html'
        return render(request, template_name)
def mobileKnowdegree(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "iconcolor" : "tomato"
                        }
                        #home_template variable get html file
                        template_name = "mknowdegree.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        #home_template variable get html file
                        template_name = "mknowdegree.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)

def mobileKnowcollege(request):
        if request.method  == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "iconcolor" : "tomato"
                        }
                        #home_template variable get html file
                        template_name = "mknowcollege.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        #home_template variable get html file
                        template_name = "mknowcollege.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)

def mobileknowdevice(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "iconcolor" : "tomato"
                        }
                        #home_template variable get html file
                        template_name = "mknowdevice.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        #home_template variable get html file
                        template_name = "mknowdevice.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
def mobileCollegeQ(request):
        if request.method == "GET": 
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname strin
                        #template variables to fill in
                        template_vars={
                                "name": finalObj.get("name"),
                                "iconcolor" : "tomato"
                        }
                        #home_template variable get html file
                        template_name = "mfakewebsite.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        template_name = 'mfakewebsite.html'
                        return render(request, template_name, template_vars)
        else:
                colleges = request.POST.get("colleges")
                collegeStates = request.POST.get("collegestates")
                collegeCities = request.POST.get("collegecities")
                collegeTemperatures = request.POST.get("collegetemperatures")
                collegeWeather = request.POST.get("collegeweather")
                collegeLinks = request.POST.get("collegelinks")
                collegeACTs = request.POST.get("collegeact")
                collegeSATReading = request.POST.get("collegesatreading")
                collegeSATMath = request.POST.get("collegesatmath")
                collegecost = request.POST.get("collegecost")
                collegeBlackPop = request.POST.get("collegeblackpop")
                collegeWhitePop = request.POST.get("collegewhitepop")
                collegeAsianPop = request.POST.get("collegeasianpop")
                collegeHispanicPop = request.POST.get("collegehispanicpop")
                collegePrices = request.POST.get("collegecost")
                collegePriceCalculator = request.POST.get("collegepricecalculator")
                collegeNicheURL = request.POST.get("collegenicheurl")
                userACT = request.POST.get("useract")
                userSAT = request.POST.get("usersat")
                userCity = request.POST.get("cityOfUser")
                userState = request.POST.get("stateOfUser")
                houseHoldIncome = request.POST.get("houseHoldIncome")
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                
                if colleges:
                        #user variable holds value of current user
                        # user = "Seun"
                        where = db.collection(u'users').where(u'username', u'==', user)
                        where2 = where.where(u'password', u'==', password).stream()
                        finalObj = None
                        template_vars = {}
                        for doc in where2:
                                
                                finalObj = doc.to_dict()
                        #user variable holds value of current user
                        #if there is user
                        if finalObj:
                                nickname =  finalObj.get("name")   
                                finalObj = db.collection(u'users').document(user)
                                #nickname variable holds user nickname string
                                #while there are more objects in the datastore with the same nickname
                                collegesList = colleges.split(',')
                                collegeStatesList= collegeStates.split(',')
                                collegeCitiesList = collegeCities.split(',')
                                collegeTemperaturesList = collegeTemperatures.split(',')
                                collegeWeatherList = collegeWeather.split(',')
                                collegeACTList = collegeACTs.split(',')
                                collegeSATReadingList = collegeSATReading.split(',')
                                collegeSATMathList = collegeSATMath.split(',')
                                collegeBlackPopList = collegeBlackPop.split(',')
                                collegeWhitePopList = collegeWhitePop.split(',')
                                collegeAsianPopList = collegeAsianPop.split(',')
                                collegeHispanicPopList = collegeHispanicPop.split(',')
                                collegeLinksList = collegeLinks.split(',')
                                collegePricesList = collegePrices.split(',')
                                collegeNicheURLList = collegeNicheURL.split(',')
                                collegePriceCalculatorList = collegePriceCalculator.split(',')
                                finalObj.set({
                                        u'colleges' : collegesList,
                                        u'collegeLinks' : collegeLinksList,
                                        u'collegeCities' : collegeCitiesList,
                                        u'collegeStates' : collegeStatesList,
                                        u'collegeTemperatures' : collegeTemperaturesList,
                                        u'collegeWeather' : collegeWeatherList,
                                        u'userACT' : userACT,
                                        u'userSAT' : userSAT,
                                        u'userCity' : userCity,
                                        u'userState' : userState ,
                                        u'houseHoldIncome' : houseHoldIncome
                                        
                                },  merge=True)
                                #creates new object and sets variables
                                #template variables to fill in
                                template_vars={
                                        "colleges" : colleges,
                                        "collegeStates" : collegeStates,
                                        "collegeLinks" : collegeLinks,
                                        "collegeWeather" : collegeWeather,
                                        "collegeCities" : collegeCities,
                                        "collegeACTS" : collegeACTs,
                                        "collegeSATMath" : collegeSATMath,
                                        "collegeSATReading" : collegeSATReading,
                                        "collegePrices" : collegePrices,
                                        "collegePriceCalculators" : collegePriceCalculator,
                                        "collegeNiche" : collegeNicheURL,
                                        "collegeTemperature" : collegeTemperatures,
                                        "blackPop" : collegeBlackPop,
                                        "whitePop" : collegeWhitePop,
                                        "asianPop" : collegeAsianPop,
                                        "hispanicPop" : collegeHispanicPop,
                                        "name": nickname,
                                        "iconcolor" : "tomato"


                                }
                                #home_template variable get html file
                                template_name = "mcollege_rec.html"
                                #writes to the webpage file
                                return render(request, template_name, template_vars)

                        else:
                                template_vars={
                                        "colleges" : colleges,
                                        "collegeStates" : collegeStates,
                                        "collegeLinks" : collegeLinks,
                                        "collegeWeather" : collegeWeather,
                                        "collegeCities" : collegeCities,
                                        "collegeACTS" : collegeACTs,
                                        "collegeSATMath" : collegeSATMath,
                                        "collegeSATReading" : collegeSATReading,
                                        "collegePrices" : collegePrices,
                                        "collegePriceCalculators" : collegePriceCalculator,
                                        "collegeNiche" : collegeNicheURL,
                                        "collegeTemperature" : collegeTemperatures,
                                        "blackPop" : collegeBlackPop,
                                        "whitePop" : collegeWhitePop,
                                        "asianPop" : collegeAsianPop,
                                        "hispanicPop" : collegeHispanicPop,
                                        "name": "log in"

                                }
                                #home_template variable get html file
                                template_name = "mcollege_rec.html"
                                #writes to the webpage file
                                return render(request, template_name, template_vars)
                else:
                        return HttpResponseRedirect("/mobile/college_questions")

def mobileDegree(request):
        if request.method == "GET":
                        user = request.COOKIES.get("CPUSVAL")
                        password = request.COOKIES.get("CPPWVAL")
                        where = db.collection(u'users').where(u'username', u'==', user)
                        where2 = where.where(u'password', u'==', password).stream()
                        finalObj = None
                        template_vars = {}
                        for doc in where2:
                                
                                finalObj = doc.to_dict()
                        if finalObj:
                                #nickname variable holds user nickname string
                                nickname = finalObj.get("name")
                                #template variables to fill in
                                template_vars={
                                        "name": nickname,
                                        "iconcolor" : "tomato"
                                }
                                #home_template variable get html file
                                template_name = "mdegree_questions.html"
                                return render(request, template_name, template_vars)
                        else:
                                #template variables to fill in
                                template_vars={
                                        "name": "log in"
                                }
                                #home_template variable get html file
                                template_name = "mdegree_questions.html"
                                #writes to the webpage file
                                return render(request, template_name, template_vars)
        else:
                #variable stores majors from website template 
                majors = request.POST.get("majors")
                majorLinks = request.POST.get("majorLinks")
                majorDescriptions = request.POST.get("descriptions")
                
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")

                #user variable holds value of current user
                # user = "Seun"
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        nickname = finalObj.get("name") 
                        finalObj = db.collection(u'users').document(user)
                        majorList = majors.split(",")
                        finalObj.set({
                                u'majors' : majorList,
                                        
                        },  merge=True)
                        #nickname variable holds user nickname string
                        #sets incrementor to 0
                        i=0
                        #while there are more objects in the datastore with the same nickname
                
                        #template variables to fill in
                        template_vars={
                                "majors" : majors,
                                "majorLinks" : majorLinks,
                                "majorDescriptions" : majorDescriptions,
                                "name": nickname,
                                "iconcolor" : "tomato"
                        }
                        #home_template variable get html file
                        template_name = "mdegree_rec.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "majors" : majors,
                                "majorLinks" : majorLinks,
                                "majorDescriptions" : majorDescriptions,
                                "name": "log in",
                        }
                        #home_template variable get html file
                        template_name = "mdegree_rec.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)


def mobileabout(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                #variable to hold string values from the inputs in the html pages
                devices= request.POST.get("devices")
                urls = request.POST.get("urls")
                images = request.POST.get("images")

                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        nickname = finalObj.get("name")
                        #nickname variable holds user nickname string
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "iconcolor" : "tomato"
                        }
                        #home_template variable get html file
                        template_name = "mabout.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in",
                                "iconcolor" : "#232323"
                        }
                        #home_template variable get html file
                        template_name = "mabout.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
        template_name = 'Map.html'
        return render(request, template_name)

def mobileDevicepicker(request):
        if request.method == 'GET':
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "iconcolor" : "tomato"
                        }
                        #home_template variable get html file
                        template_name = 'mdevicepicker.html'
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }

                        template_name = 'mdevicepicker.html'
                        return render(request, template_name, template_vars)
        else:
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                #variable to hold string values from the inputs in the html pages
                devices= request.POST.get("devices")
                urls = request.POST.get("urls")
                images = request.POST.get("images")

                if devices:
                        where = db.collection(u'users').where(u'username', u'==', user)
                        where2 = where.where(u'password', u'==', password).stream()
                        finalObj = None
                        template_vars = {}
                        for doc in where2:
                                
                                finalObj = doc.to_dict()
                        #user variable holds value of current user
                        #if there is user
                        if finalObj:
                                nickname = finalObj.get("name")
                                #nickname variable holds user nickname string
                                finalObj = db.collection(u'users').document(user)
                                deviceList = devices.split(",")
                                finalObj.set({
                                        u'devices' : deviceList,
                                                
                                },  merge=True)
                                #template variables to fill in
                                template_vars={
                                        "devices" : devices,
                                        "urls" : urls, 
                                        "images" : images,
                                        "name": nickname,
                                        "iconcolor" : "tomato"
                                }
                                #home_template variable get html file
                                template_name = "mdevice_rec.html"
                                #writes to the webpage file
                                return render(request, template_name, template_vars)
                        else:
                                #template variables to fill in
                                template_vars={
                                        "devices" : devices,
                                        "urls" : urls, 
                                        "images" : images,
                                        "name": "log in",
                                }
                                #home_template variable get html file
                                template_name = 'mdevice_rec.html'
                                return render(request, template_name, template_vars)
                else:
                        return HttpResponseRedirect("/mobile/devicepicker")



def mobileResources(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname
                        }
                        #home_template variable get html file
                        template_name = "mresources.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in"
                        }
                        #home_template variable get html file
                        template_name = "mresources.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)

def mobileLogin(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL") 

                #user variable holds value of current user
                #if there is user
                if user:
                        return HttpResponseRedirect("/mobile/save")
                        if user: 
                                #nickname variable holds user nickname string
                                nickname = "Seun"
                        #template variables to fill in
                        template_vars={
                                "name": user
                        }
                        #home_template variable get html file
                        template_name = "mindex.html"
                        
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #if there is not user, redirect to no user handler
                        return HttpResponseRedirect("/mobile/withGoogle")
                        template_name = 'mindex.html'
                        return render(request, template_name)
                # website_template = the_jinja_env.get_template("golog.html"
                # self.response.write(website_template.render(user))

        else:
                return HttpResponseRedirect("/withGoogle")

def mobileNoUserHandler(request):
        template_name = 'LasCrucesNM/SoGlam/SoGlam.html'
        return render(request, template_name)

def mobileSaver(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        majors = finalObj.get("majors")
                        updateTemplateVars(template_vars, "majors", majors)
                        colleges = finalObj.get("colleges")
                        updateTemplateVars(template_vars, "colleges", colleges)
                        collegeCities = finalObj.get("collegeCities")
                        updateTemplateVars(template_vars, "collegeCities", collegeCities)
                        collegeStates = finalObj.get("collegeStates")
                        updateTemplateVars2(template_vars, "collegeStates", collegeStates, colleges)
                        collegeTemperatures = finalObj.get("collegeTemperatures")
                        updateTemplateVars2(template_vars, "collegeTemperatures", collegeTemperatures, colleges)
                        collegeWeather = finalObj.get("collegeWeather")
                        updateTemplateVars2(template_vars, "collegeWeather", collegeWeather, colleges)
                        collegeLinks = finalObj.get("collegeLinks")
                        updateTemplateVars2(template_vars, "collegeLinks", collegeLinks, colleges)
                        devices = finalObj.get("laptops")
                        updateTemplateVars(template_vars, "devices", devices)
                        template_vars.update({"usersat" : finalObj.get("userSAT")})
                        template_vars.update({"useract" : finalObj.get("userACT")})
                        template_vars.update({"gpa" : finalObj.get("GPA")})
                        template_vars.update({"usercity" : finalObj.get("userCity")})
                        template_vars.update({"userState" : finalObj.get("userState")})
                        template_vars.update({"name" : finalObj.get("name")})
                        template_vars.update({"iconcolor" : "tomato"})
                        if finalObj.get("imageUrl"):
                               template_vars.update({"profileImage" : "https://storage.googleapis.com/collegeplus2.appspot.com"+finalObj.get("imageUrl")}) 
                        template_name = "mprofile.html"
                        # writes to the webpage file
                        return render(request, template_name, template_vars)
                        return HttpResponseRedirect("/home")
              
                else:
                        return HttpResponseRedirect("/mobile/withGoogle")
        elif request.method == 'POST':
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                newName = request.POST.get("newName")
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        finalObj = db.collection(u'users').document(user)
                        finalObj.set({
                                u'name' : newName
                                        
                        },  merge=True)
                return HttpResponseRedirect("/mobile/save")
                # avatar = request.POST.get('img')
                # avatar = images.resize(avatar, 32, 32)
                # ourUser = request.COOKIES.get("CPUSVAL")
                # #user variable holds value of current user
                # user = "Seun"
                # if user:
                #         #nickname variable holds user nickname string
                #         nickname = "Seun"
                #         userinfo.query().filter(userinfo.namer==nickname).fetch()[0].avatar = avatar
                #         userinfo.query().filter(userinfo.namer==nickname).fetch()[0].put()
                #         self.redirect("/save")
                # elif ourUser != None:
                #         userinfo.query().filter(userinfo.namer==ourUser).fetch()[0].avatar = avatar
                #         userinfo.query().filter(userinfo.namer==ourUser).fetch()[0].put()
                #         self.redirect("/save")
                return HttpResponseRedirect("/home")

def mobileLogout(request):
        response = HttpResponseRedirect('/mobile/')
        response.delete_cookie('CPUSVAL')
        response.delete_cookie('CPPWVAL')
        return response

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))
def test(request):
        user = request.COOKIES.get("CPUSVAL")  
        password = request.COOKIES.get("CPPWVAL")  
        userObj = db.collection(u'users').document(user).get().to_dict()
        if userObj:
                userObj = userObj if userObj.get("password") == password else None  
        if userObj:
                if request.method == "GET":
                        if not userObj.get("messages"):
                                userObjCpy = db.collection(u'users').document(user)
                                userObjCpy.set({
                                        "messages" : {"name" : userObj.get("name")}
                                }, merge = True)
                        template_name = "sellingPage.html"
                        return render(request, 'test.html', { "messages" : json.dumps(userObj.get("messages")), "username" : user}) 
                else:
                        image1 = processImage(request.POST.get("listingImage1"))
                        image2 = processImage(request.POST.get("listingImage2"))
                        image3 = processImage(request.POST.get("listingImage3"))
                        image4 = processImage(request.POST.get("listingImage4"))

                        data = {
                                "author" : request.POST.get("person"),
                                "host" : user,
                                "listing" : request.POST.get("listing"),
                                "description" : request.POST.get("description"),
                                "price" : request.POST.get("price"),
                                "images" : [image1, image2, image3, image4]
                        }
                        
                        collegeData.get("items").append(data)
                        collegeDataCpy = db.collection(u'colleges').document(college)
                        collegeDataCpy.set({
                                "items" : collegeData.get("items")
                        }, merge = True)
                        if userObj.get("collegeAttended") == college:
                                if len(userObj.get("listings")) < 5:
                                        userObj.get("listings").append(data)
                                        userObjCpy = db.collection(u'users').document(user)
                                        userObjCpy.set({
                                                "listings" : userObj.get("listings")
                                        }, merge = True)
                        return HttpResponseRedirect("../sold")
        else:
                return HttpResponseRedirect("../login")

def engineeringSubQuestions(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                        }
                        #home_template variable get html file
                        template_name = "engineeringSubCatergories.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in",
                                "iconcolor" : "#232323"
                        }
                        #home_template variable get html file
                        template_name = "engineeringSubCatergories.html"
                        return render(request, template_name, template_vars)
                template_name = 'LasCrucesNM/Maxx Designs for VIP\'s/maxx.html'
                return render(request, template_name)
        else:
                #variables that hold what is returned from the template
                majors= request.POST.get("engineering")
                #user variable holds value of current user
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.name("name")
                        #sets incrementor to 0
                        nickname = finalObj.get("name") 
                        finalObj = db.collection(u'users').document(user)
                        majorList = majors.split(",")
                        finalObj.set({
                                u'majors' : majorList,
                                        
                        },  merge=True)
                        #nickname variable holds user nickname string

                        #template variables to fill in
                        template_vars={
                                "majors" : majors,
                                "name": nickname,
                        }
                        #home_template variable get html file
                        template_name = "engineeringSubCategoriesResults.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)

                else:
                    #template variables to fill in
                    template_vars={
                        "majors" : majors,
                        "name": "log in",
                    }
                    #home_template variable get html file
                    template_name = "engineeringSubCategoriesResults.html"
                    #writes to the webpage file
                    return render(request, template_name, template_vars)

def about(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
                #variable to hold string values from the inputs in the html pages
                devices= request.POST.get("devices")
                urls = request.POST.get("urls")
                images = request.POST.get("images")

                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        nickname = finalObj.get("name")
                        #nickname variable holds user nickname string
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "iconcolor" : "tomato"
                        }
                        #home_template variable get html file
                        template_name = "about.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in",
                                "iconcolor" : "#232323"
                        }
                        #home_template variable get html file
                        template_name = "about.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
        template_name = 'Map.html'
        return render(request, template_name)

def mobileEngineeringSubQuestions(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "iconcolor" : "tomato"
                        }
                        #home_template variable get html file
                        template_name = "mengineeringSubCategories.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in",
                                "iconcolor" : "#232323"
                        }
                        #home_template variable get html file
                        template_name = "mengineeringSubCategories.html"
                        return render(request, template_name, template_vars)
                
        else:
                #variables that hold what is returned from the template
                majors= request.POST.get("engineering")
                #user variable holds value of current user
                user = request.COOKIES.get("CPUSVAL")
                password = request.COOKIES.get("CPPWVAL")
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #sets incrementor to 0
                        nickname = finalObj.get("name") 
                        finalObj = db.collection(u'users').document(user)
                        majorList = majors.split(",")
                        finalObj.set({
                                u'majors' : majorList,
                                        
                        },  merge=True)
                        #nickname variable holds user nickname string

                        #template variables to fill in
                        template_vars={
                                "majors" : majors,
                                "name": nickname,
                                "iconcolor" : "tomato"
                        }
                        #home_template variable get html file
                        template_name = "mengineeringSubCategoriesResults.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)

                else:
                    #template variables to fill in
                    template_vars={
                        "majors" : majors,
                        "name": "log in",
                    }
                    #home_template variable get html file
                    template_name = "mengineeringSubCategoriesResults.html"
                    #writes to the webpage file
                    return render(request, template_name, template_vars)
# def mobileEngineeringSubQuestions(request):
#         template_name = 'LasCrucesNM/Maxx Designs for VIP\'s/maxx.html'
#         return render(request, template_name)

def gpaCalculator(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
               
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "logged": "none",
                                "notlogged" : "none",
                        
                        }
                        #home_template variable get html file
                        template_name = "gpaCalculator.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in",
                                "logged": "none",
                                "notlogged" : "none",
                        
                        }
                        #home_template variable get html file
                        template_name = "gpaCalculator.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
        else: 
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
               
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        gpa = request.POST.get("gpaholder")
                        nickname = finalObj.get("name")
                        finalObj = db.collection(u'users').document(user)
                        finalObj.set({
                                u'GPA' : gpa,
                                        
                        },  merge=True)
                        #template variables to fill in
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "logged": "block",
                                "notlogged" : "none",
                        
                        }
                        #home_template variable get html file
                        template_name = "gpaCalculator.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in",
                                "logged": "none",
                                "notlogged" : "block",
                        
                        }
                        #home_template variable get html file
                        template_name = "gpaCalculator.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)

def mobileGPACalculator(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
               
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        #nickname variable holds user nickname string
                        nickname = finalObj.get("name")
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "logged": "none",
                                "notlogged" : "none",
                                "iconcolor" : "tomato"
                        
                        }
                        #home_template variable get html file
                        template_name = "mgpaCalculator.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in",
                                "logged": "none",
                                "notlogged" : "none",
                        
                        }
                        #home_template variable get html file
                        template_name = "mgpaCalculator.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
        else: 
                user = request.COOKIES.get("CPUSVAL")  
                password = request.COOKIES.get("CPPWVAL")  
               
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                #user variable holds value of current user
                #if there is user
                if finalObj:
                        gpa = request.POST.get("gpaholder")
                        nickname = finalObj.get("name")
                        finalObj = db.collection(u'users').document(user)
                        finalObj.set({
                                u'GPA' : gpa,
                                        
                        },  merge=True)
                        #template variables to fill in
                        #template variables to fill in
                        template_vars={
                                "name": nickname,
                                "logged": "block",
                                "notlogged" : "none",
                                "iconcolor" : "tomato"
                        
                        }
                        #home_template variable get html file
                        template_name = "mgpaCalculator.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        #template variables to fill in
                        template_vars={
                                "name": "log in",
                                "logged": "none",
                                "notlogged" : "block",
                        
                        }
                        #home_template variable get html file
                        template_name = "mgpaCalculator.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)

def Ads(request):
        template_name = 'LasCrucesNM/Maxx Designs for VIP\'s/maxx.html'
        return render(request, template_name)

def SSLActivation(request):
        template_name = 'Map.html'
        return render(request, template_name)

def withGoogle(request):
        if request.method == "GET":
                #home_template variable get html file
                template_name = "signInGoogle.html"
                #writes to the webpage file
                return render(request, template_name)
        else:
                user = request.POST.get("username")
                password = request.POST.get("password")
                google = False
                if not user:
                        google = True
                        user = request.POST.get("googleUsername")
                        password = "google"
                nickname = user[0: user.index('@')]
                user = cipher(user)
                password = cipher(password)
                where = db.collection(u'users').where(u'username', u'==', user)
                
                
                finalObj = None
                template_vars = {}
                for doc in where:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        template_vars={
                                "name" : "You already have an account with us"
                        }
                        #home_template variable get html file
                        template_name = "signInGoogle.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        finalObj = db.collection(u'users').document(user)
                        t1 = threading.Thread(target=createCookies, args=(user, password))
                        t1.start()
                        finalObj.set({
                                u'username' : user,
                                u'password' : password,
                                u'majors' : [],
                                u'colleges' : [],
                                u'collegeLinks' : [],
                                u'collegeStates' : [],
                                u'devices' : [],
                                u'collegeCities' : [],
                                u'name' : nickname,
                                u'GPA' : 0,
                                u'userACT' : 0,
                                u'userSAT' : 0,
                                u'userCity' : "someWhere",
                                u'userState' : "whoKnows",
                                u'imageUrl' : "",
                                u'listings' : [],
                                u'messages' : {}
                                
                        },  merge=True)
                        template_vars={
                                "name" : "Your account has been created!"
                        }
                        
                        template_name = "signInGoogle.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
        template_name = 'LasCrucesNM/SoGlam/mSoGlam.html'
        return render(request, template_name)

def createCookies(user, password):
        response = HttpResponseRedirect("/home")
        set_cookie(response, "CPUSVAL", user)
        set_cookie(response, "CPPWVAL", password)
        return response

def loginBoth(request):
        if request.method == "GET":
                #home_template variable get html file
                template_name = "loginBothOptions.html"
                #writes to the webpage file
                return render(request, template_name)
        else:
                user = request.POST.get("username")
                password = request.POST.get("password")
                image = ""
                google = False
                if not user:
                        google = True
                        user = request.POST.get("googleUsername")
                        password = "google"
                        image = request.POST.get("googleImage")
                user = cipher(user)
                password = cipher(password)
                where = db.collection(u'users').where(u'username', u'==', user)
                
                userObj = None
                for doc in where.stream():
                        
                        userObj = doc.to_dict()
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        response = HttpResponseRedirect("/home")
                        set_cookie(response, "CPUSVAL", user)
                        set_cookie(response, "CPPWVAL", password)
                        finalObj = db.collection(u'users').document(user)
                        # response.set_cookie("username", value=user, max_age=(24*60*60), path='/', domain="http://127.0.0.1:8000/")
                        # response.set_cookie("password", value=password, max_age=(24*60*60), path='/', domain="http://127.0.0.1:8000/")
                        return response
                elif userObj and not finalObj:
                        template_vars = {
                                "name" : "Either the username or password is wrong"
                        }
                        if google:
                               template_vars = {
                                        "name2" : "You don't have an account with us"
                                } 
                        response = HttpResponseRedirect('/login')
                        response.delete_cookie('CPUSVAL')
                        response.delete_cookie('CPPWVAL')
                        # return response
                else:
                        template_vars={
                                "name" : "You don't have an account with us"
                        }
                        if google:
                               template_vars = {
                                        "name2" : "You don't have an account with us"
                                } 
                        response = HttpResponseRedirect('/login')
                        response.delete_cookie('CPUSVAL')
                        response.delete_cookie('CPPWVAL')
                        # return response
                template_name = "loginBothOptions.html"
                #writes to the webpage file
                return render(request, template_name, template_vars)        
        template_name = 'LasCrucesNM/Maxx Designs for VIP\'s/maxx.html'
        return render(request, template_name)

def mobileWithGoogle(request):
        if request.method == "GET":
                #home_template variable get html file
                template_name = "mWithGoogle.html"
                #writes to the webpage file
                return render(request, template_name)
        else:
                user = request.POST.get("username")
                password = request.POST.get("password")
                google = False
                if not user:
                        google = True
                        user = request.POST.get("googleUsername")
                        password = "google"
                nickname = user[0: user.index('@')]
                user = cipher(user)
                password = cipher(password)
                where = db.collection(u'users').where(u'username', u'==', user)
                
                
                finalObj = None
                template_vars = {}
                for doc in where:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        template_vars={
                                "name" : "You already have an account with us"
                        }
                        #home_template variable get html file
                        template_name = "mWithGoogle.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else:
                        finalObj = db.collection(u'users').document(user)
                        t1 = threading.Thread(target=createCookies, args=(user, password))
                        t1.start()
                        finalObj.set({
                                u'username' : user,
                                u'password' : password,
                                u'majors' : [],
                                u'colleges' : [],
                                u'collegeLinks' : [],
                                u'collegeStates' : [],
                                u'devices' : [],
                                u'collegeCities' : [],
                                u'name' : nickname,
                                u'GPA' : 0,
                                u'userACT' : 0,
                                u'userSAT' : 0,
                                u'userCity' : "someWhere",
                                u'userState' : "whoKnows",
                                u'imageUrl' : "",
                                u'listings' : [],
                                u'messages' : {}
                                
                        },  merge=True)
                        template_vars={
                                "name" : "Your account has been created!"
                        }
                        
                        template_name = "mWithGoogle.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
        template_name = 'LasCrucesNM/SoGlam/mSoGlam.html'
        return render(request, template_name)
def mLogin(request):
        if request.method == "GET":
                #home_template variable get html file
                template_name = "mLogin.html"
                #writes to the webpage file
                return render(request, template_name)
        else:
                user = request.POST.get("username")
                password = request.POST.get("password")
                image = ""
                google = False
                if not user:
                        google = True
                        user = request.POST.get("googleUsername")
                        password = "google"
                        image = request.POST.get("googleImage")
                user = cipher(user)
                password = cipher(password)
                where = db.collection(u'users').where(u'username', u'==', user)
                
                userObj = None
                for doc in where.stream():
                        
                        userObj = doc.to_dict()
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                template_vars = {}
                for doc in where2:
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        response = HttpResponseRedirect("/mobile/")
                        set_cookie(response, "CPUSVAL", user)
                        set_cookie(response, "CPPWVAL", password)
                        finalObj = db.collection(u'users').document(user)
                        # response.set_cookie("username", value=user, max_age=(24*60*60), path='/', domain="http://127.0.0.1:8000/")
                        # response.set_cookie("password", value=password, max_age=(24*60*60), path='/', domain="http://127.0.0.1:8000/")
                        return response
                elif userObj and not finalObj:
                        template_vars = {
                                "name" : "Either the username or password is wrong"
                        }
                        if google:
                               template_vars = {
                                        "name2" : "You don't have an account with us"
                                } 
                        response = HttpResponseRedirect('/mobile/login')
                        response.delete_cookie('CPUSVAL')
                        response.delete_cookie('CPPWVAL')
                        # return response
                else:
                        template_vars={
                                "name" : "You don't have an account with us"
                        }
                        if google:
                               template_vars = {
                                        "name2" : "You don't have an account with us"
                                } 
                        response = HttpResponseRedirect('/mobile/login')
                        response.delete_cookie('CPUSVAL')
                        response.delete_cookie('CPPWVAL')
                        # return response
                template_name = "loginBothOptions.html"
                #writes to the webpage file
                return render(request, template_name, template_vars)        
        template_name = 'LasCrucesNM/Maxx Designs for VIP\'s/maxx.html'
        return render(request, template_name)


def showData(request):
        template_name = 'LasCrucesNM/Maxx Designs for VIP\'s/maxx.html'
        return render(request, template_name)

def showData2(request):
        template_name = 'Map.html'
        return render(request, template_name)

def showData3(request):
        template_name = 'LasCrucesNM/SoGlam/mSoGlam.html'
        return render(request, template_name)

def showData4(request):
        template_name = 'LasCrucesNM/Maxx Designs for VIP\'s/maxx.html'
        return render(request, template_name)

def setData(request):
        template_name = 'Map.html'
        return render(request, template_name)
    
def addNewUser(request):
        template_name = 'LasCrucesNM/SoGlam/mSoGlam.html'
        return render(request, template_name)

def addGoogleNewUser(request):
        template_name = 'LasCrucesNM/Maxx Designs for VIP\'s/maxx.html'
        return render(request, template_name)

def addAppleNewUser(request):
        template_name = 'Map.html'
        return render(request, template_name)

def embeddedAdPage(request):
        template_name = 'LasCrucesNM/SoGlam/mSoGlam.html'
        return render(request, template_name)

def jsonTest(request):
        template_name = 'LasCrucesNM/Maxx Designs for VIP\'s/maxx.html'
        return render(request, template_name)

def setTemp(request):
        template_name = 'Map.html'
        return render(request, template_name)

def cipher(stringVal):
    sentVar = ""
    arr = ["a", "b", "c", "f", "y"]
    for c in stringVal:
        sentVar += str(float(ord(c))/2)
        sentVar += random.choice(arr)
    return sentVar

def TermsOfService(request):
        template_name = 'TermsOfService.html'
        return render(request, template_name)

def PrivacyPolicy(request):
        template_name = 'PrivacyPolicy.html'
        return render(request, template_name)

def ForgotPassword(request):
        if request.method == "GET":
                template_vars = {
                        "display" : "none"
                }
                template_name = 'ForgotPassword.html'
                return render(request, template_name, template_vars)
        else:
                recipient = request.POST.get("sendEmail")
                ciphered = cipher(recipient)
                where = db.collection(u'users').where(u'username', u'==', ciphered).stream()
                finalObj = None
                rando = random.randint(1000, 10000)
                for doc in where:
                        finalObj = doc.to_dict()
                if finalObj:
                        finalObj = db.collection(u'users').document(ciphered)
                        finalObj.set({
                                u'tempPasscode' : rando,
                                        
                        },  merge=True)
                        mail = send_mail(
                                "Reset Password",
                                "To reset email : https://collegeplus.us/ResetPassword?username="+ cipher(recipient) + "&passcode=" + str(rando),
                                settings.EMAIL_HOST_USER ,
                                [recipient],
                                fail_silently=False,
                        )
                        template_vars = {
                                "display" : "block"
                        }
                template_name = 'ForgotPassword.html'
                return render(request, template_name, template_vars)


def mobileForgotPassword(request):
        if request.method == "GET":
                template_vars = {
                        "display" : "none"
                }
                template_name = 'mobileForgotPassword.html'
                return render(request, template_name, template_vars)
        else:
                recipient = request.POST.get("sendEmail")
                template_vars = {

                }
                ciphered = cipher(recipient)
                where = db.collection(u'users').where(u'username', u'==', username).stream()
                finalObj = None
                for doc in where:
                        finalObj = doc.to_dict()
                if finalObj:
                        finalObj = db.collection(u'users').document(username)
                        finalObj.set({
                                u'tempPasscode' : random.randint(1000, 10000),
                                        
                        },  merge=True)
                        mail = send_mail(
                                "Reset Password",
                                "To reset email : https://collegeplus.us/ResetPassword?username="+ cipher(recipient),
                                settings.EMAIL_HOST_USER ,
                                [recipient],
                                fail_silently=False,
                        )
                        template_vars = {
                                "display" : "block"
                        }
                template_name = 'mobileForgotPassword.html'
                return render(request, template_name, template_vars)

def handler404(request, exception = None):
        return render(request, "handle404.html", status = 404)

def ResetPassword(request):
        if request.method == "GET":
                # template_name = "ResetPassword.html"
                # return render(request, template_name)
                username = request.GET["username"]
                passcode = request.GET["passcode"]
                where = db.collection(u'users').where(u'username', u'==', username)
                
                userObj = None
                finalObj = None
                for doc in where.stream():                  
          
                        finalObj = doc.to_dict()
                if finalObj:
                        if finalObj.get("tempPasscode") == int(passcode):
                                template_vars = {
                                        'name' : passcode,
                                        'verdict' : "none",
                                        'user' : username
                                }
                                #home_template variable get html file
                                template_name = "ResetPassword.html"
                                #writes to the webpage file
                                return render(request, template_name, template_vars)
                        template_vars = {
                                "verdict" : "block"
                        }
                        finalObj = db.collection(u'users').document(username)
                        finalObj.set({
                                "tempPasscode" : firestore.DELETE_FIELD
                        },  merge=True)
                        #home_template variable get html file
                        template_name = "ResetPassword.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else : 
                        obj = {'error' : "account doesn't exist"}
                        response =  JsonResponse(obj)
                        return response
        else:
                newPassword = request.POST.get("password1")
                username = request.POST.get("username")
                passcode = request.POST.get("passcode")
                where = db.collection(u'users').where(u'username', u'==', username)
                finalObj = None
                for doc in where.stream():
                        
                        finalObj = doc.to_dict()
                if finalObj:
                        if finalObj.get("tempPasscode") == int(passcode):
                                finalObj = db.collection(u'users').document(username)
                                finalObj.set({
                                        u'password' : cipher(newPassword),
                                        u'tempPasscode' : firestore.DELETE_FIELD
                                                
                                },  merge=True)
                        else:
                                finalObj.set({
                                        "tempPasscode" : firestore.DELETE_FIELD
                                },  merge=True)
                template_name = 'PasswordChanged.html'
                return render(request, template_name)
def mobileResetPassword(request):
        if request.method == "GET":
                username = cypher(request.GET["username"])
                where = db.collection(u'users').where(u'username', u'==', username)
                userObj = None
                finalObj = None
                for doc in where.stream():
                        if userObj:
                                finalObj = doc.to_dict()
                                break
                        else:
                                userObj = doc.to_dict()
                if userObj:
                        if userObj.get("password") != "51.5g110g55.5g102g54.0g100g":
                                template_vars = {
                                        'name' : username
                                }
                                #home_template variable get html file
                                template_name = "mobileResetPassword.html"
                                #writes to the webpage file
                                return render(request, template_name, template_vars)
                        elif finalObj:
                                if finalObj.get("password") != "51.5g110g55.5g102g54.0g100g":
                                        template_vars = {
                                                'name' : username
                                        }
                                        #home_template variable get html file
                                        template_name = "ResetPassword.html"
                                        #writes to the webpage file
                                        return render(request, template_name, template_vars)


                        template_vars = {
                                'name' : username
                        }
                        #home_template variable get html file
                        template_name = "mobileResetPassword.html"
                        #writes to the webpage file
                        return render(request, template_name, template_vars)
                else : 
                        obj = {'error' : username}
                        response =  JsonResponse(obj)
                        return response
        else:
                newPassword = request.GET("password")
                username = request.GET("username")
                where = db.collection(u'users').where(u'username', u'==', username)
                finalObj = None
                for doc in where.stream():
                        finalObj = doc.to_dict()
                if finalObj:
                        finalObj = db.collection(u'users').document(username)
                        finalObj.set({
                                u'password' : newPassword,
                                        
                        },  merge=True)
                template_name = 'mPasswordChanged.html'
                return render(request, template_name, template_vars)
def showApps(request):
        template_name = 'showApps.html'
        return render(request, template_name)

def mobileShowApps(request):
        template_name = 'Map.html'
        return render(request, template_name)

def returnDegreeSelections(request):
        ethnic = 0
        engineering =0
        communication=0
        legal=0
        english=0
        biological=0
        computer = 0
        education = 0
        political = 0
        business = 0
        economics = 0
        nursing = 0
        finance = 0
        history = 0
        kinesiology = 0
        finished = False

        list1 = [ethnic, engineering, communication, legal, english, biological, computer, education, political, business, economics, nursing, finance, history]
        list2 = ["Ethnic and Gender Studies", "Engineering", "Communication", "Legal Studies", "English", "Biological Sciences", "Computer Science", "Education", "Political Science", "Business", "Economics", "Nursing", "Finance", "History"]
        if request.GET.get("ques1", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques1", " ").replace("+", " "))]+= 1
        if request.GET.get("ques2", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques2", " ").replace("+", " "))]+= 1
        if request.GET.get("ques3", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques3", " ").replace("+", " "))]+= 1
        if request.GET.get("ques4", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques4", " ").replace("+", " "))]+= 1
        if request.GET.get("ques5", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques5", " ").replace("+", " "))]+= 1
        if request.GET.get("ques6", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques6", " ").replace("+", " "))]+= 1
        if request.GET.get("ques7", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques7", " ").replace("+", " "))]+= 1
        if request.GET.get("ques8", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques8", " ").replace("+", " "))]+= 1
        if request.GET.get("ques9", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques9", " ").replace("+", " "))]+= 1
        if request.GET.get("ques10", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques10", " ").replace("+", " "))]+= 1

        top3 = []
        descriptions = []
        urlslist = []
        list2clone = list2.copy()
        list1clone = list1.copy()
        description = [
          "The ethnic studies field explores theories of race, migration, social policy and historical instances regarding various ethnic groups. Gender studies focuses on how the different sexes handle various issues and includes feminist and masculinity theory, as well as theories regarding sexuality, gender roles and various types of gender social systems.",
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
        ]
        urls = [
                "https://study.com/directory/category/Liberal_Arts_and_Humanities/Ethnic_and_Gender_Studies.html#:~:text=Ethnic%20and%20gender%20studies%20are,opportunities%20in%20these%20interdisciplinary%20fields.",
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
        ]

        while(len(top3) < 3):
                tempIndex = 0
                for i in range(0, len(list1clone)):
                        if list1clone[i] > list1clone[tempIndex]:
                                tempIndex = i
                top3.append(list2clone[tempIndex])
                descriptions.append(description[list2.index(list2clone[tempIndex])])
                urlslist.append(urls[list2.index(list2clone[tempIndex])])
                del list2clone[tempIndex]
                del list1clone[tempIndex]
        dictOfDegrees = {
                "majors" : top3,
                "descriptions" : descriptions,
                "urls" : urlslist 
        }

        return JsonResponse(dictOfDegrees)

def returnEngineeringSelections(request):
        civil = 0
        electrical = 0
        chemical = 0
        petroleum = 0
        environmental = 0
        biomedical = 0
        computer = 0
        nuclear =  0
        list1 = [civil, electrical, chemical, environmental, biomedical, computer, nuclear]
        list2 = ["Civil Engineering", "Electrical Engineering", "Chemical Engineering", "Petroleum Engineering", "Environmental Engineering", "Biomedical Engineering", "Computer Engineering", "Nuclear Engineering"]

        if request.GET.get("ques1", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques1", " ").replace("+", " "))]+= 1
        if request.GET.get("ques2", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques2", " ").replace("+", " "))]+= 1
        if request.GET.get("ques3", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques3", " ").replace("+", " "))]+= 1
        if request.GET.get("ques4", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques4", " ").replace("+", " "))]+= 1
        if request.GET.get("ques5", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques5", " ").replace("+", " "))]+= 1
        if request.GET.get("ques6", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques6", " ").replace("+", " "))]+= 1
        if request.GET.get("ques7", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques7", " ").replace("+", " "))]+= 1
        if request.GET.get("ques8", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques8", " ").replace("+", " "))]+= 1
        if request.GET.get("ques9", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques9", " ").replace("+", " "))]+= 1
        if request.GET.get("ques10", " ").replace("+", " ") in list2:
                list1[list2.index(request.GET.get("ques10", " ").replace("+", " "))]+= 1

        top3 = []
        descriptions = []
        urlslist = []
        list2clone = list2.copy()
        list1clone = list1.copy()
        description = [
          "The ethnic studies field explores theories of race, migration, social policy and historical instances regarding various ethnic groups. Gender studies focuses on how the different sexes handle various issues and includes feminist and masculinity theory, as well as theories regarding sexuality, gender roles and various types of gender social systems.",
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
        ]
        urls = [
                "https://study.com/directory/category/Liberal_Arts_and_Humanities/Ethnic_and_Gender_Studies.html#:~:text=Ethnic%20and%20gender%20studies%20are,opportunities%20in%20these%20interdisciplinary%20fields.",
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
        ]

        while(len(top3) < 3):
                tempIndex = 0
                for i in range(0, len(list1clone)):
                        if list1clone[i] > list1clone[tempIndex]:
                                tempIndex = i
                top3.append(list2clone[tempIndex])
                descriptions.append(description[list2.index(list2clone[tempIndex])])
                urlslist.append(urls[list2.index(list2clone[tempIndex])])
                del list2clone[tempIndex]
                del list1clone[tempIndex]
        dictOfDegrees = {
                "majors" : top3,
                "descriptions" : descriptions,
                "urls" : urlslist 
        }

        return JsonResponse(dictOfDegrees)

def returnDeviceSelections(request):
        
        laptops = {
                "thinkpads": {
                        "p1":{
                                "i7": {
                                        "value":"ThinkPad P1 Gen 2 (15) Laptop Workstation",
                                        "url":"https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-p/c/thinkpadp",
                                        "num": 0,
                                        "img": "https://www.lenovo.com/medias/lenovo-thinkpad-p-series-feature-hero.png?context=bWFzdGVyfHJvb3R8NzM4ODF8aW1hZ2UvcG5nfGhlOC9oMjgvOTc4NDY1MTgwODc5OC5wbmd8NjAxMjg3NjJhNzM4MGE2OWMyZTFiODA5NGUyZjY5NjNkYjQ3YTkwZDcyOTBkZmZjMzYxZjU1MzIwMWQ5ZjQyZQ",
                                },
                        } ,
                        "x1":{
                                "i7":{
                                        "value":"ThinkPad X1 Carbon Gen 7 (14) laptop",
                                        "url":"https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-x1/c/thinkpadx1",
                                        "num": 0,
                                        "img": "https://www.lenovo.com/medias/lenovo-laptop-thinkpad-x1-subseries-thumbnail.png?context=bWFzdGVyfHJvb3R8MTcxMTl8aW1hZ2UvcG5nfGgzMy9oOGMvMTA4OTI2ODA2OTE3NDIucG5nfGMyN2JiZjliN2ZjODE3Nzk1Yzk3ZjA3YTAxOGQzYWI3ODI4MTNmZDNmZGM4OTdkYWE5YmI3MWE0ZjI3NWIwYzg&w=1920",
                                },

                        },
                        "yoga":{
                                "i7":{
                                        "value":"Yoga C930 (14) Laptop",
                                        "url":"https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-yoga/c/thinkpadyoga",
                                        "num": 0,
                                        "img": "https://www.lenovo.com/medias/lenovo-laptop-thinkpad-2-in-1-subseries-thumbnail.png?context=bWFzdGVyfHJvb3R8MjUyNjB8aW1hZ2UvcG5nfGhjOC9oODQvMTA4OTI2NzQ0NjU4MjIucG5nfDRhYTI5MTU1OGIyOWFjMTUzNzVkNGM3MDM4MWYwNDU5Mzc5ZjMxZjRkNWJmNDdhZjYxOTYyM2Y3ZTkyNDI4ZTk&w=1920",
                                },
                        },


                },
                "surface":{
                        "surfaces":{
                                "i5":{
                                        "value":"Surface Laptop 3",
                                        "url":"https://www.microsoft.com/en-us/p/surface-laptop-3/8vfggh1r94tm?activetab=overview",
                                        "num": 0,
                                        "img": "https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE2v60k?ver=802f",
                                },
                        },
                        "pro":{
                                "i7":{
                                        "value":"Surface Pro 7",
                                        "url":"https://www.microsoft.com/en-us/p/surface-pro-7/8n17j0m5zzqs?activetab=overview",
                                        "num": 0,
                                        "img": "https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE2GUWJ?ver=2120",
                                },
                        },
                        "book":{
                                "i7":{
                                        "value":"Surface Book 3",
                                        "url":"https://www.microsoft.com/en-us/p/surface-book-3/8xbw9g3z71f1?activetab=pivot%3aoverviewtab",
                                        "num": 0,
                                        "img": "https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE1FU5k?ver=cec9",
                                },
                        },
                },
                "macbook":{
                        "air":{
                                "m1":{
                                        "value":"Apple Macbook Air",
                                        "url":"https://www.apple.com/us-hed/shop/buy-mac/macbook-air",
                                        "num": 0,
                                        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-space-gray-select-201810?wid=904&hei=840&fmt=jpeg&qlt=80&op_usm=0.5,0.5&.v=1603332211000",
                                },
                        },
                        "pro":{
                                "m1":{
                                        "value":"Apple Macbook Pro",
                                        "url":"https://www.apple.com/us-hed/shop/buy-mac/macbook-pro/13-inch",
                                        "num": 0,
                                        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mbp-spacegray-select-202011?wid=904&hei=840&fmt=jpeg&qlt=80&op_usm=0.5,0.5&.v=1603406905000",
                                },
                        },
                },
                "pixel":{
                        "pixelbook":{
                                "i5":{
                                        "value":"Google Pixelbook",
                                        "url":"https://store.google.com/product/google_pixelbook",
                                        "num": 0,
                                        "img": "https://lh3.googleusercontent.com/uMVyiVMEKr9SYnY8g90tGVwKAuAAZrC2urEVASlb9G89PBhEqeuE1PD01PWppV_RbZIr=w1000",
                                },
                                "i7":{
                                        "value":"Google Pixelbook",
                                        "url":"https://store.google.com/product/google_pixelbook",
                                        "num": 0,
                                        "img": "https://lh3.googleusercontent.com/uMVyiVMEKr9SYnY8g90tGVwKAuAAZrC2urEVASlb9G89PBhEqeuE1PD01PWppV_RbZIr=w1000",
                                },
                        },
                        "go" : {
                                "i5" : {
                                        "value" : "Google Pixelbook Go",
                                        "url" : "https://store.google.com/product/pixelbook_go",
                                        "num" : 0,
                                        "img" : "https://cnet1.cbsistatic.com/img/j-12omWHRXGxkAVypxREY1_MIyw=/1200x675/2019/10/24/a8f906ee-afcf-4750-bc13-67846334757b/51-pixelbook-go.jpg"
                                },
                                "i7" : {
                                        "value" : "Google Pixelbook Go",
                                        "url" : "https://store.google.com/product/pixelbook_go",
                                        "num" : 0,
                                        "img" : "https://cnet1.cbsistatic.com/img/j-12omWHRXGxkAVypxREY1_MIyw=/1200x675/2019/10/24/a8f906ee-afcf-4750-bc13-67846334757b/51-pixelbook-go.jpg"
                                }
                        }
                },
                "chromebook":{
                        "dell":{
                                "celeron":{
                                        "value":"Dell Chromebook 3100",
                                        "url":"https://www.dell.com/en-us/work/shop/dell-laptops-and-notebooks/chromebook-3100/spd/chromebook-11-3100-laptop/s001c310011us?gacd=9646510-1025-5761040-266794296-0&dgc=st&ds_rl=1282786&gclid=CjwKCAiAq8f-BRBtEiwAGr3DgZLk8i0U3wtkRiIwTs0whw25HnImc80su7rWHcGI3HUneuKayRiO6RoCJckQAvD_BwE&gclsrc=aw.ds",
                                        "num": 0,
                                        "img": "https://i.dell.com/is/image/DellContent//content/dam/global-asset-library/Products/Notebooks/Chromebook/11_3100_non-touch/ch3100nt_lnb_00000f90_gy.psd?fmt=pjpg&pscan=auto&scl=1&hei=402&wid=402&qlt=95,0&resMode=sharp2&op_usm=1.75,0.3,2,0&size=402,402",
                                },
                        },
                        "samsung":{
                                "celeron":{
                                        "value":"Samsung Chromebook 4",
                                        "url":"https://www.samsung.com/us/computing/chromebooks/under-12/chromebook-4-11-6-32gb-storage-4gb-ram-xe310xba-k01us/",
                                        "num": 0,
                                        "img": "https://image-us.samsung.com/SamsungUS/home/computing/chromebooks/pdp/xe310xba-k03us/gallery/Gallery-CB4-11in-1-092519.jpg?$product-details-jpg$",
                                },
                        },
                },
                "dell":{
                        "xps":{
                                "i7":{
                                        "value":"XPS 15 2-in-1 Laptop",
                                        "url":"https://www.dell.com/en-us/shop/cty/pdp/spd/xps-15-9500-laptop?gacd=9694607-1007-5761040-0-0&dgc=st&&gclid=CjwKCAjw26H3BRB2EiwAy32zhdy_xK6wvC_g6hL6YgHlZRZbzXfzqNcwuIEuyPl2KevUsp6LMZctvhoCHbkQAvD_BwE&gclsrc=aw.ds",
                                        "num": 0,
                                        "img": "https://i.dell.com/is/image/DellContent//content/dam/global-site-design/product_images/dell_client_products/notebooks/xps_notebooks/xps_15_9500/pdp/notebook_laptop_xps_15_9500_npl_pdp_mod_05.jpg?qlt=95&amp;fit=constrain,1&amp;hei=470&amp;wid=920&amp;fmt=jpg",
                                        },
                                "i5":{
                                        "value":"XPS 15 2-in-1 Laptop",
                                        "url":"https://www.dell.com/en-us/shop/cty/pdp/spd/xps-15-9500-laptop?gacd=9694607-1007-5761040-0-0&dgc=st&&gclid=CjwKCAjw26H3BRB2EiwAy32zhdy_xK6wvC_g6hL6YgHlZRZbzXfzqNcwuIEuyPl2KevUsp6LMZctvhoCHbkQAvD_BwE&gclsrc=aw.ds",
                                        "num": 0,
                                        "img": "https://i.dell.com/is/image/DellContent//content/dam/global-site-design/product_images/dell_client_products/notebooks/xps_notebooks/xps_15_9500/pdp/notebook_laptop_xps_15_9500_npl_pdp_mod_05.jpg?qlt=95&amp;fit=constrain,1&amp;hei=470&amp;wid=920&amp;fmt=jpg",
                                },
                        },
                },
                "hp":{
                        "spectre":{
                                "i7":{
                                        "value":"HP Spectre x360 13 inch",
                                        "url":"https://store.hp.com/us/en/pdp/hp-spectre-x360-laptop-13t-touch-7al88av-1?jumpid=ma_2017-spectre-family_product-tile_hp-spectre-x-360_11_7al88av-1_hp-spectre-x360-lapt",
                                        "num": 0,
                                        "img": "https://cnet1.cbsistatic.com/img/Lt6RzR_6J4woW1QgVpaScsXCnm8=/1200x675/2019/11/27/bb5014cc-9049-4ccf-b946-f8cc33449b8e/hp-spectre-x360-13-late-2019-20.jpg",
                                },
                        },
                        "envy":{
                                "i7":{
                                        "value":"HP ENVY Laptop -13t",
                                        "url":"https://store.hp.com/us/en/pdp/hp-envy-laptop-13t-ba000-8mx92av-1",
                                        "num": 0,
                                        "img": "https://cdn.mos.cms.futurecdn.net/LFGXuEaG2jnCv8nG3XPN7E.jpg",
                                },
                        },
                },
                "acer":{
                        "swift1":{
                                "celeron":{
                                        "value":"Swift 1 Laptop",
                                        "url":"https://www.acer.com/ac/en/US/content/series/swift1",
                                        "num": 0,
                                        "img": "https://static.acer.com/up/Resource/Acer/Laptops/Swift_1/Overview/20180315/swift_1_overview_features_large.jpg",
                                },
                        },
                        "swift3":{
                                "i7":{
                                        "value":"Swift 3 Laptop",
                                        "url":"https://www.acer.com/ac/en/US/content/series/swift3",
                                        "num": 0,
                                        "img": "https://static.acer.com/up/Resource/Acer/Laptops/Swift_3/SF313-52_SF314-57/20200109/Swift-3_ksp-02_2560-Athena.jpg",
                                },
                        },
                }
        }
        ## the favorite fasho
        laptops["macbook"]["air"]["m1"]["num"]  = 3
        if request.GET.get("ques1", " ").replace("+", " ") =="0":
                laptops["thinkpads"]["p1"]["i7"]["num"] += 5
                laptops["thinkpads"]["x1"]["i7"]["num"] += 5
                laptops["macbook"]["pro"]["m1"]["num"] += 7
                laptops["macbook"]["air"]["m1"]["num"] += 7
        
        if request.GET.get("ques1", " ").replace("+", " ") == "1" :
                laptops["thinkpads"]["yoga"]["i7"]["num"] += 5
                laptops["surface"]["pro"]["i7"]["num"] += 5
                laptops["macbook"]["air"]["m1"]["num"] += 5
                laptops["pixel"]["go"]["i5"]["num"] += 3
                laptops["pixel"]["go"]["i7"]["num"] += 3
        
        if request.GET.get("ques1", " ").replace("+", " ") == "2" : 
                laptops["thinkpads"]["yoga"]["i7"]["num"] += 5
                laptops["dell"]["xps"]["i7"]["num"] += 5
                laptops["hp"]["spectre"]["i7"]["num"] += 5
                laptops["dell"]["xps"]["i5"]["num"] += 5
                laptops["pixel"]["pixelbook"]["i7"]["num"] += 5
        if request.GET.get("ques1", " ").replace("+", " ") == "3":
                laptops["hp"]["envy"]["i7"]["num"] += 5
                laptops["pixel"]["pixelbook"]["i5"]["num"] += 5
                laptops["acer"]["swift3"]["i7"]["num"] += 5
                laptops["surface"]["surfaces"]["i5"]["num"] += 5
        
        if request.GET.get("ques1", " ").replace("+", " ") == "4":
                laptops["acer"]["swift3"]["i7"]["num"] += 5
        
        if request.GET.get("ques1", " ").replace("+", " ") == "5":
                laptops["acer"]["swift1"]["celeron"]["num"] += 5
                laptops["chromebook"]["samsung"]["celeron"]["num"] += 5
                laptops["chromebook"]["dell"]["celeron"]["num"] += 5
        
        #####################
        if request.GET.get("ques2", " ").replace("+", " ") == "0":
                laptops["thinkpads"]["p1"]["i7"]["num"] += 3
                laptops["thinkpads"]["x1"]["i7"]["num"] += 3
                laptops["thinkpads"]["yoga"]["i7"]["num"] += 3
                laptops["surface"]["surfaces"]["i5"]["num"] += 3
                laptops["surface"]["pro"]["i7"]["num"] += 3
                laptops["surface"]["book"]["i7"]["num"] += 3
                laptops["dell"]["xps"]["i7"]["num"] += 3
                laptops["dell"]["xps"]["i5"]["num"] += 3
                laptops["hp"]["spectre"]["i7"]["num"] += 3
                laptops["hp"]["envy"]["i7"]["num"] += 3
                laptops["acer"]["swift1"]["celeron"]["num"] += 3
                laptops["acer"]["swift3"]["i7"]["num"] += 3
        
        if request.GET.get("ques2", " ").replace("+", " ") == "1":
                laptops["macbook"]["air"]["m1"]["num"] += 3
                laptops["macbook"]["pro"]["m1"]["num"] += 3
        
        if request.GET.get("ques2", " ").replace("+", " ") == "2":
                laptops["pixel"]["pixelbook"]["i5"]["num"] += 3
                laptops["pixel"]["go"]["i5"]["num"] += 3
                laptops["pixel"]["go"]["i7"]["num"] += 3
                laptops["chromebook"]["samsung"]["celeron"]["num"] += 3
                laptops["chromebook"]["dell"]["celeron"]["num"] += 3
                laptops["pixel"]["pixelbook"]["i7"]["num"] += 3

        ######################
        if request.GET.get("ques3", " ").replace("+", " ") == "0":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1

        if request.GET.get("ques3", " ").replace("+", " ") == "1":
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1
                laptops["hp"]["envy"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1

        if request.GET.get("ques4", " ").replace("+", " ") == "0":
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1

        if request.GET.get("ques4", " ").replace("+", " ") == "1":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1 
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1

        if request.GET.get("ques5", " ").replace("+", " ") == "0":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1

        if request.GET.get("ques5", " ").replace("+", " ") == "1":
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1

        if request.GET.get("ques6", " ").replace("+", " ") == "0":
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1

        if request.GET.get("ques6", " ").replace("+", " ") == "1":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1

        if request.GET.get("ques6", " ").replace("+", " ") == "2":
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1

        if request.GET.get("ques6", " ").replace("+", " ") == "3":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
        
        if request.GET.get("ques6", " ").replace("+", " ") == "4":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1
        
        if request.GET.get("ques6", " ").replace("+", " ") == "5":
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
        
        if request.GET.get("ques6", " ").replace("+", " ") == "6":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1
        
        if request.GET.get("ques7", " ").replace("+", " ") == "0":
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1
        
        if request.GET.get("ques8", " ").replace("+", " ") == "0":
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i7"]["num"] += 1
        
        if request.GET.get("ques8", " ").replace("+", " ") == "1":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
        
        if request.GET.get("ques8", " ").replace("+", " ") == "2":
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1
        
        if request.GET.get("ques9", " ").replace("+", " ") == "0":
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1
        
        if request.GET.get("ques9", " ").replace("+", " ") == "1":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
        
        if request.GET.get("ques10", " ").replace("+", " ") == "0":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
        
        if request.GET.get("ques10", " ").replace("+", " ") == "1":
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"] += 1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1

        listOfLaptops = []
        listOfUrls = []
        listOfImages = []

        mainList = [laptops["thinkpads"]["p1"]["i7"], laptops["thinkpads"]["x1"]["i7"], laptops["thinkpads"]["yoga"]["i7"], laptops["surface"]["surfaces"]["i5"], laptops["surface"]["pro"]["i7"], laptops["surface"]["book"]["i7"], laptops["macbook"]["air"]["m1"], laptops["macbook"]["pro"]["m1"], laptops["pixel"]["pixelbook"]["i5"], laptops["pixel"]["pixelbook"]["i7"], laptops["chromebook"]["dell"]["celeron"], laptops["chromebook"]["samsung"]["celeron"], laptops["dell"]["xps"]["i7"], laptops["dell"]["xps"]["i5"], laptops["hp"]["spectre"]["i7"], laptops["hp"]["envy"]["i7"], laptops["acer"]["swift1"]["celeron"], laptops["acer"]["swift3"]["i7"], laptops["pixel"]["go"]["i5"], laptops["pixel"]["go"]["i7"]]
        comparisonList = mainList.copy()
        realTop3 = []
        while(len(realTop3) < 3):
                tempMax =  0
                index = 0
                for i in range(0, len(comparisonList)):
                        if comparisonList[i]["num"] > tempMax:
                                tempMax = comparisonList[i]["num"]
                                index = i
                realTop3.append(comparisonList[index])
                del comparisonList[index]
        dictOfDegrees = {
                "devices" : [realTop3[0]["value"], realTop3[1]["value"], realTop3[2]["value"]],
                "url" : [realTop3[0]["url"], realTop3[1]["url"], realTop3[2]["url"]],
                "image" : [realTop3[0]["img"], realTop3[1]["img"], realTop3[2]["img"]],
        }

        response =  JsonResponse(dictOfDegrees)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response

def returnDeviceSelections2(answers):
        
        laptops = {
                "thinkpads": {
                        "p1":{
                                "i7": {
                                        "value":"ThinkPad P1 Gen 2 (15) Laptop Workstation",
                                        "url":"https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-p/c/thinkpadp",
                                        "num": 0,
                                        "img": "https://www.lenovo.com/medias/lenovo-thinkpad-p-series-feature-hero.png?context=bWFzdGVyfHJvb3R8NzM4ODF8aW1hZ2UvcG5nfGhlOC9oMjgvOTc4NDY1MTgwODc5OC5wbmd8NjAxMjg3NjJhNzM4MGE2OWMyZTFiODA5NGUyZjY5NjNkYjQ3YTkwZDcyOTBkZmZjMzYxZjU1MzIwMWQ5ZjQyZQ",
                                },
                        } ,
                        "x1":{
                                "i7":{
                                        "value":"ThinkPad X1 Carbon Gen 7 (14) laptop",
                                        "url":"https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-x1/c/thinkpadx1",
                                        "num": 0,
                                        "img": "https://www.lenovo.com/medias/lenovo-laptop-thinkpad-x1-subseries-thumbnail.png?context=bWFzdGVyfHJvb3R8MTcxMTl8aW1hZ2UvcG5nfGgzMy9oOGMvMTA4OTI2ODA2OTE3NDIucG5nfGMyN2JiZjliN2ZjODE3Nzk1Yzk3ZjA3YTAxOGQzYWI3ODI4MTNmZDNmZGM4OTdkYWE5YmI3MWE0ZjI3NWIwYzg&w=1920",
                                },

                        },
                        "yoga":{
                                "i7":{
                                        "value":"Yoga C930 (14) Laptop",
                                        "url":"https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-yoga/c/thinkpadyoga",
                                        "num": 0,
                                        "img": "https://www.lenovo.com/medias/lenovo-laptop-thinkpad-2-in-1-subseries-thumbnail.png?context=bWFzdGVyfHJvb3R8MjUyNjB8aW1hZ2UvcG5nfGhjOC9oODQvMTA4OTI2NzQ0NjU4MjIucG5nfDRhYTI5MTU1OGIyOWFjMTUzNzVkNGM3MDM4MWYwNDU5Mzc5ZjMxZjRkNWJmNDdhZjYxOTYyM2Y3ZTkyNDI4ZTk&w=1920",
                                },
                        },


                },
                "surface":{
                        "surfaces":{
                                "i5":{
                                        "value":"Surface Laptop 3",
                                        "url":"https://www.microsoft.com/en-us/p/surface-laptop-3/8vfggh1r94tm?activetab=overview",
                                        "num": 0,
                                        "img": "https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE2v60k?ver=802f",
                                },
                        },
                        "pro":{
                                "i7":{
                                        "value":"Surface Pro 7",
                                        "url":"https://www.microsoft.com/en-us/p/surface-pro-7/8n17j0m5zzqs?activetab=overview",
                                        "num": 0,
                                        "img": "https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE2GUWJ?ver=2120",
                                },
                        },
                        "book":{
                                "i7":{
                                        "value":"Surface Book 3",
                                        "url":"https://www.microsoft.com/en-us/p/surface-book-3/8xbw9g3z71f1?activetab=pivot%3aoverviewtab",
                                        "num": 0,
                                        "img": "https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE1FU5k?ver=cec9",
                                },
                        },
                },
                "macbook":{
                        "air":{
                                "m1":{
                                        "value":"Apple Macbook Air",
                                        "url":"https://www.apple.com/us-hed/shop/buy-mac/macbook-air",
                                        "num": 0,
                                        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-space-gray-select-201810?wid=904&hei=840&fmt=jpeg&qlt=80&op_usm=0.5,0.5&.v=1603332211000",
                                },
                        },
                        "pro":{
                                "m1":{
                                        "value":"Apple Macbook Pro",
                                        "url":"https://www.apple.com/us-hed/shop/buy-mac/macbook-pro/13-inch",
                                        "num": 0,
                                        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mbp-spacegray-select-202011?wid=904&hei=840&fmt=jpeg&qlt=80&op_usm=0.5,0.5&.v=1603406905000",
                                },
                        },
                },
                "pixel":{
                        "pixelbook":{
                                "i5":{
                                        "value":"Google Pixelbook",
                                        "url":"https://store.google.com/product/google_pixelbook",
                                        "num": 0,
                                        "img": "https://lh3.googleusercontent.com/uMVyiVMEKr9SYnY8g90tGVwKAuAAZrC2urEVASlb9G89PBhEqeuE1PD01PWppV_RbZIr=w1000",
                                },
                                "i7":{
                                        "value":"Google Pixelbook",
                                        "url":"https://store.google.com/product/google_pixelbook",
                                        "num": 0,
                                        "img": "https://lh3.googleusercontent.com/uMVyiVMEKr9SYnY8g90tGVwKAuAAZrC2urEVASlb9G89PBhEqeuE1PD01PWppV_RbZIr=w1000",
                                },
                        },
                        "go" : {
                                "i5" : {
                                        "value" : "Google Pixelbook Go",
                                        "url" : "https://store.google.com/product/pixelbook_go",
                                        "num" : 0,
                                        "img" : "https://cnet1.cbsistatic.com/img/j-12omWHRXGxkAVypxREY1_MIyw=/1200x675/2019/10/24/a8f906ee-afcf-4750-bc13-67846334757b/51-pixelbook-go.jpg"
                                },
                                "i7" : {
                                        "value" : "Google Pixelbook Go",
                                        "url" : "https://store.google.com/product/pixelbook_go",
                                        "num" : 0,
                                        "img" : "https://cnet1.cbsistatic.com/img/j-12omWHRXGxkAVypxREY1_MIyw=/1200x675/2019/10/24/a8f906ee-afcf-4750-bc13-67846334757b/51-pixelbook-go.jpg"
                                }
                        }
                },
                "chromebook":{
                        "dell":{
                                "celeron":{
                                        "value":"Dell Chromebook 3100",
                                        "url":"https://www.dell.com/en-us/work/shop/dell-laptops-and-notebooks/chromebook-3100/spd/chromebook-11-3100-laptop/s001c310011us?gacd=9646510-1025-5761040-266794296-0&dgc=st&ds_rl=1282786&gclid=CjwKCAiAq8f-BRBtEiwAGr3DgZLk8i0U3wtkRiIwTs0whw25HnImc80su7rWHcGI3HUneuKayRiO6RoCJckQAvD_BwE&gclsrc=aw.ds",
                                        "num": 0,
                                        "img": "https://i.dell.com/is/image/DellContent//content/dam/global-asset-library/Products/Notebooks/Chromebook/11_3100_non-touch/ch3100nt_lnb_00000f90_gy.psd?fmt=pjpg&pscan=auto&scl=1&hei=402&wid=402&qlt=95,0&resMode=sharp2&op_usm=1.75,0.3,2,0&size=402,402",
                                },
                        },
                        "samsung":{
                                "celeron":{
                                        "value":"Samsung Chromebook 4",
                                        "url":"https://www.samsung.com/us/computing/chromebooks/under-12/chromebook-4-11-6-32gb-storage-4gb-ram-xe310xba-k01us/",
                                        "num": 0,
                                        "img": "https://image-us.samsung.com/SamsungUS/home/computing/chromebooks/pdp/xe310xba-k03us/gallery/Gallery-CB4-11in-1-092519.jpg?$product-details-jpg$",
                                },
                        },
                },
                "dell":{
                        "xps":{
                                "i7":{
                                        "value":"XPS 15 2-in-1 Laptop",
                                        "url":"https://www.dell.com/en-us/shop/cty/pdp/spd/xps-15-9500-laptop?gacd=9694607-1007-5761040-0-0&dgc=st&&gclid=CjwKCAjw26H3BRB2EiwAy32zhdy_xK6wvC_g6hL6YgHlZRZbzXfzqNcwuIEuyPl2KevUsp6LMZctvhoCHbkQAvD_BwE&gclsrc=aw.ds",
                                        "num": 0,
                                        "img": "https://i.dell.com/is/image/DellContent//content/dam/global-site-design/product_images/dell_client_products/notebooks/xps_notebooks/xps_15_9500/pdp/notebook_laptop_xps_15_9500_npl_pdp_mod_05.jpg?qlt=95&amp;fit=constrain,1&amp;hei=470&amp;wid=920&amp;fmt=jpg",
                                        },
                                "i5":{
                                        "value":"XPS 15 2-in-1 Laptop",
                                        "url":"https://www.dell.com/en-us/shop/cty/pdp/spd/xps-15-9500-laptop?gacd=9694607-1007-5761040-0-0&dgc=st&&gclid=CjwKCAjw26H3BRB2EiwAy32zhdy_xK6wvC_g6hL6YgHlZRZbzXfzqNcwuIEuyPl2KevUsp6LMZctvhoCHbkQAvD_BwE&gclsrc=aw.ds",
                                        "num": 0,
                                        "img": "https://i.dell.com/is/image/DellContent//content/dam/global-site-design/product_images/dell_client_products/notebooks/xps_notebooks/xps_15_9500/pdp/notebook_laptop_xps_15_9500_npl_pdp_mod_05.jpg?qlt=95&amp;fit=constrain,1&amp;hei=470&amp;wid=920&amp;fmt=jpg",
                                },
                        },
                },
                "hp":{
                        "spectre":{
                                "i7":{
                                        "value":"HP Spectre x360 13 inch",
                                        "url":"https://store.hp.com/us/en/pdp/hp-spectre-x360-laptop-13t-touch-7al88av-1?jumpid=ma_2017-spectre-family_product-tile_hp-spectre-x-360_11_7al88av-1_hp-spectre-x360-lapt",
                                        "num": 0,
                                        "img": "https://cnet1.cbsistatic.com/img/Lt6RzR_6J4woW1QgVpaScsXCnm8=/1200x675/2019/11/27/bb5014cc-9049-4ccf-b946-f8cc33449b8e/hp-spectre-x360-13-late-2019-20.jpg",
                                },
                        },
                        "envy":{
                                "i7":{
                                        "value":"HP ENVY Laptop -13t",
                                        "url":"https://store.hp.com/us/en/pdp/hp-envy-laptop-13t-ba000-8mx92av-1",
                                        "num": 0,
                                        "img": "https://cdn.mos.cms.futurecdn.net/LFGXuEaG2jnCv8nG3XPN7E.jpg",
                                },
                        },
                },
                "acer":{
                        "swift1":{
                                "celeron":{
                                        "value":"Swift 1 Laptop",
                                        "url":"https://www.acer.com/ac/en/US/content/series/swift1",
                                        "num": 0,
                                        "img": "https://static.acer.com/up/Resource/Acer/Laptops/Swift_1/Overview/20180315/swift_1_overview_features_large.jpg",
                                },
                        },
                        "swift3":{
                                "i7":{
                                        "value":"Swift 3 Laptop",
                                        "url":"https://www.acer.com/ac/en/US/content/series/swift3",
                                        "num": 0,
                                        "img": "https://static.acer.com/up/Resource/Acer/Laptops/Swift_3/SF313-52_SF314-57/20200109/Swift-3_ksp-02_2560-Athena.jpg",
                                },
                        },
                }
        }
        ## the favorite fasho
        laptops["macbook"]["air"]["m1"]["num"]  = 3
        if answers[0] =="0":
                laptops["thinkpads"]["p1"]["i7"]["num"] += 5
                laptops["thinkpads"]["x1"]["i7"]["num"] += 5
                laptops["macbook"]["pro"]["m1"]["num"] += 7
                laptops["macbook"]["air"]["m1"]["num"] += 7
        
        if answers[0] == "1" :
                laptops["thinkpads"]["yoga"]["i7"]["num"] += 5
                laptops["surface"]["pro"]["i7"]["num"] += 5
                laptops["macbook"]["air"]["m1"]["num"] += 5
                laptops["pixel"]["go"]["i5"]["num"] += 3
                laptops["pixel"]["go"]["i7"]["num"] += 3
        
        if answers[0] == "2" : 
                laptops["thinkpads"]["yoga"]["i7"]["num"] += 5
                laptops["dell"]["xps"]["i7"]["num"] += 5
                laptops["hp"]["spectre"]["i7"]["num"] += 5
                laptops["dell"]["xps"]["i5"]["num"] += 5
                laptops["pixel"]["pixelbook"]["i7"]["num"] += 5
        if answers[0] == "3":
                laptops["hp"]["envy"]["i7"]["num"] += 5
                laptops["pixel"]["pixelbook"]["i5"]["num"] += 5
                laptops["acer"]["swift3"]["i7"]["num"] += 5
                laptops["surface"]["surfaces"]["i5"]["num"] += 5
        
        if answers[0] == "4":
                laptops["acer"]["swift3"]["i7"]["num"] += 5
        
        if answers[0] == "5":
                laptops["acer"]["swift1"]["celeron"]["num"] += 5
                laptops["chromebook"]["samsung"]["celeron"]["num"] += 5
                laptops["chromebook"]["dell"]["celeron"]["num"] += 5
        
        #####################
        if answers[1] == "0":
                laptops["thinkpads"]["p1"]["i7"]["num"] += 3
                laptops["thinkpads"]["x1"]["i7"]["num"] += 3
                laptops["thinkpads"]["yoga"]["i7"]["num"] += 3
                laptops["surface"]["surfaces"]["i5"]["num"] += 3
                laptops["surface"]["pro"]["i7"]["num"] += 3
                laptops["surface"]["book"]["i7"]["num"] += 3
                laptops["dell"]["xps"]["i7"]["num"] += 3
                laptops["dell"]["xps"]["i5"]["num"] += 3
                laptops["hp"]["spectre"]["i7"]["num"] += 3
                laptops["hp"]["envy"]["i7"]["num"] += 3
                laptops["acer"]["swift1"]["celeron"]["num"] += 3
                laptops["acer"]["swift3"]["i7"]["num"] += 3
        
        if answers[1] == "1":
                laptops["macbook"]["air"]["m1"]["num"] += 3
                laptops["macbook"]["pro"]["m1"]["num"] += 3
        
        if answers[1] == "2":
                laptops["pixel"]["pixelbook"]["i5"]["num"] += 3
                laptops["pixel"]["go"]["i5"]["num"] += 3
                laptops["pixel"]["go"]["i7"]["num"] += 3
                laptops["chromebook"]["samsung"]["celeron"]["num"] += 3
                laptops["chromebook"]["dell"]["celeron"]["num"] += 3
                laptops["pixel"]["pixelbook"]["i7"]["num"] += 3

        ######################
        if answers[2] == "0":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1

        if answers[2] == "1":
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1
                laptops["hp"]["envy"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1

        if answers[3] == "0":
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1

        if answers[3] == "1":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1 
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1

        if answers[4] == "0":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1

        if answers[4] == "1":
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1

        if answers[5] == "0":
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1

        if answers[5] == "1":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1

        if answers[5] == "2":
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1

        if answers[5] == "3":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
        
        if answers[5] == "4":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1
        
        if answers[5] == "5":
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
        
        if answers[5] == "6":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1
        
        if answers[6] == "0":
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1
        
        if answers[7] == "0":
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["pixel"]["go"]["i7"]["num"] += 1
        
        if answers[7] == "1":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["pixel"]["pixelbook"]["i5"]["num"]+=1
                laptops["pixel"]["go"]["i5"]["num"] += 1
        
        if answers[7] == "2":
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1
        
        if answers[8] == "0":
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"]+=1
        
        if answers[8] == "1":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
        
        if answers[9] == "0":
                laptops["surface"]["surfaces"]["i5"]["num"]+=1
                laptops["surface"]["pro"]["i7"]["num"]+=1
                laptops["surface"]["book"]["i7"]["num"]+=1
                laptops["macbook"]["air"]["m1"]["num"]+=1
                laptops["macbook"]["pro"]["m1"]["num"]+=1
                laptops["dell"]["xps"]["i7"]["num"]+=1
                laptops["dell"]["xps"]["i5"]["num"]+=1
                laptops["hp"]["spectre"]["i7"]["num"]+=1
                laptops["thinkpads"]["p1"]["i7"]["num"]+=1
                laptops["thinkpads"]["x1"]["i7"]["num"]+=1
                laptops["thinkpads"]["yoga"]["i7"]["num"]+=1
                laptops["acer"]["swift1"]["celeron"]["num"]+=1
                laptops["acer"]["swift3"]["i7"]["num"]+=1
        
        if answers[9] == "1":
                laptops["chromebook"]["dell"]["celeron"]["num"]+=1
                laptops["chromebook"]["samsung"]["celeron"]["num"] += 1
                laptops["pixel"]["go"]["i5"]["num"] += 1
                laptops["pixel"]["go"]["i7"]["num"] += 1

        listOfLaptops = []
        listOfUrls = []
        listOfImages = []

        mainList = [laptops["thinkpads"]["p1"]["i7"], laptops["thinkpads"]["x1"]["i7"], laptops["thinkpads"]["yoga"]["i7"], laptops["surface"]["surfaces"]["i5"], laptops["surface"]["pro"]["i7"], laptops["surface"]["book"]["i7"], laptops["macbook"]["air"]["m1"], laptops["macbook"]["pro"]["m1"], laptops["pixel"]["pixelbook"]["i5"], laptops["pixel"]["pixelbook"]["i7"], laptops["chromebook"]["dell"]["celeron"], laptops["chromebook"]["samsung"]["celeron"], laptops["dell"]["xps"]["i7"], laptops["dell"]["xps"]["i5"], laptops["hp"]["spectre"]["i7"], laptops["hp"]["envy"]["i7"], laptops["acer"]["swift1"]["celeron"], laptops["acer"]["swift3"]["i7"], laptops["pixel"]["go"]["i5"], laptops["pixel"]["go"]["i7"]]
        comparisonList = mainList.copy()
        realTop3 = []
        while(len(realTop3) < 3):
                tempMax =  0
                index = 0
                for i in range(0, len(comparisonList)):
                        if comparisonList[i]["num"] > tempMax:
                                tempMax = comparisonList[i]["num"]
                                index = i
                realTop3.append(comparisonList[index])
                del comparisonList[index]
        dictOfDegrees = {
                "devices" : [realTop3[0]["value"], realTop3[1]["value"], realTop3[2]["value"]],
                "url" : [realTop3[0]["url"], realTop3[1]["url"], realTop3[2]["url"]],
                "image" : [realTop3[0]["img"], realTop3[1]["img"], realTop3[2]["img"]],
        }

        return dictOfDegrees

def changeProfilePicture(request):
        template_name = "changeProfilePicture.html"
        user = request.COOKIES.get("CPUSVAL")  
        password = request.COOKIES.get("CPPWVAL")  
        
        where = db.collection(u'users').where(u'username', u'==', user)
        where2 = where.where(u'password', u'==', password).stream()
        finalObj = None
        template_vars = {}
        nickname = ""
        for doc in where2:
                
                finalObj = doc.to_dict()
        #user variable holds value of current user
        #if there is user
        if finalObj:
                #nickname variable holds user nickname string
                nickname = finalObj.get("name")
        else:
                return HttpResponseRedirect("/home")
        if request.method == 'POST': 
                image = request.FILES['image']
                thumb_width = 150
                imagePil = Image.open(image)
                width, height = imagePil.size
                if width != height or width != 175:
                        return render(request, template_name , {"error": "wrong measurements", "name" : nickname}) 
                im_thumb = crop_center(imagePil, thumb_width, thumb_width)
                public_uri = None
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                name = image.name
                name = name.replace(" ", "%20")
                for doc in where2:
                        finalObj = doc.to_dict()
                if finalObj:
                        if finalObj.get("imageUrl"):
                                bucket.delete_blob(finalObj.get("imageUrl")[1:])
                        public_uri = Upload.upload_image(image, user+"/" + image.name)
                        finalObj = db.collection(u'users').document(user)
                        finalObj.set({
                                u'imageUrl' : "/images/profilePictures/"+user+"/" + name,       
                        },  merge=True) 
                width, height = imagePil.size
                print("width  : " + str(width), "height : " + str(height))
                if width == height and width == 175:
                        return HttpResponse("<img src='%s'/>" % (public_uri))
                else:
                        return render(request, template_name , {"error": "wrong measurements", "name" : nickname}) 
        return render(request, template_name, {"name" : nickname})

def importantDates(request):
        importantDatesObj = {
                "allEvents" : 
                        [       {
                                        "name" : "Early Decision Application window" ,
                                        "dates" : ['2020-10-01', '2020-11-01', '2020-11-02''2020-11-03', '2020-11-04', '2020-11-05', '2020-11-06', '2020-11-07', '2020-11-08', '2020-11-09', '2020-11-10', '2020-11-11', '2020-11-12', '2020-11-13', '2020-11-14', '2020-11-15', '2021-10-01', '2021-11-01', '2021-11-02', '2021-11-03', '2021-11-04','2021-11-05', '2021-11-06', '2021-11-07', '2021-11-08', '2021-11-09', '2021-11-10', '2021-11-11', '2021-11-12', '2021-11-13', '2021-11-14', '2021-11-15', '2022-10-01', '2022-11-01', '2022-11-02', '2022-11-03', '2022-11-04', '2022-11-05', '2022-11-06', '2022-11-07', '2022-11-08', '2022-11-09', '2022-11-10', '2022-11-11', '2022-11-12', '2022-11-13', '2022-11-14', '2022-11-15', '2023-10-01', '2023-11-01', '2023-11-02', '2023-11-03', '2023-11-04', '2023-11-05', '2023-11-06', '2023-11-07', '2023-11-08', '2023-11-09', '2023-11-10', '2023-11-11', '2023-11-12', '2023-11-13', '2023-11-14', '2023-11-15', '2024-10-01', '2024-11-01', '2024-11-02', '2024-11-03', '2024-11-04', '2024-11-05', '2024-11-06', '2024-11-07', '2024-11-08', '2024-11-09', '2024-11-10', '2024-11-11', '2024-11-12', '2024-11-13', '2024-11-14', '2024-11-15'],
                                        "color" : "#70d7c7"
                                
                        },
                                {
                                        "name" : "Regular Decision Application opens" ,
                                        "dates" : ["2021-01-01", "2025-01-01" , "2024-01-01", "2023-01-01", "2022-01-01"],
                                        "color" : "#cc66ff"
                                
                        },
                                {
                                        "name" : "The Common App opens" ,
                                        "dates" : ["2020-08-01", "2021-08-01", "2022-08-01", "2023-08-01", "2024-08-01"],
                                        "color" : "#ff6666"
                                
                        },
                                {
                                        "name" : "SAT Testing Day" ,
                                        "dates" : ["2020-08-29", "2020-09-26", "2020-10-03", "2020-11-07", "2020-12-05", "2021-03-13", "2021-05-08", "2021-06-05"],
                                        "color" : "#99ff66"
                                
                        },
                        {
                                        "name" : "ACT Testing Day",
                                        "dates" : ["2020-10-17", "2020-10-24", "2020-10-25", "2021-02-06", "2021-04-17", "2021-06-12", "2021-07-17"],
                                        "color" : "#efdc10"
                                
                        }
                ]

        }
        return JsonResponse(importantDatesObj)

def mobileChangeProfilePicture(request):
        template_name = "mChangeProfilePicture.html"
        user = request.COOKIES.get("CPUSVAL")  
        password = request.COOKIES.get("CPPWVAL")  
        
        where = db.collection(u'users').where(u'username', u'==', user)
        where2 = where.where(u'password', u'==', password).stream()
        finalObj = None
        template_vars = {}
        nickname = ""
        for doc in where2:
                
                finalObj = doc.to_dict()
        #user variable holds value of current user
        #if there is user
        if finalObj:
                #nickname variable holds user nickname string
                nickname = finalObj.get("name")
        else:
                return HttpResponseRedirect("/home")
        if request.method == 'POST': 
                image = request.FILES['image']
                thumb_width = 150
                imagePil = Image.open(image)
                width, height = imagePil.size
                if width != height or width != 175:
                        return render(request, template_name , {"error": "wrong measurements", "name" : nickname}) 
                im_thumb = crop_center(imagePil, thumb_width, thumb_width)
                public_uri = None
                where = db.collection(u'users').where(u'username', u'==', user)
                where2 = where.where(u'password', u'==', password).stream()
                finalObj = None
                name = image.name
                name = name.replace(" ", "%20")
                for doc in where:
                        finalObj = doc.to_dict()
                if finalObj:
                        if finalObj.get("imageUrl"):
                                bucket.delete_blob(finalObj.get("imageUrl")[1:])
                        public_uri = Upload.upload_image(image, user+"/" + image.name)
                        finalObj = db.collection(u'users').document(user)
                        finalObj.set({
                                u'imageUrl' : "/images/profilePictures/"+user+"/" + name,       
                        },  merge=True) 
                width, height = imagePil.size
                print("width  : " + str(width), "height : " + str(height))
                if width == height and width == 175:
                        return HttpResponse("<img src='%s'/>" % (public_uri))
                else:
                        return render(request, template_name , {"error": "wrong measurements", "name" : nickname}) 
        return render(request, template_name, {"name" : nickname})

def collegeSupplies(request):
        blob = bucket2.blob('Supplies.json')
        supplies = json.loads(blob.download_as_string(client=None))
        return JsonResponse(supplies)

def collegeSupplies2():

        blob = bucket2.blob('Supplies.json')
        supplies = json.loads(blob.download_as_string(client=None))
        return supplies

def adminCollegeSupplies(request):
        template_name = "adminSuppliesPage.html"
        postTemplate = "postAdminSupplies.html"
        user = request.COOKIES.get("CPUSVAL")  
        password = request.COOKIES.get("CPPWVAL") 
        where = db.collection(u'users').where(u'username', u'==', user)
        where2 = where.where(u'password', u'==', password).stream()
        finalObj = None
        for doc in where2:
                finalObj = doc.to_dict()
        if finalObj:
                if finalObj.get("admin") == True:
                        if request.method == 'POST': 
                                additions = request.POST.get("additions")
                                additions = json.loads(additions)
                                print(additions)
                                blob = bucket2.blob('Supplies.json')
                                supplySet = set()
                                supplies = json.loads(blob.download_as_string(client=None))
                                for product in supplies["main"]:
                                        supplySet.add(product["name"])
                                for product in additions["main"]:
                                        if product["name"] not in supplySet:
                                                supplies["main"].append(product)
                                                supplySet.add(product["name"])
                                blob = bucket2.blob('Supplies.json')
                                blob.upload_from_string(
                                        data=json.dumps(supplies),
                                        content_type='application/json'
                                )
                                return render(request, postTemplate)
                        return render(request, template_name)
                else:
                        return HttpResponseRedirect("/home")
        else:
                return HttpResponseRedirect("/home")

def mobileAdminCollegeSupplies(request):
        user = request.COOKIES.get("CPUSVAL")  
        password = request.COOKIES.get("CPPWVAL") 
        template_name = "mAdminSuppliesPage.html"
        postTemplate = "mPostAdminSupplies.html"
        where = db.collection(u'users').where(u'username', u'==', user)
        where2 = where.where(u'password', u'==', password).stream()
        finalObj = None
        for doc in where2:
                finalObj = doc.to_dict()
        if finalObj:
                if finalObj.get("admin") == True:
                        if request.method == 'POST': 
                                additions = request.POST.get("additions")
                                additions = json.loads(additions)
                                blob = bucket2.blob('Supplies.json')
                                supplySet = set()
                                supplies = json.loads(blob.download_as_string(client=None))
                                for product in supplies["main"]:
                                        supplySet.add(product["name"])
                                for product in additions["main"]:
                                        if product["name"] not in supplySet:
                                                supplies["main"].append(product)
                                                supplySet.add(product["name"])
                                blob = bucket2.blob('Supplies.json')
                                blob.upload_from_string(
                                        data=json.dumps(supplies),
                                        content_type='application/json'
                                )
                                return render(request, postTemplate)
                        return render(request, template_name)
                else:
                        return HttpResponseRedirect("/mobile/home")
        else:
                return HttpResponseRedirect("/mobile/home")

def collegeSuppliesView(request):
        supplies = collegeSupplies2()
        returningStr = ""
        for elem in supplies["main"]:
                returningStr += ("<div class='container'>"+ 
                "<div>"+
                    "<img class='image' src = " + elem["image"] + "/>"+
                "</div>"+
                "<div>"+
                    "<div class='inner'>" +
                        "<div>"+
                            "<h1 class='title'>"+
                                elem["name"]+
                            "</h1>"+
                        "</div>"+
                        "<div class='priceDiv'>"+
                            "<h1 class='price'>"+
                                elem["price-range"]+
                            "</h1>"+
                        "</div>"+
                    "</div>"+
                    "<div>"+
                        "<p class='description'>"+
                            elem["description"] + 
                        "</p>"+
                    "</div>"+
                "</div>"+
            "</div>")
        template_name = "collegeSupplies.html"
        blob = bucket2.blob('Supplies.json')
        template_vars = json.loads(blob.download_as_string(client=None))
        return render(request, template_name, {"body" : json.dumps(template_vars)})

def mCollegeSuppliesView(request):
        template_name = "mCollegeSupplies.html"
        return render(request, template_name)

def knowSuppliesView(request):
        template_name = "knowSupplies.html"

        return render(request, template_name)

def mKnowSuppliesView(request):
        template_name = "mKnowSupplies.html"
        return render(request, template_name)

def colleges():
        blob = bucket2.blob("collegeJSON.json")
        obj = json.loads(blob.download_as_string(client=None))
        return obj

def collegesListAPI(request):
        if request.method == "GET": 
                return JsonResponse(colleges())

def buyOrSell(request):
        template_name = "buyOrSell.html"
        return render(request, template_name, { "colleges" : json.dumps(colleges())})

def sellingPage(request, college):
        collegeData = db.collection(u'colleges').document(college).get().to_dict()
        print("\n\n" + college + "\n\n")
        user = request.COOKIES.get("CPUSVAL")  
        password = request.COOKIES.get("CPPWVAL")  
        userObj = db.collection(u'users').document(user).get().to_dict()
        if userObj:
                userObj = userObj if userObj.get("password") == password else None  
        if userObj:
                if request.method == "GET":
                        if collegeData:
                                if not userObj.get("collegeAttended"):
                                        userObjCpy = db.collection(u'users').document(user)
                                        userObjCpy.set({
                                                "collegeAttended" : college,
                                                "listings" : []
                                        }, merge = True)
                                template_name = "sellingPage.html"
                                return render(request, template_name, {"college" : college, "formalCollege" : seperateByUpperCase(college), "listingAmount" : 5 - len(userObj.get("listings"))})
                        else:
                                return HttpResponseRedirect("../buyOrSell")
                else:
                        listingSet = set()
                        for elem in userObj.get("listings"):
                                listingSet.add(elem["listing"])
                        allowed = len(userObj.get("listings")) < 5 and request.POST.get("listing") not in listingSet
                        image1 = None
                        image2 = None
                        image3 = None
                        image4 = None

                        if allowed:
                                image1 = processImage(request.FILES["listingImage1"], user,  request.POST.get("listing"), 1)
                                image2 = processImage(request.FILES.get("listingImage2"), user, request.POST.get("listing"), 2)
                                image3 = processImage(request.FILES.get("listingImage3"), user, request.POST.get("listing"), 3)
                                image4 = processImage(request.FILES.get("listingImage4"), user, request.POST.get("listing"), 4)

                        data = {
                                "author" : request.POST.get("person"),
                                "host" : user,
                                "listing" : request.POST.get("listing"),
                                "description" : request.POST.get("description"),
                                "price" : request.POST.get("price"),
                                "images" : [image1, image2, image3, image4],
                                "college" : college
                        }
                        
                        collegeItems = None
                        if collegeData:
                                collegeItems = collegeData.get("items")
                                if allowed:
                                        collegeItems.append(data)
                        else:
                                collegeItems = [data]
                        collegeDataCpy = db.collection(u'colleges').document(college)
                        collegeDataCpy.set({
                                "items" : collegeItems
                        }, merge = True)
                        
                        if allowed:
                                userObj.get("listings").append(data)
                                userObjCpy = db.collection(u'users').document(user)
                                userObjCpy.set({
                                        "listings" : userObj.get("listings")
                                }, merge = True)

                        return HttpResponseRedirect("../sold/"+college)
        else:
                return HttpResponseRedirect("../login")
def processImage(image, user, listingName, num):
        returnVal = None
        try:
                print("opening the image fasho")
                pil_img = Image.open(image)
                returnVal = io.BytesIO()
                print("NOT IO")
                newsize = (400, 400) 
                pil_img.resize(newsize)
                try:
                        print("maybe saving")
                        pil_img.save(returnVal, 'jpeg', quality = 80)
                except:
                        pil_img.save(returnVal, 'png', quality = 80)
                print("before close")
                pil_img.close() 
                try:
                        print("next try catch")
                        imageName = "images/listings/" + user + "/" + listingName + str(num)
                        imageName = removeSymbols(imageName, True)
                        blob = bucket.blob(imageName)
                        blob.upload_from_string(returnVal.getvalue(), content_type='image/jpeg')
                        imageName = "/" + imageName
                        returnVal = imageName
                except Exception as exc:
                        returnVal = None
                        print("cannot upload")
                        print(exc)
        except Exception as e:
                returnVal = None
                print( e)
        return returnVal
def seperateByUpperCase(incoming):
        returnedString = ""
        count = 0
        for char in incoming:
                count += 1
                if char.isupper() and count != 1 and count != len(incoming):
                        returnedString += " " + char
                else:
                        returnedString += char
        return returnedString

def soldPage(request, college):
        template_name = "soldPage.html"
        return render(request, template_name, {"college" : college})

def buyingPage(request, college):
        template_name = "buyingPage.html"
        collegeData = db.collection(u'colleges').document(college).get().to_dict()
        if collegeData:
                items = collegeData.get("items")
                return render(request, template_name, {"items" : json.dumps({"main" : items}), "collegeName" : seperateByUpperCase(college)})
        else:
                return HttpResponseRedirect("../buyOrSell")
def updatedWebMessaging(request):
        if request.method == "GET":
                user = request.GET.get("user")
                recipient  = request.GET.get("recipient") if request.GET.get("recipient") else None
                userObj = db.collection(u'users').document(user).get().to_dict()
                if request.GET.get("netIncomePw"):
                        if request.GET.get("netIncomePw") != userObj.get("password"):
                                userObj = None
                recipientUser = db.collection(u'users').document(recipient).get().to_dict()
                obj = json.loads(unquote(request.GET.get("obj"))) if request.GET.get("obj") else None
                recipientObj = None
                if recipient:
                        recipientObj = obj.copy()
                        recipientObj["sender"] =  not obj["sender"]
                print(obj)
                if userObj:
                        if request.method == "GET":
                                if not userObj.get("messages"):
                                        userObjCpy = db.collection(u'users').document(user)
                                        userObjCpy.set({
                                                "messages" : {"name" : userObj.get("name")}
                                        }, merge = True)
                                if recipient:
                                        if not recipientUser.get("messages"):
                                                recipientUserCpy = db.collection(u'users').document(recipient)
                                                recipientUserCpy.set({
                                                        "messages" : {"name" : recipientUser.get("name")}
                                                }, merge = True)
                                        if user in recipientUser.get("messages"):
                                                recipientUser.get("messages")[user]["messageList"].append(recipientObj)
                                                recipientUserCpy = db.collection(u'users').document(recipient)
                                                recipientUserCpy.set({
                                                        "messages" : recipientUser.get("messages")
                                                }, merge = True)
                                        else:
                                                #figure this out tommorrow
                                                recipientUser.get("messages")[user] = {}
                                                recipientUser.get("messages")[user]["messageList"] = [recipientObj]
                                                recipientUserCpy = db.collection(u'users').document(recipient)
                                                recipientUserCpy.set({
                                                        "messages" : recipientUser.get("messages")
                                                }, merge = True)
                                        if recipient in userObj.get("messages"):
                                                userObj.get("messages")[recipient]["messageList"].append(obj)
                                                userObjCpy = db.collection(u'users').document(user)
                                                userObjCpy.set({
                                                        "messages" : userObj.get("messages")
                                                }, merge = True)
                                        else:
                                                #figure this out tommorrow
                                                userObj.get("messages")[recipient] = {}
                                                userObj.get("messages")[recipient]["messageList"] = [obj]
                                                
                                                userObjCpy = db.collection(u'users').document(user)
                                                userObjCpy.set({
                                                        "messages" : userObj.get("messages")
                                                }, merge = True)
                                t1 = threading.Thread(target=deleteOldMessages, args=(userObj.get("messages"), user))
                                t1.start()
                                response =  JsonResponse(userObj.get("messages"))  
                                return response      


def newMessage(request):
        user = request.COOKIES.get("CPUSVAL")  
        password = request.COOKIES.get("CPPWVAL")  
        userObj = db.collection(u'users').document(user).get().to_dict()
        if userObj:
                userObj = userObj if userObj.get("password") == password else None  
        if userObj:
                if request.method == "GET":
                        recipient  = request.GET.get("recipient") if request.GET.get("recipient") else None
                        if not userObj.get("messages"):
                                userObjCpy = db.collection(u'users').document(user)
                                userObjCpy.set({
                                        "messages" : {"name" : userObj.get("name")}
                                }, merge = True)
                        template_name = "newMessage.html"
                        if recipient:
                                
                                messages =  userObj.get("messages")
                                if recipient in messages:
                                        messages = messages
                                else:
                                        if recipient != user:
                                                recipientUser = db.collection(u'users').document(recipient).get().to_dict()
                                                userObj.get("messages")[recipient] = {"name" : recipientUser.get("name")}
                                                userObj.get("messages")[recipient]["messageList"] = []
                                                userObjCpy = db.collection(u'users').document(user)
                                                userObjCpy.set({
                                                        "messages" : userObj.get("messages")
                                                }, merge = True)
                                        # recipientObj = obj.copy()
                                        # recipientObj["sender"] =  not obj["sender"]
                                        # if not recipientUser.get("messages"):
                                        #         recipientUserCpy = db.collection(u'users').document(recipient)
                                        #         recipientUserCpy.set({
                                        #                 "messages" : {"name" : recipientUser.get("name")}
                                        #         }, merge = True)
                                        # if user in recipientUser.get("messages"):
                                        #         recipientUser.get("messages")[user]["messageList"].append(recipientObj)
                                        #         recipientUserCpy = db.collection(u'users').document(recipient)
                                        #         recipientUserCpy.set({
                                        #                 "messages" : recipientUser.get("messages")
                                        #         }, merge = True)
                                        # else:
                                        #         #figure this out tommorrow
                                        #         recipientUser.get("messages")[user] = {}
                                        #         recipientUser.get("messages")[user]["messageList"] = [recipientObj]
                                        #         recipientUserCpy = db.collection(u'users').document(recipient)
                                        #         recipientUserCpy.set({
                                        #                 "messages" : recipientUser.get("messages")
                                        #         }, merge = True)
                                        # if recipient in userObj.get("messages"):
                                        #         userObj.get("messages")[recipient]["messageList"].append(obj)
                                        #         userObjCpy = db.collection(u'users').document(user)
                                        #         userObjCpy.set({
                                        #                 "messages" : userObj.get("messages")
                                        #         }, merge = True)
                                        # else:
                                        #         #figure this out tommorrow
                                        #         userObj.get("messages")[recipient] = {}
                                        #         userObj.get("messages")[recipient]["messageList"] = [obj]
                                                
                                        #         userObjCpy = db.collection(u'users').document(user)
                                        #         userObjCpy.set({
                                        #                 "messages" : userObj.get("messages")
                                        #         }, merge = True) 
                                response = render(request, template_name , { "messages" : json.dumps(userObj.get("messages")), "username" : user, "currentRecipient" : recipient})
                                return response

        else:
                return HttpResponseRedirect("../login")

def messengerPage(request):
        user = request.COOKIES.get("CPUSVAL")  
        password = request.COOKIES.get("CPPWVAL")  
        userObj = db.collection(u'users').document(user).get().to_dict()
        if userObj:
                userObj = userObj if userObj.get("password") == password else None  
        if userObj:
                if request.method == "GET":
                        if not userObj.get("messages"):
                                userObjCpy = db.collection(u'users').document(user)
                                userObjCpy.set({
                                        "messages" : {"name" : userObj.get("name")}
                                }, merge = True)
                        template_name = "messages.html"
                        return render(request, template_name, { "messages" : json.dumps(userObj.get("messages")), "username" : user}) 
        else:
                return HttpResponseRedirect("../login")

def deleteOldMessages(importedMessages, user):
        for key in importedMessages:
                print(importedMessages[key])
                importedList = importedMessages[key]["messageList"]
                if len(importedList) > 350:
                        reversedList = importedList.reverse()
                        while len(reversedList) > 300:
                                reversedList.pop()
                        importedMessages[key]["messageList"] = reversedList.reverse()
        userObj = db.collection(u'users').document(user)
        userObj.set({
                "messages" : importedMessages
        }, merge= True)

def deleteListing(request):
        obj = json.loads(unquote(request.GET.get("obj")))
        user = request.COOKIES.get("CPUSVAL")
        user = db.collection("users").document(user).get().to_dict()
        collegeName = obj["college"]
        college = db.collection("colleges").document(collegeName).get().to_dict()
        if user:
                for image in obj["images"]:
                        if image:
                                print(image[1:])
                                blob = bucket.blob(image[1:])
                                blob.delete()
                if user.get("listings"):
                        if obj in user.get("listings"):
                                listings = user.get("listings")
                                listings.remove(obj)
                                userCpy = db.collection("users").document(request.COOKIES.get("CPUSVAL"))
                                userCpy.set({
                                        "listings" : listings
                                }, merge = True)
                if college.get("items"):
                        if obj in college.get("items"):
                                listings = college.get("items")
                                listings.remove(obj)
                                collegeCpy = db.collection("colleges").document(collegeName)
                                collegeCpy.set({
                                        "items" : listings
                                }, merge = True)
                return JsonResponse({"main" : user.get("listings")})
        else: 
                JsonResponse({[]})

def deleteListingApp(request):
        obj = json.loads(unquote(request.GET.get("obj")))
        user = request.GET.get("user")
        userName = user
        user = db.collection("users").document(user).get().to_dict()
        # if request.GET.get("netIncomePw"):
        #                 if request.GET.get("netIncomePw") != user.get("password"):
        #                         user = None
        collegeName = obj["college"]
        college = db.collection("colleges").document(collegeName).get().to_dict()
        if user:
                for image in obj["images"]:
                        if image:
                                print(image[1:])
                                blob = bucket.blob(image[1:])
                                try:
                                        blob.delete()
                                except:
                                        print("deletion failed")
                if user.get("listings"):
                        if obj in user.get("listings"):
                                listings = user.get("listings")
                                listings.remove(obj)
                                userCpy = db.collection("users").document(userName)
                                userCpy.set({
                                        "listings" : listings
                                }, merge = True)
                if college.get("items"):
                        if obj in college.get("items"):
                                listings = college.get("items")
                                listings.remove(obj)
                                collegeCpy = db.collection("colleges").document(collegeName)
                                collegeCpy.set({
                                        "items" : listings
                                }, merge = True)
                return JsonResponse({"main" : user.get("listings")})
        else: 
                JsonResponse({[]})
# def createEntities(request):
#         blob = bucket2.blob('users.json')
#         users = json.loads(blob.download_as_string(client=None))
#         for user in users["main"]:
#                 if user["username"] == "jasmine.patrick10@gmail.com":
#                         continue
#                 if user["username"].find("@") == -1:
#                         continue
#                 finalObj = db.collection(u'users').document(cipher(user["username"]))           
#                 finalObj.set({
#                         u'username' : cipher(user["username"]),
#                         u'password' : cipher(user["password"]) if user["password"] else "google",
#                         u'majors' : [],
#                         u'colleges' : [],
#                         u'collegeLinks' : [],
#                         u'collegeStates' : [],
#                         u'devices' : [],
#                         u'collegeCities' : [],
#                         u'name' : user["username"][0 : user["username"].index("@")] ,
#                         u'GPA' : 0,
#                         u'userACT' : 0,
#                         u'userSAT' : 0,
#                         u'userCity' : "someWhere",
#                         u'userState' : "whoKnows",
#                         u'imageUrl' : ""
                        
#                 },  merge=True)


def userPersonality(request):
        if request.method == "GET":
                user = request.COOKIES.get("CPUSVAL")
                userName = user
                user = db.collection("users").document(user).get().to_dict()
                password = request.COOKIES.get("CPPWVAL")
                required = ""
                if user : 
                        if user.get("personality"):
                                required = ""
                        else:
                                required = "required"
                template_name = "editUser.html"
                return render(request, template_name, { "colleges" : json.dumps(colleges()), "required" : required})
        else:
                user = request.COOKIES.get("CPUSVAL")
                userName = user
                user = db.collection("users").document(user).get().to_dict()
                password = request.COOKIES.get("CPPWVAL")
                if user:
                        if user.get("password") != password:
                                user = None
                chosenCollege = request.POST.get("chosen")
                majors = request.POST.get("majors").split(",") if request.POST.get("majors") else []
                minors = request.POST.get("minors").split(",") if request.POST.get("minors") else []
                hobbies = request.POST.get("hobbies").split(",") if request.POST.get("hobbies") else []
                peeves = request.POST.get("peeves").split(",") if request.POST.get("peeves") else []
                neatness = request.POST.get("neatness")
                partyPerson = request.POST.get("partyPerson")
                healthy = request.POST.get("healthy")
                likes = request.POST.get("likes").split(",") if request.POST.get("likes") else []
                image1 = None
                image2 = None
                image3 = None
                if user : 
                        if request.FILES.get("image1"):
                                image1 = processImage(request.FILES["image1"], userName, 1)
                        if request.FILES.get("image2"):
                                image2 = processImage(request.FILES.get("image2"), userName, 2)
                        if request.FILES.get("image3"):
                                image3 = processImage(request.FILES.get("image3"), userName, 3)

                        data = {
                                "college" : chosenCollege,
                                "majors" : majors,
                                "minors" : minors,
                                "hobbies" : hobbies,
                                "peeves" : peeves,
                                "likes" : likes,
                                "neatness" : True if neatness == "Yes" else False,
                                "partyPerson" : True if partyPerson == "Yes" else False,
                                "healthy" : True if healthy == "Yes" else False,
                                "images" : [image1, image2, image3]
                        }
                        print(data)
                        if user.get("personality"):
                                personality = user.get("personality")
                                personality["college"] = chosenCollege if chosenCollege else personality["college"]
                                personality["majors"] = majors if majors else personality["majors"]
                                personality["minors"] = minors if minors else personality["minors"]
                                personality["hobbies"] = hobbies if hobbies else personality["hobbies"]
                                personality["peeves"] = peeves if peeves else personality["peeves"]
                                personality["likes"] = likes if likes else personality["likes"]
                                personality["neatness"] = data["neatness"] if neatness else personality["neatness"]
                                personality["partyPerson"] = data["partyPerson"] if partyPerson else personality["partyPerson"]
                                personality["healthy"] = data["healthy"] if healthy else personality["healthy"]
                                personality["images"] = data["images"] if image1 else personality["images"]
                                userCpy = db.collection("users").document(userName)
                                userCpy.set({
                                        "personality" : personality
                                }, merge = True)
                        else:
                                userCpy = db.collection("users").document(userName)
                                userCpy.set({
                                        "personality" : data
                                }, merge = True)
                        return HttpResponseRedirect('../findOtherStudents/'+user.get("personality").get("college"))
                else:
                        return HttpResponseRedirect('../login')
def processImage(image, user, num):
        returnVal = None
        try:
                print("opening the image fasho")
                pil_img = Image.open(image)
                returnVal = io.BytesIO()
                print("NOT IO")
                newsize = (400, 400) 
                pil_img.resize(newsize)
                try:
                        print("maybe saving")
                        pil_img.save(returnVal, 'jpeg', quality = 80)
                except:
                        pil_img.save(returnVal, 'png', quality = 80)
                print("before close")
                pil_img.close() 
                try:
                        print("next try catch")
                        imageName = "images/personality/" + user + "/"  + "userImage"+ str(num)
                        imageName = removeSymbols(imageName, True)
                        blob = bucket.blob(imageName)
                        blob.upload_from_string(returnVal.getvalue(), content_type='image/jpeg')
                        imageName = "/" + imageName
                        returnVal = imageName
                except Exception as exc:
                        returnVal = None
                        print("cannot upload")
                        print(exc)
        except Exception as e:
                returnVal = None
                print( e)
        return returnVal    

def findOtherStudents(request, college):
        user = request.COOKIES.get("CPUSVAL")
        userName = user
        user = db.collection("users").document(user).get().to_dict()
        password = request.COOKIES.get("CPPWVAL")
        if user:
                if user.get("password") != password:
                        user = None
        if user:
                template_name = "showStudents.html"
                return render(request, template_name, {"collegeName" : seperateByUpperCase(college)})
        else:
                return HttpResponseRedirect("../login")

def findStudentsWebAPI(request):
        user = request.COOKIES.get("CPUSVAL")
        userName = user
        user = db.collection("users").document(user).get().to_dict()
        password = request.COOKIES.get("CPPWVAL")
        where = db.collection("users").where(u'personality.college', u'==', user.get("personality")["college"]).stream()
        returnedObj = {"main" : []}
        for doc in where:
                tempDoc = doc.to_dict()
                returnedObj["main"].append(
                        {
                                "name" : tempDoc.get("name"),
                                "host" : doc.id,
                                "personality" : tempDoc.get("personality")
                        }
                )
        return JsonResponse(returnedObj)

def removeSymbols(s, overload):
    for c in s:
        if ((not c.isalpha()) and (not c.isnumeric()) and not "/") or (c is " "):
            s = s.replace(c, "")
    return s

def isContained(char):
    var = ["a", "b", "c", "f", "y"]
    for x in range(0, len(var)):
        if char == var[x]:
            return True
    return False

def cypher(stringVal):
    sentVar = ""
    start = 0
    for x in range(0, len(stringVal)):
        if isContained(stringVal[x]):
            sentVar += chr(int(float(stringVal[start: x])*2))
            start = x+1
    return sentVar

def cipher2(stringVal):
    sentVar = ""
    arr = ["a", "b", "c", "f", "y"]
    for c in stringVal:
        sentVar += str(float(ord(c))/2)
        sentVar += random.choice(arr)
    return sentVar


def compute_hash(s):
  p = 31
  m = 1e9+9
  hash_value = 0
  p_pow = 1
  for c in s:
    if c != ' ':
      hash_value = (hash_value + (ord(c) - ord(' ') + 1) * p_pow) % m
    p_pow = (p_pow*p) % m
  return int(hash_value)

s = "@example01"

def cipher(s):
  hexString = hex(compute_hash(s))
  empty = ""
  for c in hexString:
    empty += (c+s[3].upper())
  return empty[4:]

def set_cookie(response, key, value, days_expire = 1):
  if days_expire is None:
    max_age = 24 * 60 * 60  #one year
  else:
    max_age = days_expire * 24 * 60 * 60 
  expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
  response.set_cookie(key, value, max_age=max_age, expires=expires)
  #, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None