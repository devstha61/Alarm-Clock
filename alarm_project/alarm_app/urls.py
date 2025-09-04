from django.urls import path
from . import views


urlpatterns = [
    path('', views.alarm_list, name='alarm_list'),
    path('<int:pk>/delete/', views.delete_alarm, name='delete_alarm'),
    path('<int:pk>/toggle/', views.toggle_alarm, name='toggle_alarm'),
    ]