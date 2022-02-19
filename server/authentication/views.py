from django.shortcuts import render, redirect, HttpResponse

def home(request):
    return render(request,'authentication/login.html')

def login(request):
    return render(request,'authentication/login.html')