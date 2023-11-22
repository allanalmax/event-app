# myapp/urls.py
from django.urls import path
from .views import index, create_event, show_data

app_name = 'eventapp'

urlpatterns = [
    path('', index, name='index'),
    path('create_event/', create_event, name='create_event'),
    path('show_data/', show_data, name='show_data'),
]
