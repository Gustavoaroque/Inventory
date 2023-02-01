from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms  import ClientsForm
from django.db import connection


# Create your views here.
def home(request):
    lotes = Pots.objects.all()
    clients = Clients.objects.all()
    return render(request, 'lotification/home.html',{'lotes':lotes,'clients':clients})

def user_list(request):
    clients = Clients.objects.all()
    context = {'clients':clients}
    return render(request, 'lotification/user_list.html',context)

def customers_list(request):
    clients = Clients.objects.all()
    context = {'clients':clients}
    return render(request, 'lotification/customer_list.html',context)

def lote_list(request):
    lotes = Pots.objects.all()
    return render(request, 'lotification/lote_list.html',{'lotes':lotes})

def lote_info(request,pk):
    # pass
    # query= '''SELECT * FROM lotification_Clients WHERE id = 1'''
    # cursor = connection.cursor()
    # cursor.execute(query)
    # print(cursor)
    cursor = Pots.objects.get(id = pk)
    all_Pots = Pots.objects.all()
    # x = cursor.payments_set.all()
    pagos = Payments.objects.filter(Payment_Pot = cursor.id)
    
    print(pagos)
    context = {'lote':cursor, 'pagos':pagos}
    return render(request, 'lotification/lote_info.html',context)

def new_lote(request):
    return render(request,'lotification/new_lote.html')

def new_client(request):
    # pass
    form = ClientsForm()

    if request.method == 'POST':
        # print(request.POST)
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientes')
    context = {'form':form}
    return render(request,'lotification/new_client.html',context)


# def list(request):
#     lotes = Lote.objects.all()

#     return render(request,'lotification/list.html',{'lotes':lotes})





