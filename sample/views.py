from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import courses

# Create your views here.

def validate(request):
    return render(request, 'validate.html')

def signup(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        email = request.POST['email']
        username = request.POST['username']
        p1 = request.POST['p1']
        p2 = request.POST['p2']
        # test1 = [fn, ln, email, username, p1, p2]
        # print(test1)
        if p1 == p2:
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already taken")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("Email already exists")
            else:
                user = User.objects.create_user(first_name=fn,last_name=ln,username=username,email=email, password=p1)
                user.save()
                return (HttpResponse("User Created successfully"))
        else:
            return HttpResponse("Password not matched...........")
    
    else:
        return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')


def course(request):
    all_courses = courses.objects.all()
    data1 = {
        'data' : all_courses
    }
    return render(request,'webpage.html',data1)

def Home(request):
    founder = "John Wesley"
    address= "Kolkata"
    data = {
        "name" : founder,
        "add" : address
    }
    return render(request,'index.html',data)


def result(request):
    num1 = int(request.POST['n1'])
    num2 = int(request.POST['n2'])
    operator = request.POST['operator']
    if(operator == "+"):
        result = num1 + num2
    elif(operator == "-"):
        result = num1 - num2
    elif(operator == "*"):
        result = num1 * num2
    elif(operator == "/"):
        result = num1 / num2
    elif(operator == "**"):
        result = num1 ** num2
    elif(operator == "%"):
        result = num1 % num2 
    data2 = {
        "num1" : num1,
        "num2" : num2,
        "result" : result
    }
    return render(request, 'result.html', data2)

