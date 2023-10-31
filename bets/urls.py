from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('matches/', views.match_list, name='matches'),
]
