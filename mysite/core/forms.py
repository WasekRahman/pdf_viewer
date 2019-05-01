from django import forms

from .models import *


class PDFForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ('title', 'pdf')
