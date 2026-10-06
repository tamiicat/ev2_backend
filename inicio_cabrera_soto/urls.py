from django.urls import path
from . import views

app_name = "temas"
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tema1/', views.tema1, name='tema1'),
    path('tema2/', views.tema2, name='tema2'),
]