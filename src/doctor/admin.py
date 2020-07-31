from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Profile, ClinicPhotos, Thumbnail, Clinic, MyPatients, locationn, specialty, profile_pic_thumbnails, New_Specialty

admin.site.register(Profile)

admin.site.register(Clinic)

# class ThumbnailInline(admin.TabularInline):
#     model = Thumbnail
#     extra = 0
#
# class ClinicPhotoAdmin(admin.ModelAdmin):
#     inlines = [
#         ThumbnailInline,
#     ]
#     class Meta:
#         model = ClinicPhotos
#
# admin.site.register(ClinicPhotos, ClinicPhotoAdmin)

admin.site.register(ClinicPhotos)
admin.site.register(Thumbnail)
admin.site.register(MyPatients)
admin.site.register(locationn)
admin.site.register(specialty)
# admin.site.register(corousels)
# admin.site.register(corouselThumbnails)
admin.site.register(profile_pic_thumbnails)
admin.site.register(New_Specialty)









#Patient Admin Classes

# class Patient(User):
#     class Meta:
#         proxy = True
#         verbose_name = 'patient'
#         verbose_name_plural = 'patients'
#
# class PatientInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Patient Profile'
#     fk_name = 'user'
#     fields = [
#         "patient_picture","birth_date","mobile_no","role"
#     ]
#
# class PatientAdmin(UserAdmin):
#     inlines = (PatientInline, )
#     #list_display = ('email', 'first_name', 'last_name', 'get_company', 'is_active')
#     list_display = ('email', 'first_name', 'last_name', 'is_active', 'id')
#
#     def get_queryset(self, request):
#         qs = super(PatientAdmin, self).get_queryset(request)
#         #return qs.select_related("profile").defer("profile__board_certifications") # you need to filter it properly! depends on how you implemented
#
#         return qs.filter(profile__role='P')  # you need to filter it properly! depends on how you implemented

#Doctor Admin Classes

# class Doctor(User):
#     class Meta:
#         proxy = True
#         verbose_name = 'doctor'
#         verbose_name_plural = 'doctors'

# class DoctorInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Doctor Profile'
#
#     fields = [
#         "second_name",
#         "education",
#         "specialty",
#         "professional_membership",
#         "board_certifications",
#         "professional_awards",
#         "professional_biography",
#         "dr_profile_pic",
#         "height_field",
#         "width_field",
#         "mobile_no",
#         "role"
#     ]
#
#     fk_name = 'user'

# class DoctorAdmin(UserAdmin):
#     inlines = (DoctorInline, )
#     list_display = ('email', 'first_name', 'last_name', 'is_active','id')  # the fields you want from the doctor
#
#     def get_queryset(self, request):
#         qs = super(DoctorAdmin, self).get_queryset(request)
#         return qs.filter(profile__role='D')  # you need to filter it properly! depends on how you implemented
#

#Register Admin Classes

# admin.site.unregister(User)
# admin.site.register(Doctor, DoctorAdmin)
# admin.site.register(Patient, PatientAdmin)
# admin.site.register(Treatment)










































































# Register your models here.
#from .models import Doctor, Patient,doctor_location_images #hero_section

#class ProfileInline(admin.StackedInline):
    #model = Doctor
    #can_delete = False
    #verbose_name_plural = 'Doctor'
    #fk_name = 'user'

#class CustomUserAdmin(UserAdmin):
        #inlines = (ProfileInline, )

        #def get_inline_instances(self, request, obj=None):
            #if not obj:
                #return list()
            #return super(CustomUserAdmin, self).get_inline_instances(request, obj)


#admin.site.unregister(User)
#admin.site.register(User, CustomUserAdmin)


