import django_filters
from .models import *

class PotFilter(django_filters.FilterSet):
    class Meta:
        model=Pots
        fields = ['pot_dispo','pot_owner','pot_price']

class ClientFilter(django_filters.FilterSet):
    class Meta:
        model=Clients
        fields = ['client_name','client_last_name','client_phone']