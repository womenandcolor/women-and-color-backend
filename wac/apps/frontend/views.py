from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}
    return render(request, 'frontend/home.html', context)


@login_required
def profile(request):
    context = {}
    return render(request, 'frontend/home.html', context)
