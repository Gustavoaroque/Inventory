from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms  import *
from django.db import connection
from .filters import *
from django.contrib.auth.forms import UserCreationForm
import django_excel as excel
from datetime import datetime
from openpyxl import Workbook
from django.http.response  import HttpResponse
from io import BytesIO
# from reportlab.lib.pagesizes import A4, cm
from reportlab.pdfgen import canvas
from django.http import FileResponse
from django.conf import settings


# Create your views here.
def home(request):
    clients = Clients.objects.raw('SELECT * FROM lotification_Clients LIMIT 5')
    clients_count = Clients.objects.all().count()

    lotes = Pots.objects.raw('SELECT * FROM lotification_Pots LIMIT 5')
    pots_count = Pots.objects.all().count()

    
    context = {'lotes':lotes,'clients':clients,'numero_clientes':clients_count,'numero_lotes':pots_count}   
    return render(request, 'lotification/home.html',context)

def user_list(request):
    clients = Clients.objects.all()
    context = {'clients':clients}
    return render(request, 'lotification/user_list.html',context)

def customers_list(request):
    clients = Clients.objects.all()
    
    cliente_filtrado = ClientFilter(request.GET, queryset=clients)
    clients = cliente_filtrado.qs
    print(cliente_filtrado)
    context = {'clients':clients,'filtro':cliente_filtrado}
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
    area = cursor.pot_large * cursor.pot_width
    # params = {'area:'}
    abono_total = 0

    if pagos:
        for pago in pagos:
            abono_total +=pago.Payment_amount
            print(pago.Payment_amount)
    else:
        print('No hay pagos')

    print(str(abono_total))
    restante = cursor.pot_price - abono_total
    context = {'lote':cursor, 'pagos':pagos,'form_payment':form, 'area':area, 'abono':abono_total, 'restante':restante,'id_pot':pk}

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


def login(request):
    return render(request, 'lotification/login.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'lotification/register.html',context)

# def list(request):
#     lotes = Lote.objects.all()

#     return render(request,'lotification/list.html',{'lotes':lotes})



def gen_EXCEL(request, pk):
    cursor = Pots.objects.get(id = pk)
    pagos = Payments.objects.filter(Payment_Pot = cursor.id)
    wb = Workbook()
    ws = wb.active
    ws['B1'] = "Reporte pagos"
    ws.merge_cells('B1:D1')
    ws['B3'] = 'ID de Pago'
    ws['C3'] = 'Monto ($)'
    ws['D3'] = 'Fecha'
    contador = 4
    for pago in pagos:
        ws.cell(row = contador, column = 2).value = pago.id
        ws.cell(row = contador, column = 3).value = pago.Payment_amount
        ws.cell(row = contador, column = 4).value = "{0:%d-%m-%Y}".format(pago.Payment_date)
        contador+=1
    today = datetime.now()
    strToday = today.strftime("%Y%m%d")
    nombre_archivo = "Reporte_pagos_Lote"+str(cursor.id)+ strToday+".xlsx"
    response = HttpResponse(content_type="application/ms-excel")
    content = "attachment; filename = {0}".format(nombre_archivo)
    response['Content-Disposition']=content
    wb.save(response)
    return response 

    # sheet = excel.pe.Sheet(export)
    # sheet.group_rows_by_column(0)
    # print(export)
    # return excel.make_response(sheet,"csv",file_name="results de pago-"+strToday+".csv")


def pdf_report(request, pk):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100,100,'Hello World')
    # img = str(settings.BASE_DIR) + "\static\img\logo_sin_fondo.png"
    # print(img)
    # p.drawImage(img,300,300,300,300)
    p.showPage()
    p.save()
    buffer.seek(0)
    today = datetime.now()
    strToday = today.strftime("%Y%m%d")
    nombre_archivo = "Cotizacion_"+ strToday +".pdf"
    return FileResponse(buffer,as_attachment=True,filename=nombre_archivo)


