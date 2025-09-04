from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from alarm_app import views as alarm_views

urlpatterns = [
    path('', lambda request: redirect('alarms/')),  
    path('admin/', admin.site.urls),
    path('alarms/', include('alarm_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', alarm_views.signup_view, name='signup'),
]
