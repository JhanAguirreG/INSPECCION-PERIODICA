from django import forms
from .models import InspeccionDiaria


class InspeccionForm(forms.ModelForm):
    class Meta:
        model = InspeccionDiaria
        exclude = ['institucion', 'pdf']