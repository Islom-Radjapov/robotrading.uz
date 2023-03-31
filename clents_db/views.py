from django.shortcuts import render
from django.http import HttpResponse
from .models import Database

def encode(login):
    result = ""
    for x in login:
        if x == "0":
            result += "i"
        elif x == "1":
            result += "s"
        elif x == "2":
            result += "l"
        elif x == "3":
            result += "o"
        elif x == "4":
            result += "m"
        elif x == "5":
            result += "b"
        elif x == "6":
            result += "e"
        elif x == "7":
            result += "k"
        elif x == "8":
            result += "r"
        elif x == "9":
            result += "a"
    return result



def my_view(request):
    data = Database.objects.all()
    output = '_'.join([f"{encode(d.login)}-{encode(str(d.date.year))}.{encode(str(d.date.month))}.{encode(str(d.date.day))}" for d in data])
    return HttpResponse(output)