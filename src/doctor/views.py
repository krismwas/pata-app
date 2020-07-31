import datetime

from django.shortcuts import render, redirect
# from django.contrib.messages import constants as messages
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import View

from django.contrib.auth import get_user_model
from django.db.models import Avg, Count
from django.db import transaction
from django.http import Http404

from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.template import loader
# from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from django.urls import reverse


from rating.models import Rating
from . models import Profile, Clinic, ClinicPhotos, MyPatients, specialty, locationn, New_Specialty
from book_appointment.models import BookAppoinment
from .forms import (FormClinicUpdate, FormPatientUser, FormPatientProfile, FormDoctorUser, FormDoctorProfile, ClinicPhotoForm,
                    form_doctors_contact, formAddclinic, ProfilePhotoForm )

from pata.mixings import LoginRequiredMixing
from django.core.management.utils import get_random_secret_key

# def testcss(request):
#     return render(request, "test_css.html")


class PatientMobile(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        # print("--------------------------")
        print(request.POST)
        patient_mobile_no = request.POST.get("mobile_no")
        if patient_mobile_no is None:
            return JsonResponse({}, status=404)
        patient_mobile_no = patient_mobile_no.strip()

        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            patient_obj = self.model.objects.get(id=self.request.user.id)
            patient_obj.profile.mobile_no = patient_mobile_no
            patient_obj.save()
            data={"success":True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class DocMobileNo(View):
    model = get_user_model()
    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated():
            return JsonResponse({}, status=401)
        mobile_number = request.POST.get("mobile_no")
        if mobile_number is None:
            return JsonResponse({}, status=404)
        mobile_number = mobile_number.strip()
        # print(fname)
        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.profile.mobile_no = mobile_number
            doc_obj.save()
            data = {"success": True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class DocUserName(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)
        user_name = request.POST.get("username")
        if user_name is None:
            return JsonResponse({}, status=404)
        user_name = user_name.strip()
        # print(fname)
        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.username = user_name
            doc_obj.save()
            data = {"success": True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class PatientDob(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        doc_dob = request.POST.get("dob")
        doc_dob = parse(doc_dob).strftime('%Y-%m-%d')

        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            patient_obj = self.model.objects.get(id=self.request.user.id)
            patient_obj.profile.birth_date = doc_dob
            patient_obj.save()
            data = {"success": True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class PatientLastName(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        # print("--------------------------")
        print(request.POST)
        patient_lname = request.POST.get("last_name")
        if patient_lname is None:
            return JsonResponse({}, status=404)
        patient_lname = patient_lname.strip()

        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            patient_obj = self.model.objects.get(id=self.request.user.id)
            patient_obj.last_name = patient_lname
            patient_obj.save()
            data={"success":True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class PatientFirstName(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        print("--------------------------")
        print(request.POST)
        patient_fname = request.POST.get("first_name")
        if patient_fname is None:
            return JsonResponse({}, status=404)
        patient_fname = patient_fname.strip()

        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            patient_obj = self.model.objects.get(id=self.request.user.id)
            patient_obj.first_name = patient_fname
            patient_obj.save()
            data={"success":True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class PatientEmail(View):
    model = get_user_model()
    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated():
            return JsonResponse({}, status=401)

        # print(request.POST)
        patient_email = request.POST.get("email")
        if patient_email is None:
            return JsonResponse({}, status=404)
        patient_email = patient_email.strip()

        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            patient_obj = self.model.objects.get(id=self.request.user.id)
            patient_obj.email = patient_email
            patient_obj.save()
            data={"success":True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class PatientUsername(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated():
            return JsonResponse({}, status=401)

        # print(request.POST)
        patient_username = request.POST.get("username")
        if patient_username is None:
            return JsonResponse({}, status=404)
        patient_username = patient_username.strip()
        print("----------------------------------")

        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            patient_obj = self.model.objects.get(id=self.request.user.id)
            patient_obj.username = patient_username
            patient_obj.save()
            data={"success":True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class professionalBiography(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        # print(request.POST)
        professional_bio = request.POST.get("probio")
        if professional_bio is None:
            return JsonResponse({}, status=404)
        professional_bio = professional_bio.strip()

        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.profile.professional_biography = professional_bio
            doc_obj.save()
            data={"success":True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class ProfessionalAwards(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        # print(request.POST)
        professional_awards = request.POST.get("pawards")
        if professional_awards is None:
            return JsonResponse({}, status=404)
        professional_awards = professional_awards.strip()

        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.profile.professional_awards = professional_awards
            doc_obj.save()
            data={"success":True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class ProfessionalBoardCertifications(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        # print(request.POST)
        pboard_certifcation = request.POST.get("bcertification")
        if pboard_certifcation is None:
            return JsonResponse({}, status=404)
        pboard_certifcation = pboard_certifcation.strip()

        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.profile.board_certifications = pboard_certifcation
            doc_obj.save()
            data={"success":True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class ProfessionalMembership(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        # print(request.POST)
        professional_membership = request.POST.get("pmembership")
        if professional_membership is None:
            return JsonResponse({}, status=404)

        professional_membership = professional_membership.strip()
        # print()
        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.profile.professional_membership = professional_membership
            doc_obj.save()
            data={"success":True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class ProfessionalEducation(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        # print(request.POST)
        professional_education = request.POST.get("edu")
        if professional_education is None:
            return JsonResponse({}, status=404)
        professional_education = professional_education.strip()
        # print()
        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.profile.education = professional_education
            doc_obj.save()
            data={"success":True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class DocDob(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)
        # print("-------------------------------")
        # print(request.POST)

        doc_dob = request.POST.get("dob")
        print(doc_dob)
        doc_dob = parse(doc_dob).strftime('%Y-%m-%d')

        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.profile.birth_date = doc_dob
            doc_obj.save()
            data = {"success": True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class DocEmail(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)
        print("-------------------------------")
        print(request.POST)
        doc_email = request.POST.get("email")
        if doc_email is None:
            return JsonResponse({}, status=404)
        doc_email = doc_email.strip()
        # print(doc_email)
        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.email = doc_email
            doc_obj.save()
            data = {"success": True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class SecondName(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)
        # print("-------------------------------")
        # print(request.POST)
        sname = request.POST.get("sname")
        if sname is None:
            return JsonResponse({}, status=404)
        sname = sname.strip()
        # print(sname)
        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.profile.second_name = sname
            doc_obj.save()
            data = {"success": True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class LastName(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)
        # print("-------------------------------")
        # print(request.POST)
        lname = request.POST.get("lname")
        if lname is None:
            return JsonResponse({}, status=404)
        lname = lname.strip()
        # print(lname)
        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.last_name = lname
            doc_obj.save()
            data = {"success": True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class FirstName(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)
        # print("ooooooooooooooooooooooooooooooooooooo")
        # print(request.POST)
        fname = request.POST.get("fname")
        if fname is None:
            return JsonResponse({}, status=404)
        fname = fname.strip()
        # print(fname)
        user_obj = self.model.objects.filter(id=self.request.user.id).exists()
        if user_obj:
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.first_name = fname
            doc_obj.save()
            data = {"success": True}
            return JsonResponse(data)

        data = {}
        return JsonResponse(data)


class ClinicUpdate(LoginRequiredMixing, View):

    def get(self, request, *args, **kwargs):
        clinic_id = self.kwargs.get("pk")
        clinic_obj = Clinic.objects.get(id=clinic_id)

        form = FormClinicUpdate(clinic_id, instance=clinic_obj)
        context={"form":form}
        return render(request, "doctor/edit_clinic_new.html", context)

    def post(self, request, *args, **kwargs):
        clinic_id = self.kwargs.get("pk")
        clinic_obj = Clinic.objects.get(id=clinic_id)
        form = FormClinicUpdate(clinic_id, request.POST, instance=clinic_obj, )
        # print("momomomomomomomommoommom")
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "clinic edited successfully !!")

        context = {"form": form}
        return render(request, "doctor/edit_clinic_new.html", context)


class RegisterPractice(LoginRequiredMixing, View):
    model = get_user_model()

    def get(self, request, *args, **kwargs):
        if self.request.user.profile.doctor:
            # print("yeyyeyeye")
            return redirect(reverse("doctor:index"))
        form = form_doctors_contact()
        context = {
            "form": form
        }
        return render(request, "doctor/doctor_contact_form.html", context)

    def post(self, request, *args, **kwargs):
        user_id = self.request.user.id
        try:
            user_obj = self.model.objects.get(id=user_id)
        except:
            raise Http404
        # print(user_obj)
        form = form_doctors_contact(request.POST)
        if form.is_valid():
            clinic_name_entered = form.cleaned_data.get("clinic_name")
            location_entered = form.cleaned_data.get("location")
            clinic_names = Clinic.objects.filter(clinic_name=clinic_name_entered,
                                                 clinic_location__county=location_entered)
            if clinic_names.exists():
                try:
                    clinic_obj = Clinic.objects.get(clinic_name=clinic_name_entered,
                                                    clinic_location__county=location_entered)
                except:
                    raise Http404
                clinic_obj.user.add(user_obj)
                # existing_clinic.add(user_obj)
            if not clinic_names.exists():
                location = form.cleaned_data.get("location")
                user_obj.clinic_set.create(clinic_name=clinic_name_entered, clinic_location=location,
                                           owner=self.request.user)
            mobile_no_entered = form.cleaned_data.get("mobile_no")
            mobile_no_exists = self.model.objects.filter(profile__mobile_no=mobile_no_entered)
            print(user_obj.profile.mobile_no)
            if mobile_no_exists.exists() and user_obj.profile.mobile_no != int(mobile_no_entered):
                messages.add_message(request, messages.INFO, "Please enter a valid mobile number !!!")
                print("kamaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaau")
                return redirect(reverse("doctor:doctor_contact"))

            user_obj.first_name = form.cleaned_data.get("first_name")
            user_obj.profile.doctor = True
            user_obj.profile.mobile_no = form.cleaned_data.get("mobile_no")
            user_obj.save()

        return redirect(reverse("doctor:thanks"))


class NewSpecialty(View):

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)
        new_specialty = (request.POST.get("new_specialty")).strip()
        added_specialty = New_Specialty.objects.filter(doc=self.request.user, new_specialty=new_specialty).exists()
        if not added_specialty:
            New_Specialty.objects.create(doc=self.request.user, new_specialty=new_specialty)
            data={"success":True}
            return JsonResponse(data)
        if added_specialty:
            data={"success":"already"}
            return JsonResponse(data)


class PatientUnverification(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        p_id = request.POST.get("patient_id")
        patient_obj = self.model.objects.get(id=p_id)
        doc_obj = self.model.objects.get(id=self.request.user.id)

        doc_patients = doc_obj.mypatients_set.all()

        for instance in doc_patients:
            patients = instance.patients.all()
            for patient_instance in patients:
                instance.patients.remove(patient_obj)

        data={"success":True}
        return JsonResponse(data)


class dr_upload_profile_pic(LoginRequiredMixing, View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        # this two lines delete previous codes
        self.request.user.profile.profile_pic_thumbnails_set.all().delete()
        self.request.user.profile.photo.delete()

        form = ProfilePhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            doc_obj = self.model.objects.get(id=self.request.user.id)
            doc_obj.profile.photo = form.cleaned_data.get("photo")

            doc_obj.save()
            data = {'is_valid': True,}
            return JsonResponse(data)
        else:
            data = {}
            return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        context={}
        return render(request, "doctor/upload_doctor_profile_picture.html", context)


class profile_pic_delete(LoginRequiredMixing, View):
    def post(self, request, *args, **kwargs):
        self.request.user.profile.profile_pic_thumbnails_set.all().delete()
        self.request.user.profile.photo.delete()
        data = {}
        return JsonResponse(data)


class doctors_specitys(View):

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not self.request.user.is_authenticated:
            return JsonResponse({}, status=401)
        doc_specialtys = request.POST.getlist("your_specialtys[]")
        request.user.specialty_set.clear()
        for instance in doc_specialtys:
            try:
                specialty_obj = specialty.objects.get(specialty_name=instance)
            except:
                raise Http404
            print(specialty_obj)
            specialty_obj.user.add(self.request.user)
        success=True
        data={"success":success}
        return JsonResponse(data)


class doctors_specialty_selected(View):

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)
        doc_specialty = (request.POST.get("doc_specialty")).strip()
        if not doc_specialty:
            return JsonResponse({})
        doc_specialty = specialty.objects.filter(specialty_name=doc_specialty).exists()
        print(doc_specialty)
        if doc_specialty:
            doc_specialty = specialty.objects.filter(specialty_name=(request.POST.get("doc_specialty")).strip())
            # print("oooooooooooooooooooooooooooo")
            # print(doc_specialty)
            # print("oooooooooooooooooooooooooooo")
            for instance in doc_specialty:
                instance.user.add(self.request.user)
        success=True
        data={"success":success}
        return JsonResponse(data)


class DoctorSelecteClinicAjax(View):

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not self.request.user.is_authenticated:
            return JsonResponse({}, status=401)

        clinic_selected = request.POST.get("doc_selected_clinic")
        # print(clinic_selected.)
        try:
            clinic = Clinic.objects.get(clinic_name=clinic_selected)
        except:
            raise Http404

        clinic.user.add(self.request.user)
        success=True
        data = {"success":success}
        return JsonResponse(data)


class add_new_clinic(LoginRequiredMixing, View):

    def get(self, request, *args, **kwargs):
        form = formAddclinic()
        context={"form":form}
        return render(request, "doctor/add_new_clinic.html", context)

    def post(self, request, *args, **kwargs):
        form = formAddclinic(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            does_clinic_exist = Clinic.objects.filter(clinic_name=instance.clinic_name, clinic_location=instance.clinic_location)
            if does_clinic_exist.exists():
                form = formAddclinic()
                context = {"form": form}
                messages.add_message(request, messages.INFO, " a clinic with that name is registered !!")
                return render(request, "doctor/add_new_clinic.html", context)
            # print(does_clinic_exist)
            instance.owner = self.request.user
            instance.save()
            instance.user.add(self.request.user)

        return redirect(reverse("doctor:clinic_added_success"))


class doctor_clinics_name_update(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)
        success = False
        print(request.POST)
        doc_obj = self.model.objects.get(id=self.request.user.id)
        doc_clinics = request.POST.getlist("clinic_name[]")
        doc_obj.clinic_set.clear()
        for instance in doc_clinics:
            new_clinics = Clinic.objects.filter(clinic_name=instance)
            for clinic_instance in new_clinics:
                doc_obj.clinic_set.add(clinic_instance)
        success=True

        data = {
            "success":success
        }
        return JsonResponse(data)


class DelPicAjax(View):

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        print("9999999999999900000000000000000")
        pid_id = request.POST.get("pic_id")

        print(pid_id)
        try:
            pic_obj = ClinicPhotos.objects.filter(id=pid_id).delete()
        except:
            raise Http404
        pic_obj
        # print(pic_obj)
        data={}
        return JsonResponse(data)


class uploadClinicPhotosAjax(LoginRequiredMixing, View):

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404
        if not self.request.user.profile.doctor:
            raise Http404

        form = ClinicPhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            clinic_id = self.kwargs.get("id")
            try:
                clinic = Clinic.objects.get(id=clinic_id)
            except:
                raise Http404
            print("wwwwgggggggbbbbbbbbb--------")
            print(clinic)
            pics_count = clinic.clinicphotos_set.count()
            # print(pics_count)
            if pics_count >= 6:
                data={'maximum_pics':True}
                return JsonResponse(data)
            photo.clinic = clinic

            photo.save()
            data = {'is_valid': True, 'name': photo.photo.name, 'url': photo.photo.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


    def get(self, request, *args, **kwargs):
        clinic_id = self.kwargs.get("id")
        try:
            clinic = Clinic.objects.get(id=clinic_id)
        except:
            raise Http404
        context = {
            "clinic":clinic
            }
        return render(request, "doctor/upload_clinic_photos.html", context)


class clinicPhotosAjax(View):
    model = get_user_model()

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        clinics = request.user.clinic_set.all()

        doctors_clinics = loader.render_to_string('doctor/clinicPhotosList.html', {"clinics": clinics})

        data={
            "doctors_clinics":doctors_clinics
        }
        return JsonResponse(data)


class DoctorEditProfile(LoginRequiredMixing, View):
# class DoctorAjaxEditProfile(View):
    model = get_user_model()

    def get(self, request, *args, **kwargs):
        if not self.request.user.profile.doctor:
            raise Http404
        if not request.user.profile.doctor_activate:
            return redirect(reverse("doctor:thanks"))
        doc_obj = self.model.objects.get(id = self.request.user.id)
        reviews = doc_obj.doc_rated.all()
        docObjratingAVG = doc_obj.doc_rated.aggregate(Avg("rating_value"))

        thumbnail_sd = []
        thumbnail_micro = []
        clinic = doc_obj.clinic_set.first()
        if clinic:
            # print(clinic)
            for instance in clinic.clinicphotos_set.all():
                sd_thumbnails = instance.thumbnail_set.filter(type="sd")
                thumbnail_sd.append(sd_thumbnails)
                micro_thumbnails = instance.thumbnail_set.filter(type="micro")
                thumbnail_micro.append(micro_thumbnails)

        no_of_thumbnail_sd = len(thumbnail_sd)
        location_instances = locationn.objects.all()
        doc_profile_pic_sd = doc_obj.profile.profile_pic_thumbnails_set.filter(type="sd")
        # print(doc_profile_pic_sd)
        all_specialtys = specialty.objects.all()

        doc_specialtys = doc_obj.specialty_set.all()
        if not doc_specialtys.exists():
            messages.add_message(request, messages.INFO, "Please note that you will not be listed untill you enter your specialty !!!")

        if doc_specialtys.exists() and not doc_obj.last_name:
            messages.add_message(request, messages.INFO, "Please enter your last name !!")
        doc_clinic = doc_obj.clinic_set.all()

        all_clinics = Clinic.objects.all()

        clinics_you_own = Clinic.objects.filter(owner=self.request.user)

        context = {
                "clinics_you_own" : clinics_you_own,
                "all_clinics" : all_clinics,
                "doc_clinic" : doc_clinic,
                "doc_specialtys" : doc_specialtys,
                "all_specialtys" : all_specialtys,
                "doc_profile_pic_sd" : doc_profile_pic_sd,
                "location_instances" : location_instances,
                "no_of_thumbnail_sd": no_of_thumbnail_sd,
                "thumbnail_micro" : thumbnail_micro,
                "thumbnail_sd" : thumbnail_sd,
                "doc_obj" : doc_obj,
                "reviews" : reviews,
                "docObjratingAVG" : docObjratingAVG,

        }
        return render(request, "doctor/doctor_profile_edit.html", context)


class PatientVerification(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not self.request.user.profile.doctor:
            raise Http404
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)

        patient_id = request.POST.get("patient_id")
        try:
            patient_obj = self.model.objects.get(id=patient_id)
        except:
            return JsonResponse({}, status=404)
        try:
            dakitari = MyPatients.objects.get(dr=self.request.user)
            dakitari.patients.add(patient_obj)
        except MyPatients.DoesNotExist:
            # print("wewew")
            patients_wangu = MyPatients()
            patients_wangu.save()
            patients_wangu.patients.add(patient_obj)
            patients_wangu.dr.add(self.request.user)

        data = {
            "success":True,
            "p_id": patient_id
        }
        return JsonResponse(data)


class PatientHome(LoginRequiredMixing, View):
    model = get_user_model()

    def get(self, request, *args, **kwargs):
        print("jeez")
        if self.request.user.profile.doctor:
            print("steve austine")
            # raise Http404
            return redirect(reverse('doctor:doctor_profile'))
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        seven_days_from_today = today + datetime.timedelta(days=7)
        today_dr_appointments = BookAppoinment.objects.filter(patient=self.request.user).filter(
            appointment_datee=today).order_by("-id")

        all_dr_appointments = BookAppoinment.objects.filter(patient=self.request.user).order_by("-timestamp").exclude(
            appointment_datee__range=(today, seven_days_from_today))

        future_dr_appointments = BookAppoinment.objects.filter(patient=self.request.user, appointment_datee__range=(
        tomorrow, seven_days_from_today)).order_by("-timestamp")

        try:
            patient_obj = self.model.objects.get(id=request.user.id)
        except:
            raise Http404
        # print(patient_obj)

        context = {
            "future_dr_appointments": future_dr_appointments,
            "doc_appointments": all_dr_appointments,
            "today_dr_appointments": today_dr_appointments,
            "patient_obj" : patient_obj
        }

        return render(request, "doctor/patient_home.html", context)


class DoctorAppointment(LoginRequiredMixing, View):
    def get(self, request, *args, **kwargs):
        if not request.user.profile.doctor_activate:
            return redirect(reverse("doctor:thanks"))
        if not self.request.user.profile.doctor:
            raise Http404
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        # print("------")
        # print(tomorrow)
        # print("------")
        seven_days_from_today = today + datetime.timedelta(days=7)
        # print(seven_days_from_today)
        # today_min = datetime.datetime.combine(today, datetime.time.min)
        # today_max = datetime.datetime.combine(today, datetime.time.max)
        today_dr_appointments = BookAppoinment.objects.filter(doctor=self.request.user).filter(appointment_datee=today).order_by("-id")

        all_dr_appointments = BookAppoinment.objects.filter(doctor=self.request.user).order_by("-timestamp").exclude(appointment_datee__range=(today, seven_days_from_today))

        future_dr_appointments = BookAppoinment.objects.filter(doctor=self.request.user, appointment_datee__range=(tomorrow, seven_days_from_today)).order_by("-timestamp")

        context = {
            "future_dr_appointments" : future_dr_appointments,
            "doc_appointments" : all_dr_appointments,
            "today_dr_appointments" : today_dr_appointments
        }
        return render(request, "doctor/doctor_appointment.html", context)


class DoctorPatients(LoginRequiredMixing, View):
    model = get_user_model()

    def get(self, request, *args, **kwargs):
        if not request.user.profile.doctor_activate:
            return redirect(reverse("doctor:thanks"))
        if not self.request.user.profile.doctor:
            raise Http404
        my_patients_qs = self.request.user.mypatients_set.all()
        for instance in my_patients_qs:
            patients_qs = instance.patients.all()
            # for patient_instance in patients_qs:
            #     print(patient_instance)

            context = {
                "my_patients": patients_qs
            }
            return render(request, "doctor/doctor_patients.html", context)
        return render(request, "doctor/doctor_patients.html")


class ClinicPhotoss(View):
    template_name = "doctor/clinic_photos.html"

    def get(self, request, *args, **kwargs):
        clinic_id = kwargs.get("id")

        clinic_photos = ClinicPhotos.objects.filter(clinic_id =clinic_id)

        context = {
            "clinic_photos":clinic_photos
            }
        return render(request, "doctor/clinic_photos.html", context)


class ProfileDetailView(DetailView):
    model = get_user_model()
    template_name = "doctor/doctor_profile_detail.html"

    def get_context_data(self, *args, **kwargs):
        specialty_en = self.kwargs.get("specc")

        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        llll = obj.profile.doc_location
        # print(llll)
        user = self.request.user
        all_locations = locationn.objects.all()
        all_specialtys = specialty.objects.all()
        rating_avg = obj.doc_rated.aggregate(Avg("rating_value"))
        rating_pentage_avg = rating_avg["rating_value__avg"]

        micro_profile_pic = obj.profile.profile_pic_thumbnails_set.filter(type="micro")
        sd_profile_pic = obj.profile.profile_pic_thumbnails_set.filter(type="sd")
        k = len("Hekimadoctors directory for doctors dentists gynecologist surgeons etc")
        print("--------------")
        print(k)

        context["micro_profile_pic"] = micro_profile_pic
        context["sd_profile_pic"] = sd_profile_pic
        # new if self.request.user.is_authenticated():
        if self.request.user.is_authenticated:
            context["rating_yangu"] = obj.doc_rated.filter(user=user)
        context["rating_pentage_avg"] = rating_pentage_avg
        context["all_locations"] = all_locations
        context["all_specialtys"] = all_specialtys
        context["doc_object"] = obj
        context["doctor_clinics"] = obj.clinic_set.all()

        if self.request.user.is_authenticated:
            context["all_reviews"] = Rating.objects.filter(dr_rated=obj).exclude(user=user).order_by("-timestamp")
        if not self.request.user.is_authenticated:
            context["all_reviews"] = Rating.objects.filter(dr_rated=obj).order_by("-timestamp")

        return context

    def post(self, request, *args, **kwargs):
        all_locations = locationn.objects.all()
        all_specialities = specialty.objects.all()
        location_entered = request.POST.get("location")
        specialty_entered = request.POST.get("specialty")

        if location_entered is None or specialty_entered is None:
            # print("fff")
            return redirect("doctor:detail")

        doc_obj = self.model.objects.filter(specialty__specialty_name=specialty_entered, clinic__clinic_location__county=location_entered).distinct()
        print("-----------------------")
        print(doc_obj)
        print("-----------------------")

        context = {
            "doctors": doc_obj,
            "all_locations":all_locations,
            "all_specialities":all_specialities,
            "location_entered":location_entered,
            "specialty_entered":specialty_entered

        }
        return render(request, "doctor/filtered_doctors.html", context)


# function for listing all the locations
class index(View):
    model=get_user_model()

    def get(self, request, *args, **kwargs):

        # print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        # print(get_random_secret_key())
        all_locations = locationn.objects.all()
        all_specialtys = specialty.objects.all()
        print(all_specialtys)
        # corsl_imgs = corousels.objects.all()
        # print(corsl_imgs)

        context = {
            "all_locations" : all_locations,
            "all_specialtys" : all_specialtys,
            # "corsl_imgs" : corsl_imgs
        }

        return render(request, 'doctor/index.html', context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        location_entered = request.POST.get("location")
        specialty_entered = request.POST.get("specialty")
        if specialty_entered is not None and location_entered is None:
            doc_obj = self.model.objects.filter(specialty__specialty_name=specialty_entered).distinct()
        if specialty_entered is None and location_entered is not None:
            doc_obj = self.model.objects.filter(clinic__clinic_location__county=location_entered).distinct()
        if specialty_entered is None and location_entered is None:
            return redirect("doctor:index")
        if specialty_entered is not None and location_entered is not None:
            doc_obj = self.model.objects.filter(specialty__specialty_name=specialty_entered,
                                                clinic__clinic_location__county=location_entered).distinct()

        # print(lct)
        # print(spt)
        # if specialty_entered is None or location_entered is None:
        #     print("fff")
        #     return redirect("doctor:index")
        #
        # doc_obj = self.model.objects.filter(specialty__specialty_name = specialty_entered, clinic__clinic_location__county = location_entered).distinct()
        # print("wowowowowowowoowowwowowowo")
        # print(doc_obj)


        #
        all_locations = locationn.objects.all()
        all_specialtys = specialty.objects.all()

        context = {
            "doctors": doc_obj,
            "location_entered" : location_entered,
            "specialty_entered" : specialty_entered,
            "all_locations": all_locations,
            "all_specialtys": all_specialtys
        }
        return render(request, "doctor/filtered_doctors.html", context)








