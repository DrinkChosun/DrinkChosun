from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('index/', views.index, name='index'),
]
