from django.urls import path

from . import views

urlpatterns = [
    path('', views.my_form, name='my_form'),
]
