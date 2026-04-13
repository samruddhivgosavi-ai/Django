from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")
    #return HttpResponse("Homepage")

def sub(request):
    if request.method=="POST":
        n1 = request.POST["num1"]
        n2 = request.POST["num2"]


        res = int(n1) - int(n2)

        return HttpResponse("Subtraction=%d"%res)
    else:
        return HttpResponse("Failed")

def mul(request):
    if request.method=="POST":
        num1 = request.POST["first_number"]
        num2 = request.POST["second_number"]

        output = int(num1) * int(num2)

        return HttpResponse("Multiplication=%d"%output)
    else:
        return render(request,"arith.html")
    
def registration(request):
    return render(request,"registration.html")

def formsave(request):
    if request.method=="POST":
        n = request.POST["name"]
        em = request.POST["email"]
        ps = request.POST["password"]
        cn = request.POST["contact"]
        ci = request.POST["city"]

        s=Students()
        s.save() # to insert data

        return HttpResponse ("Registered Successfully")
    else:
        return HttpResponse ("Registration Failed")