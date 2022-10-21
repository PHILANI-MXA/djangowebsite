from django.urls import path
from . import views
import polls

urlpatterns = [
    path('', views.index, name='index'),
]