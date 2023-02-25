from django.urls import path
from . import views
from wkhtmltopdf.views import PDFTemplateView
from django.urls import path, include

urlpatterns = [
    path("home", views.home,name="home"),
    path("user_list", views.user_list, name='user_list'),
    path("clientes",views.customers_list,name='clients'),
    path("lote", views.lote_list,name="lote"),
    path("lote_info/<str:pk>/", views.lote_info),
    path("nuevo_lote", views.new_lote),
    path("nuevo_cliente", views.new_client),
    path("login",views.login_page, name="login"),
    path("logOut",views.log_out, name="logOut"),
    path("register", views.register, name="register"),
    path("lote_info/<str:pk>/gen/",views.gen_EXCEL),
    path("lote_info/<str:pk>/cotizacion",views.pdf_report, name='pdf_report'),
    path("lote_info/<str:pk>/edit",views.edit_pot, name='edit_pot'),
    path("lote_info/<str:pk>/delete",views.delete_pot, name='delete_pot'),
    path("client/<str:pk>/edit",views.edit_client, name='edit_pot'),
    path("client/<str:pk>/delete",views.delete_client, name='delete_pot'),
    path("lote_info/<str:pk>/payment_edit/<str:pk_pay>",views.edit_payment, name='edit_paymentt'),
    path("lote_info/<str:pk>/payment_delete/<str:pk_pay>",views.delete_payment, name='delete_payment'),
    path("user_info/<str:pk>",views.edit_user, name='edit_user'),
    path("user/<str:pk>/delete",views.delete_user, name='delete_user'),
]
