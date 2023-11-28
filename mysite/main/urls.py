from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='category'),
    path('players/<int:id>/', views.player, name='players')
]
