from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tennis-index'),
    path('player<int:player_id>/', views.show, name='tennis-show'),
    path('player/new/', views.create, name='create-player')
]
