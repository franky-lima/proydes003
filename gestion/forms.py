from django import forms
from .models import Entidad

class EntidadForm(forms.ModelForm):
    class Meta: 
        model = Entidad
        fields = ('razonSocial', 'ruc','direccionFiscal','contacto','telefono','correo','cuenta',)
     