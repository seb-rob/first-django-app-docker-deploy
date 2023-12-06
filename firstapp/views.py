from django.shortcuts import render
from datetime import date

# Create your views here.
from django.http import HttpResponse

def index(request):
    template = "<html>"\
        "This is your first view" \
        "</html>"
    return HttpResponse(content = template)

def get_date(request):
    today = date.today()
    template = "<html>"\
        "Todays date is {}" \
        "</html>".format(today)
    return HttpResponse(content = template)