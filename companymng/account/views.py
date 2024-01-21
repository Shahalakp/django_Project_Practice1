from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('hello world')

def luminar(request):
    return HttpResponse('welcome to luminar')

def land(request):
    return render(request,"landing.html")

def logi(request):
    return render(request,"login.html")

def regis(request):
    return render(request,"registration.html")

def sample(request):
    data="luminar technolab"
    status=False
    student=[
        {"name":"Shahala","age":23,"class":"bsc cs"},
        {"name":"Shalu","age":20,"class":"bca"},
        {"name":"adhil","age":22,"class":"bsc phy"}
    ]
    return render(request,"sample.html",{"viewdata":data,"status":status,"student_list":student})

def employee(request):
    employee=[
        {"id":1,"name":"Ajith","phone":9876654438,"Dept":"Technical"},
        {"id":2,"name":"sajith","phone":9876623478,"Dept":"Technical"},
        {"id":3,"name":"deepak","phone":9876656749,"Dept":"Technical"},
        {"id":4,"name":"Arun","phone":9394854438,"Dept":"Technical"},
        {"id":5,"name":"varun","phone":9837654438,"Dept":"Technical"}
    ]
    return render(request,"employees.html",{"employee_list":employee})

def home(request):
    return render(request,"home.html")
