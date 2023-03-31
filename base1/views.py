from django.shortcuts import render

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

from django.http import HttpResponse
from .models import Database1

def my_view(request):
    data = Database1.objects.all()
    output = '_'.join([f"{encode(d.login)}-{str(d.date).replace('-', '.')}" for d in data])

    return HttpResponse(output)


# from django.http import HttpResponse
# from .models import Database1
#
#
# def my_view(request):
#     data = Database1.objects.all()
#     rows = []
#     for d in data:
#         row = f"<tr><td>{d.name}</td><td>{d.date}</td></tr>"
#         rows.append(row)
#     headers = "<tr><th>Name</th><th>Date</th></tr>"
#
#     table = f"<table>{headers}{''.join(rows)}</table>"
#     return HttpResponse(table)