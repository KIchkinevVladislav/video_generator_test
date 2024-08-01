from django.urls import path

from .views import TickerView

app_name = 'ticker'


urlpatterns = [
    path('', TickerView.as_view(), name='ticker_generator')
    ]