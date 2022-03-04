from django.urls import reverse_lazy
from django.shortcuts import redirect, render

def index_page_not_logged(request):
    success_url = reverse_lazy('templates/account/login.html')