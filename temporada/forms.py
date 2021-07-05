from seriado.models import Seriado
from django import forms
from .models import Temporada

class TemporadaForm(forms.ModelForm):
    imageFile = forms.FileField(required=False)
    class Meta:
        model = Temporada
        
        fields = ('numero','imagemFile', 'seriado_id')
        widgets = {
            'numero': forms.TextInput(attrs={
            'class': "form-control"
            }),
        }