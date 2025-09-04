from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Alarm
from .forms import AlarmForm


@login_required
def alarm_list(request):
    alarms = Alarm.objects.filter(user=request.user)


    if request.method == 'POST':
        form = AlarmForm(request.POST)
        if form.is_valid():
            alarm = form.save(commit=False)
            alarm.user = request.user
            alarm.save()
            return redirect('alarm_list')
    else:
        form = AlarmForm()


    return render(request, 'alarm_app/alarm_list.html', {
        'alarms': alarms,
        'form': form,
    })


@login_required
def delete_alarm(request, pk):
    alarm = get_object_or_404(Alarm, pk=pk, user=request.user)
    if request.method == 'POST':
        alarm.delete()
    return redirect('alarm_list')


 @login_required
def toggle_alarm(request, pk):
    alarm = get_object_or_404(Alarm, pk=pk, user=request.user)
    if request.method == 'POST':
        alarm.is_active = not alarm.is_active
        alarm.save()
    return redirect('alarm_list')




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('alarm_list')
    else:
         form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})