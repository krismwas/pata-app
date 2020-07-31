from django.conf.urls import url
from . import views
#from django.contrib import admin
from django.views.generic import TemplateView
from rating.views import DoctorRatingAjaxView, DoctorAjaxReviewMessage, HelpfulCountAjax, ReportAbuseAjax, NoAjax
from .views import (ProfileDetailView, index, add_new_clinic,DoctorSelecteClinicAjax, FirstName, SecondName, DocEmail,
                    ClinicPhotoss, DoctorAppointment, PatientHome,doctor_clinics_name_update, dr_upload_profile_pic,
                    PatientVerification,clinicPhotosAjax,doctors_specialty_selected, profile_pic_delete,
                    DoctorPatients,doctors_specitys, DocDob, DoctorEditProfile, DocUserName,
                    PatientUnverification, NewSpecialty, RegisterPractice, ClinicUpdate, LastName,
                    uploadClinicPhotosAjax,DelPicAjax,professionalBiography, DocMobileNo,
                    PatientUsername, PatientEmail, PatientFirstName, PatientLastName, PatientDob, PatientMobile,
                    ProfessionalMembership, ProfessionalEducation, ProfessionalBoardCertifications, ProfessionalAwards )
# from book_appointment.views import ajaxDrAppointment

app_name = 'doctor'

