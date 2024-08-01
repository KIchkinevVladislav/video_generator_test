from django.db import models


class TickerText(models.Model):
    """
    Class describing the fields of the "TickerText" object 
    in the database
    """    
    text = models.CharField(max_length=256, verbose_name='Текст записанный в бегущей строке')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания видео')

    def __str__(self) -> str :
        return f'Текст записанный в бегущей строке: {self.text}'

    class Meta():
        verbose_name = 'Тект в бегущей строке'
        verbose_name_plural = 'Тексты записанные в бегущей строке'
