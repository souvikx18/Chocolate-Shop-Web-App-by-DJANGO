from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    context={"variable1":"Dinu is lawra lassan","variable2":"Bide is padaku"}
    return render(request, 'index.html',context)


def about(request):
    context={"variable1":"Dinu is lawra lassan","variable2":"Bide is padaku"}
    return render(request, 'about.html')

def services(request):
    context={"variable1":"Dinu is lawra lassan","variable2":"Bide is padaku"}
    return render(request, 'services.html')

def contact(request):
    context={"variable1":"Dinu is lawra lassan","variable2":"Bide is padaku"}
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email') 
        message=request.POST.get('message')
        contact=Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contact.html')