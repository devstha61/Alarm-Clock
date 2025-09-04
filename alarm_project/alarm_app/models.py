from django.db import models
from django.contrib.auth.models import User


class Alarm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(help_text='24h time (HH:MM)')
    label = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['time']


def __str__(self):
    return f"{self.user.username} @ {self.time} ({'on' if self.is_active else 'off'})"