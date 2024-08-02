from django import forms

from .models import TickerText


class TickerTexForm(forms.ModelForm):
    COLOR_CHOICES_TEXT = [
        ('white', 'Белый'),
        ('black', 'Черный'),
        ('random', 'Случайный')
    ]
    COLOR_CHOICES_FRAME = [
        ('white', 'Белый'),
        ('black', 'Черный'),
    ]    
    SIZE_CHOICES = [(i, f'{i}px') for i in range(100, 721, 20)]

    text_color = forms.ChoiceField(choices=COLOR_CHOICES_TEXT, label='Цвет текста')
    frame_color = forms.ChoiceField(choices=COLOR_CHOICES_FRAME, label='Цвет фона')
    video_size = forms.ChoiceField(choices=SIZE_CHOICES, label='Размер видео', initial=100)

    class Meta:
        model = TickerText
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'maxlength': 64,
                'placeholder': 'Введите текст'
            })
        }
