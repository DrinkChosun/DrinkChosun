from django.urls import path
from . import views

app_name = 'alcohols'

urlpatterns = [
    path('', views.index, name='index'),
]