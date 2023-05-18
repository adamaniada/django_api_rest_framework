from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse


def index(request):
    return render(request, "django_api_rest_framework/index.html", context={"date" : datetime.today()})

@login_required
def profile(request):
    return render(request, 'users/profile.html')