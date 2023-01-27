from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    lotes = Lote.objects.all()
    return render(request, 'lotification/home.html',{'lotes':lotes})

def user_list(request):
    return render(request, 'lotification/user_list.html')

def customers_list(request):
    return render(request, 'lotification/customer_list.html')

def lote_list(request):
    return render(request, 'lotification/lote_list.html')

def lote_info(request):
    return render(request, 'lotification/lote_info')

def new_lote(request):
    return render(request,'lotification/new_lote.html')

def new_client(request):
    return render(request,'lotification/new_client.html')


# def list(request):
#     lotes = Lote.objects.all()

#     return render(request,'lotification/list.html',{'lotes':lotes})





