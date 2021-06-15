from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def homepageview(request):
    return render(request,'home.html')
def exppageview(request):
    return render(request,'exp.html')
def certipageview(request):
    return render(request,'certi.html')
def projectpageview(request):
    return render(request,'project.html')
def contactpageview(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        msg=request.POST['msg']
        print(name,phone,email,msg)
        contact=Contact(name=name, phone=phone, email=email, msg=msg)
        contact.save()

    return render(request,'contact.html')

