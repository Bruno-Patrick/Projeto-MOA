from django.shortcuts import redirect, render
from django.urls import reverse_lazy

def iflogin(request):
    return render(request, "templates\account\login.html")