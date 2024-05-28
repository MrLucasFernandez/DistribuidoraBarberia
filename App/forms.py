from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


#Formulario de contacto
class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]


#Formulario para agregar un servicio        
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'


