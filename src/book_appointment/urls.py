from django.conf.urls import url
from . import views
from .views import book_appointment

from django.contrib import admin
# from .views import thankYou

app_name = 'book_appointment'

urlpatterns = [
    # url(r'^$', thankYou.as_view(), name='thanks'),
    url(r'^thanks/$', views.thankYou, name='thanks'),
    url(r'^(?P<id>\d+)/$', book_appointment.as_view(), name='bappointment'),

]



