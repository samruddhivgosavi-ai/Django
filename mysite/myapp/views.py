from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    # return render(request,"home.html")
    return HttpResponse("Homepage")

def sub(request):
    if request.method=="POST":
        n1 = request.POST["num1"]
        n2 = request.POST["num2"]


        res = int(n1) - int(n2)

        return HttpResponse("Subtraction=%d"%res)
    else:
        return HttpResponse("Failed")

