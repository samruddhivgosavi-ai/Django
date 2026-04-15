from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students,document
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

        s=Students(name=n,email=em,password=ps,contact=cn,city=ci)
        s.save() # to insert data

        return redirect("/viewstudents")
    else:
        return redirect("/registration")

def viewstudents(request):
    data=Students.objects.all().order_by('-id')
    return render(request,"viewstudents.html",{'data':data})

def delete(request,id):
    Students.objects.filter(id=id).delete()
    return redirect("/viewstudents")

def update(request,id):
    mydata=Students.objects.filter(id=id)
    return render(request,"updatestudents.html",{'i':mydata})

def profileupdate(request):
    if request.method=="POST":
        id = request.POST["id"]

        s = Students.objects.get(id=id)

        s.name = request.POST["name"]
        s.email = request.POST["email"]
        s.password = request.POST["password"]
        s.contact = request.POST["contact"]
        s.city = request.POST["city"]

        s.save()

        return redirect("/viewstudents")
    
def login(request):
    return render(request,"login.html")

def logincheck(request):
    if request.method=="POST":
        em = request.POST["email"]
        ps = request.POST["password"]

        data = Students.objects.filter(email=em,password=ps)

        if data:
            request.session["username"]=em # session start
            return redirect("/dashboard/")
        else:
            return redirect("/login/")
    else:
        return HttpResponse("Invalid Login")
    
def dashboard(request):
    if request.session.get("username") is not None:     # session get
        email = request.session.get("username")
        data = Students.objects.filter(email=email)
        return render(request,"dashboard.html",{'data':data})
    else:
        return redirect("/login/")

def logout(request):
    del request.session["username"] # session end
    return redirect("/login")

def addcookie(res):
    res=HttpResponse("cookies set")
    res.set_cookie("name","xyz")
    return res

def viewcookie(request):
    n=request.COOKIES["name"]
    return HttpResponse("Name is %s"%n)

def fileupload(request):
    return render(request,"fileupload.html")

def filesave(request):
    if request.method=="POST":
        em = request.POST["email"]
        ph = request.FILES["photo"]

        d = document(email=em, photo=ph)

        d.save()
        return HttpResponse("Uploaded Successfully")
    else:
        return HttpResponse("Upload Failed")

