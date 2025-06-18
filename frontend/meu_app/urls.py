from django.urls import path, include
from . import views

app_name = 'meu_app'

urlpatterns = [
    path('', views.home, name='home'), 
    path('dashboard/', views.dashboard, name='dashboard'),# Rota para a página inicial do projeto
    path('login/', views.login_view, name='login'),
    path('Register/', views.register, name='cadastro'),
]