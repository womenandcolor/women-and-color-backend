from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings


# Create your views here.
def home(request):
    context = { 'frontend_base_url': settings.FRONTEND_BASE_URL }
    return render(request, 'frontend/home.html', context)


@login_required
def profile(request):
    context = { 'frontend_base_url': settings.FRONTEND_BASE_URL }
    return render(request, 'frontend/home.html', context)
