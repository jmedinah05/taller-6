from attr import fields
from django import forms
from .models import TipoDocumento

class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = '__all__'
        