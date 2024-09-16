from django.shortcuts import render
from django.http import HttpResponse
from .models import services
# Create your views here.

def Home(request):
    
    s1 = services()
    s2 = services()
    s3 = services()
    
    #S1 created
    s1.name = "Web App Developement"
    s1.des = "We develope customizes web applications"
    s1.price = 75000
    s1.status = True
    
    #S2 created
    s2.name = "Mobile App Developement"
    s2.des = "We develope customizes Mobile applications"
    s2.price = 40000
    s2.status = False
    
    #S3 created
    s3.name = "Graphic Designing"
    s3.des = "We develope Graphic designs for Promotionals etc..,"
    s3.price = 20000
    s3.status = True
    
    allServices = [s1, s2, s3]
    
    
    founder = "John Wesley"
    address= "Kolkata"
    data = {
        "name" : founder,
        "add" : address,
        "all" : allServices
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

