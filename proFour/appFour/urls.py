from django.urls import path
from . import views

app_name = 'appFour'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('other/', views.other, name='other'),
]
