from django import forms
from .models import UsuarioModel

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioModel
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'sexo': 'Sexo',
            'email': 'Email',
            'dtNasc': 'Data de nascimento',
            'renda': 'Renda',
        }