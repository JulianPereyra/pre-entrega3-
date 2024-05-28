from django import forms
from .models import Musico
from .models import SolicitudUnirseBanda

class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = ['nombre', 'instrumento', 'genero_primario', 'genero_secundario']
        
class SolicitudUnirseBandaForm(forms.ModelForm):
    class Meta:
        model = SolicitudUnirseBanda
        fields = ['musico', 'banda', 'mensaje']


