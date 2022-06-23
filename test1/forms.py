from django import forms
from .models import Double


class DoubleForm(forms.ModelForm):
    class Meta:
        model = Double
        fields = ['value']
