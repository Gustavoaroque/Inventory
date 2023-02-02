import django_filters
from .models import *

class PotFilter(django_filters.FilterSet):
    class Meta:
        model=Pots
        fields = ['pot_dispo','pot_owner','pot_price']