from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

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

