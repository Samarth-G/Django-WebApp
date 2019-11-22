from django.urls import path
from . import views

appName = 'polls'

urlpatterns = \
[
    path('', views.index, name='home')
]