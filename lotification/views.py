from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms  import *
from django.db import connection
from .filters import *

# Create your views here.
def home(request):
    lotes = Pots.objects.all()
    clients = Clients.objects.all()

    clients_count = Clients.objects.all().count()
    pots_count = Pots.objects.all().count()
    context = {'lotes':lotes,'clients':clients,'numero_clientes':clients_count,'numero_lotes':pots_count}   
    return render(request, 'lotification/home.html',context)

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
    myFilter = PotFilter(request.GET, queryset=lotes) 

    lotes = myFilter.qs  
    context = {'lotes':lotes,'filtro':myFilter}
    return render(request, 'lotification/lote_list.html',context)

def lote_info(request,pk):
    cursor = Pots.objects.get(id = pk)
    form = PaymentForm(initial={'Payment_Pot':cursor})
    # pass
    # query= '''SELECT * FROM lotification_Clients WHERE id = 1'''
    # cursor = connection.cursor()
    # cursor.execute(query)
    # print(cursor)
   
    all_Pots = Pots.objects.all()
    # x = cursor.payments_set.all()
    pagos = Payments.objects.filter(Payment_Pot = cursor.id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lote')
    context = {'lote':cursor, 'pagos':pagos,'form_payment':form}
    return render(request, 'lotification/lote_info.html',context)

def new_lote(request):
    form = PotForm()
    if request.method == 'POST':
        form = PotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lote')
    context = {'form':form}
    return render(request,'lotification/new_lote.html',context  )

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





