from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tennis-index'),
    # path('about/', views.about, name='tennis-about'),
    # path('<id>/', views.show, name='adoption-show'), # route for /adoption/:id
    # to accept only numbers as id param
    path('<int:id>/', views.show, name='tennis-show')
]
