from django.shortcuts import render
from django.views.generic.base import TemplateView

from .forms import TickerTexForm
from .utils import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'ticker/index.html'
    title = 'Video generator'


class TickerView(TitleMixin, TemplateView):
    template_name = 'ticker/ticker_generator.html'
    title = 'Создание видео'

    def get(self, request):
        form = TickerTexForm()
        return render(request, self.template_name, {'form': form, 'title': self.title})
