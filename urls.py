
from django.conf.urls import url
from django.contrib import admin

from reception.views import (
    CreateReception, CreateReceptionRedirectView, reception_success,
    doctor_free_times)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', CreateReceptionRedirectView.as_view()),
    url(r'^reception/new/', CreateReception.as_view()),
    url(r'^reception/success/', reception_success),
    url(r'^reception/get-free-time-choices/', doctor_free_times)
]
