from django import forms
from .models import Data

class DataForms(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'