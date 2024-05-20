# myapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user:
        return render(request, 'main_page.html')
    return render(request, 'home.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')