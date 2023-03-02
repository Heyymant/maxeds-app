# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
  
# from django.contrib.auth.decorators import login_required

# def login(request):
#      retunrn render (request, login.html)


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    return render(request, 'login.html')
@login_required
def home(request):
    return render(request, 'home.html')