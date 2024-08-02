from django.db import models


class TickerText(models.Model):
    """
    Class describing the fields of the "TickerText" object 
    in the database
    """    
    text = models.CharField(max_length=32, verbose_name='Текст в бегущей строке')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания видео')

    def __str__(self) -> str :
        return f'Текст в бегущей строке: {self.text}'

    class Meta():
        verbose_name = 'Текст в бегущей строке'
        verbose_name_plural = 'Тексты записанные в бегущие строки'
