from django.shortcuts import render
from .models import login
# Create your views here.


def login_user (request):

    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = login(email=email,password=password)
        # if data.is_valid():
        data.save()


    return render(request,"login.html")