from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,"WebApp/home.html")

def services(request):
    return render(request,"WebApp/services.html")

def store(request):
    return render(request,"WebApp/store.html")

def blog(request):
    return render(request,"WebApp/blog.html")

def contact(request):
    return render(request,"WebApp/contact.html")
