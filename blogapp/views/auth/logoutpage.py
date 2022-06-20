from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.

def logoutPage(request):
    logout(request)

    return redirect('home')

