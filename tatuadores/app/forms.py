from django import forms
from app.models import tatuadores

class tatuadorForm(forms.ModelForm):
    class Meta:
        model=tatuadores
        fields='__all__'