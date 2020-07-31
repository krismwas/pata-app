import datetime
from django.shortcuts import render, get_object_or_404
from .models import BookAppoinment
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import JsonResponse, Http404
# from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
# from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def thankYou(request):
    context = {}
    return render(request, "book_appointment/thanks.html", context)


class book_appointment(View):
    model = get_user_model()

    def get(self, request, *args, **kwargs):
        dr_id = kwargs.get("id")
        try:
            doc_obj = self.model.objects.get(id=dr_id)
        except:
            raise Http404
        context={"doc_obj":doc_obj}
        return render(request, "book_appointment/book_appointment.html", context)

    def post(self, request, *args, **kwargs):
        if not request.POST.get("date_entered"):
            raise Http404
        if not self.request.user.is_authenticated:
            return redirect("account_login")
        dr_id = kwargs.get("id")
        # apptmnt_dateobj = request.POST.get("date_entered")
        apptmnt_date = request.POST.get("date_entered")
        # apptmnt_date = str(apptmnt_date)
        # apptmnt_date = parse(apptmnt_date).strftime('%Y-%m-%d')
        apptmnt_date = datetime.datetime.strptime(apptmnt_date, '%d-%m-%Y')
        # print(apptmnt_date)
        # print(dr_id)
        try:
            dr_obj = self.model.objects.get(id=dr_id)
        except:
            raise Http404
        today = datetime.datetime.today()
        today = datetime.datetime(today.year, today.month, today.day)
        print("-----")
        print(today)
        print("-----")
        print("-----")
        print(apptmnt_date)
        print("-----")
        # day_ago = apptmnt_date - datetime.timedelta(days=1)
        # print(day_ago)
        if apptmnt_date < today:
            messages.add_message(request, messages.INFO, 'Past dates are not allowed!!')
            return render(request, "book_appointment/book_appointment.html")
        k = today + timedelta(days=7)
        if apptmnt_date > k:
            print(k)
            print("lll")
            messages.add_message(request, messages.INFO, 'You cant make appointment more than a week in advance!!')
            return render(request, "book_appointment/book_appointment.html")
        apptment_exists = BookAppoinment.objects.filter(patient=request.user, doctor=dr_obj ,appointment_datee=apptmnt_date).exists()
        if apptment_exists:
            messages.add_message(request, messages.INFO, 'Your appointment has already been processed')
            return render(request, "book_appointment/book_appointment.html")
            print(apptment_exists)

        bkobj = BookAppoinment.objects.filter(patient=request.user, doctor=dr_obj, appointment_datee__range=(today, k)).exists()
        print(bkobj)
        if bkobj:
            bk_obj_result = BookAppoinment.objects.filter(patient=request.user, doctor=dr_obj, appointment_datee__range=(today, k))
            for instance in bk_obj_result:
                instance.appointment_datee = apptmnt_date
                instance.save()
            messages.add_message(request, messages.INFO, 'Your appointment has been changed successfully')
            return HttpResponseRedirect(reverse("book_appointment:thanks"))
            print(bk_obj_result)

        bkappt_obj = BookAppoinment.objects.create(patient=request.user)
        bkappt_obj.appointment_datee = apptmnt_date
        bkappt_obj.save()
        bkappt_obj.doctor.add(dr_obj)

        # messages.add_message(request, messages.INFO, 'Hello world.')

        return HttpResponseRedirect(reverse("book_appointment:thanks"))

