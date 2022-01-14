from django.urls import path

from . import views

urlpatterns = [
    path('user', views.get_users, name='get_users'),
    path('user/<int:user_id>', views.get_user_by_id, name='get_user_by_id'),
    path('calculate', views.calculate, name='calculate'),
    path('correlation', views.correlation, name='correlation')
]