from django.contrib import admin
from django.urls import path, include

from DjangoPrometheus import views

app_name = 'Prometheus'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('article/<int:pk>', views.article, name='article')
]
