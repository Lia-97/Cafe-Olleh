from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    if 'user' in request.session:
        context={'user_name':request.session.get('user')}
        return render(request,'home.html',context)
    else:
        return render(request,'home.html')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return render(request,'home.html')