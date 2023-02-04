from django.forms import ModelForm
from .models import Clients, Pots, Payments
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
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

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']