urlpatterns = [
    url(r'^patient_mobile_number/$', PatientMobile.as_view(), name='patient_mobile_no_ajax'),
    url(r'^patient_dob/$', PatientDob.as_view(), name='patient_dob_ajax'),
    url(r'^patient_last_name/$', PatientLastName.as_view(), name='patient_lname_ajax'),
    url(r'^patient_first_name/$', PatientFirstName.as_view(), name='patient_fname_ajax'),
    url(r'^patient_email/$', PatientEmail.as_view(), name='patient_email_ajax'),
    url(r'^patient_username/$', PatientUsername.as_view(), name='patient_username_ajax'),


    url(r'^professional_awards/$', ProfessionalAwards.as_view(), name='professional_award_ajax'),
    url(r'^professional_board_certifications/$', ProfessionalBoardCertifications.as_view(), name='bcertifications_ajax'),
    url(r'^professional_membership/$', ProfessionalMembership.as_view(), name='professional_membership_ajax'),
    url(r'^professional_education/$', ProfessionalEducation.as_view(), name='professional_education_ajax'),


    url(r'^doctor_mobile_no/$', DocMobileNo.as_view(), name='doc_mobile_ajax'),
    url(r'^doctor_username/$', DocUserName.as_view(), name='doc_username_ajax'),
    url(r'^doctor_dob/$', DocDob.as_view(), name='dob_ajax'),
    url(r'^doctor_email/$', DocEmail.as_view(), name='email_ajax'),
    url(r'^doctor_second_name/$', SecondName.as_view(), name='second_name_ajax'),
    url(r'^doctor_last_name/$', LastName.as_view(), name='last_name_ajax'),
    url(r'^doctor_first_name/$', FirstName.as_view(), name='first_name_ajax'),


    # url(r'^clinic_doctors/$', ClinicDoctors.as_view(), name='clinic_doctors_ajax'),
    url(r'^register_practice/$', RegisterPractice.as_view(), name='register_practice'),
    url(r'^new_specialty/$', NewSpecialty.as_view(), name='new_specitys_ajax'),
    url(r'^no/$', NoAjax.as_view(), name='no_ajax'),
    url(r'^report_abuse/$', ReportAbuseAjax.as_view(), name='report_abuse_ajax'),
    url(r'^helpful_review/$', HelpfulCountAjax.as_view(), name='helpful_count_ajax'),
    url(r'^patient_unverification/$', PatientUnverification.as_view(), name="patient_unverification_ajax"),
    url(r'^delete_profile_pic/$', profile_pic_delete.as_view(), name="profile_pic_delete_ajax"),
    url(r'^doctor_upload_pic/$', dr_upload_profile_pic.as_view(), name="doctor_upload_pic"),
    url(r'^your_specialty/$', doctors_specitys.as_view(), name="doctors_specitys_ajax"),
    url(r'^selected_specialty/$', doctors_specialty_selected.as_view(), name="doctor_specialty_selected_ajax"),
    url(r'^clinic/(?P<pk>\d+)/edit/$', ClinicUpdate.as_view(), name="edit_clinic_own_new"),
    # url(r'^edit_clinic/(?P<pk>\d+)/$', edit_clinic_you_own.as_view(), name="edit_clinic_own"),
    url(r'^doctor_selected_clinic/$', DoctorSelecteClinicAjax.as_view(), name="doc_selected_clinic_ajax"),
    url(r'^clinic_successfully_added/$',TemplateView.as_view(template_name="doctor/clinic_added_successfully.html"), name="clinic_added_success"),
    url(r'^add_clinic/$', add_new_clinic.as_view(), name="add_clinic"),
    # url(r'^clinic_location_update/$', doctor_clinics_location_update.as_view(), name="clinic_location_ajax"),
    url(r'^clinic_update/$', doctor_clinics_name_update.as_view(), name="clinic_name_ajax"),
    # url(r'^specialty_update/$', doctor_specialty_update.as_view(), name="specialty_ajax"),
    # url(r'^professional_ground/$', professionalBackground.as_view(), name="pro_bg"),
    url(r'^uploadclinicphotos/(?P<id>\d+)/$', uploadClinicPhotosAjax.as_view(), name="uploadclinicpicsajax"),
    url(r'^deleteclinicphoto/$', DelPicAjax.as_view(), name="delclinicpic"),
    url(r'^professional_biography/$', professionalBiography.as_view(), name="professinal_bio"),

    # url(r'^index/$', index.as_view(), name='index'),

    url(r'^$', index.as_view(), name='index'),
    # url(r'^accounts/logout/index/$', index.as_view(), name='index'),
    # url(r'^test/$', views.testcss, name="tesst"),
    # url(r'^all_doctors/$', all_doctors.as_view(), name='all_doctors'),
    # url(r'^(?P<pk>\d+)/(?P<specc>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/$', ProfileDetailView.as_view(), name='detail'),
    # url(r'^doctor_contact/$', doctors_contact.as_view(), name="doctor_contact"),
    url(r'^doctor_contact/thanks/$', TemplateView.as_view(template_name="thanks.html"), name='thanks'),
    url(r'^ajax/rating/$', DoctorRatingAjaxView.as_view(), name='ajax_rating'),
    url(r'^ajax/review/$', DoctorAjaxReviewMessage.as_view(), name='ajax_review_msg'),
    # url(r'^book_appointment/$', ajaxDrAppointment.as_view(), name="dr_booking"),
    url(r'^clinic_photos/(?P<id>\d+)/$', ClinicPhotoss.as_view(), name="clinic_photos"),
    # url(r'^clinic_photos/$', ClinicPhotoss.as_view(), name="clinic_photos"),
    # url(r'^myregistration/$', PatientRegistration.as_view(), name="patient_registration_user_model"),
    url(r'^patient_verification/$', PatientVerification.as_view(), name="patient_verification"),
    url(r'^patient/$', DoctorPatients.as_view(), name="doctor_patients"),
    # url(r'^profile/$', DoctorCreateView.as_view(), name="doctor_create_profile"),
    url(r'^profileEdit/$', DoctorEditProfile.as_view(), name="doctor_profile"),
    url(r'^clinic_photos/$', clinicPhotosAjax.as_view(), name="clinicPhotosAjax"),

    # url(r'^profile_update/$', profileUpdateAjax.as_view(), name="profile_update_ajax"),
    # url(r'^patient_profile_update/$', PatientProfileUpdate.as_view(), name="patient_profile_update_ajax"),

    url(r'^(?P<patient>[\w-]+)/$', PatientHome.as_view(), name="patient_home"),

    url(r'^my/(?P<user>[\w-]+)/$', DoctorAppointment.as_view(), name="doctor_appointment"),



]


