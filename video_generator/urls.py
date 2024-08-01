from django.contrib import admin
from django.urls import include, path

from ticker.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'), 
    path('ticker/', include('ticker.urls', namespace='ticker'))   
]
