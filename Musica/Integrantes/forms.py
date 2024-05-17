from django import forms
from .models import Musico

class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = ['nombre', 'instrumento', 'genero_primario', 'genero_secundario']

