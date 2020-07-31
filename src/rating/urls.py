from django.conf.urls import url
from . import views
#from django.contrib import admin

from .views import (
            DoctorRatingAjaxView
            )


app_name = 'doctor'

urlpatterns = [

    #function for user registration

    url(r'^book_appointment/$', DoctorRatingAjaxView.as_view(), name='ajax_rating'),



]


