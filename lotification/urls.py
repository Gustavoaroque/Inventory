from django.urls import path
from . import views

from django.urls import path, include

urlpatterns = [
    path("home", views.home,name="home"),
    path("user_list", views.user_list),
    path("clientes",views.customers_list,name='lients'),
    path("lote", views.lote_list,name="lote"),
    path("lote_info/<str:pk>/", views.lote_info),
    path("nuevo_lote", views.new_lote),
    path("nuevo_cliente", views.new_client),
    
]
