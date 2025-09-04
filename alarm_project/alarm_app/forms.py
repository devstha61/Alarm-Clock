from django import forms
from .models import Alarm


class AlarmForm(forms.ModelForm):
    class Meta:
        model = Alarm
        fields = ["time", "label", "is_active"]
        widgets = {
            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'label': forms.TextInput(attrs={'placeholder': 'Label (optional)'}),
            }