import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import RedirectView

from reception.forms import ReceptionForm
from reception.models import Reception


class CreateReception(CreateView):
    """Представление создания карточки на прием к мастеру."""

    model = Reception
    form_class = ReceptionForm
    success_url = '/reception/success'


def reception_success(request):
    """Представление успешного создания карточки на прием к мастеру."""
    return render(request, 'reception/reception_success.html')


class CreateReceptionRedirectView(RedirectView):
    """Представление для перенаправления на страницу создания карточки."""

    url = 'reception/new'


def master_free_times(request):
    """Представление для получения свободного времени приема мастера на дату."""
    master_id = int(request.GET['master_id'])
    date = datetime.datetime.strptime(request.GET['date'], "%d.%m.%Y")

    busy_times = Reception.objects.filter(
        master=master_id, date=date).values_list('time', flat=True)

    if busy_times.exists():
        free_time = [t for t in Reception.TIME_CHOICES
                     if t[0] not in busy_times]
    else:
        free_time = list(Reception.TIME_CHOICES)

    return HttpResponse(
        json.dumps({'free_time': free_time}), content_type='application/json')
