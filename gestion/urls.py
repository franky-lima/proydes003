from django.urls import path
from . import views

urlpatterns = [
    path('', views.entidad_list, name='entidad_list'),
    path('entidad/<int:pk>/', views.entidad_detail, name='entidad_detail'),
]
