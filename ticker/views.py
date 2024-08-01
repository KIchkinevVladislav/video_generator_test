import os
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from .forms import TickerTexForm
from .utils import TitleMixin
from .creater_video_ticker import create_video_ticker


class IndexView(TitleMixin, TemplateView):
    template_name = 'ticker/index.html'
    title = 'Video generator'


class TickerView(TitleMixin, TemplateView):
    template_name = 'ticker/ticker_generator.html'
    title = 'Создание видео'

    def get(self, request):
        form = TickerTexForm()
        return render(request, self.template_name, {'form': form, 'title': self.title})

    def post(self, request):
        form = TickerTexForm(request.POST)
        if form.is_valid():
            ticker_text = form.save()
            filename = 'new_video_ticker.mp4'
            video_path = create_video_ticker(ticker_text.text, filename)
            
            with open(video_path, 'rb') as video_file:
                response = HttpResponse(video_file.read(), content_type='video/mp4')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            os.remove(video_path)
            return response

        return render(request, self.template_name, {'form': form, 'title': self.title})
