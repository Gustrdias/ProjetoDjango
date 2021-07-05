from django import forms
from .models import Seriado

class SeriadoForm(forms.ModelForm):
    imageFile = forms.FileField(required=False)
    class Meta:
        model = Seriado
        fields = ('nome', 'genero', 'avaliacao','assistido','imagemFile','user_id')
        widgets = {
            'nome': forms.TextInput(attrs={
            'class': "form-control"
            }),
            'avaliacao': forms.NumberInput(attrs={
            'class': "form-control"
            }),
            'assistido': forms.TextInput(attrs={
            'class': "form-control"
            }),
        }