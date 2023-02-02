from django.forms import ModelForm
from .models import Clients, Pots, Payments

class ClientsForm(ModelForm):
    class Meta:
        model = Clients 
        fields = '__all__'

class PotForm(ModelForm):
    class Meta:
        model = Pots
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payments
        fields = ['Payment_amount','Payment_Pot']