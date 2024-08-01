from django import forms

from .models import TickerText


class TickerTexForm(forms.ModelForm):
    class Meta:
        model = TickerText
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'maxlength': 64,
                'placeholder': 'Введите текст'
            })
        }
