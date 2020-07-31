from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.urls import reverse
from django.db.models import Avg

from rating.models import Rating

class New_Specialty(models.Model):
    doc = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                            null=True, blank=True)
    new_specialty = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.new_specialty)


class specialty(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    specialty_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.specialty_name)


class locationn(models.Model):
    county = models.CharField(max_length=50, null=True, blank=True)
    county_image = models.ImageField(upload_to="county_images", null=True, blank=True, height_field = "height_field", width_field = "width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return str(self.county)

class Clinic(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    clinic_name = models.CharField(max_length=50)
    owner = models.CharField(max_length=150, blank=True, null=True)
    clinic_location = models.ForeignKey(locationn, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.clinic_name)

    def get_absolute_url(self):
        return reverse("doctor:edit_clinic_own", kwargs={"pk": self.pk})

    # def clinic_photos_instance_method(self):
    #     # return reverse("doctor:clinic_photos", kwargs={"id": self.user.id})
    #     return reverse("doctor:clinic_photos")


# def dr_profile_images(instance, doctor_pictures):
#     return "%s/%s" %(instance.user.last_name, doctor_pictures)

class Profile(models.Model):

    #this is the field being used as a one to one link
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    #generic data
    mobile_no = models.CharField(max_length=15, null=True, blank=False)
    photo = models.ImageField(upload_to="dr_profile_images/", null=True, blank=True, height_field="height",
                              width_field="width")  # upload_to="dr_profile_pics"
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)

    #doctor profile data
    # doctor = models.NullBooleanField(default=None)
    doctor = models.BooleanField(default=False)
    second_name = models.CharField(max_length=30, blank=True)
    education = models.CharField(max_length=500, null=True, blank=True)

    professional_membership = models.CharField(max_length=500, null=True, blank=True)
    board_certifications = models.CharField(max_length=500, null=True, blank=True)
    professional_awards = models.CharField(max_length=500, null=True, blank=True)
    professional_biography = models.TextField(max_length=1500, null=True, blank=True)

    #is_doctor = models.BooleanField(default=False)
    doctor_activate = models.BooleanField(default=False)
    patient =  models.BooleanField(default=False)

    #patient profile data
    # photo = models.ImageField(upload_to="patient_pictures/", null=True, blank=True, height_field="height",
    #                           width_field="width")
    # height = models.IntegerField(default=0)
    # width = models.IntegerField(default=0)


    # photo = models.ImageField(upload_to="patient_pictures/",null=True, blank=True, height_field = "patient_height_field", width_field = "patient_width_field")
    # patient_height_field = models.IntegerField(default=0)
    # patient_width_field = models.IntegerField(default=0)


    birth_date = models.DateField(null=True, blank=True)
    # is_patient = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username # + ' ' + self.surname

    def get_absolute_url(self):
        return reverse("doctor:detail", kwargs={"pk": self.user.id})

    def doc_obj_average_rating(self):
        return self.user.doc_rated.aggregate(Avg("rating_value"))

    #instance method to get doctor's location
    def doc_location(self):
        clinic = self.user.clinic_set.all()
        for instance in clinic:
            print(instance.clinic_location.county)
            doc_location = instance.clinic_location.county
        return doc_location

    #instance method to get doctor's specialty
    def doc_specialty(self):
        return self.user.specialty_set.all()

    def profile_pics_sd(self):
        sd_pics = self.profile_pic_thumbnails_set.filter(type="sd")
        for instance in sd_pics:
            return instance.photo.url

    def profile_pics_micro(self):
        micro_pics = self.profile_pic_thumbnails_set.filter(type="micro")
        for instance in micro_pics:
            return instance.photo.url


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
    instance.profile.save()


post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL, dispatch_uid="user_model_signal")

class profile_pic_thumbnails(models.Model):
    dr_profile_thumb_choices = (
        ("sd", "standard_images"),
        ("micro", "images_for_phones"),
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=20, choices=dr_profile_thumb_choices, default="sd")
    height = models.CharField(max_length=30, blank=True, null=True)
    width = models.CharField(max_length=30, blank=True, null=True)
    photo = models.ImageField(upload_to="dr_profile_pic/", null=True, blank=True,
                              height_field="height",
                              width_field="width")

    def __str__(self):
        return str(self.photo.path)


def dr_profile_thumbnails_post_save_receiver(instance, sender, created, *args, **kwargs):
    if instance.photo:
        sd, sd_created = profile_pic_thumbnails.objects.get_or_create(profile=instance, type="sd")
        micro, micro_created = profile_pic_thumbnails.objects.get_or_create(profile=instance, type="micro")

        sd_max = (500,500)
        micro_max = (300, 300)
        media_path = instance.photo.path


        if sd_created:
            create_thumb(media_path, sd, sd_max[0], sd_max[1])

        if micro_created:
            create_thumb(media_path, micro,  micro_max[0], micro_max[1])


post_save.connect(dr_profile_thumbnails_post_save_receiver, sender=Profile)



class ClinicPhotos(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE,
                               null=True, blank=True)
    photo_name = models.CharField(max_length=30)
    height = models.CharField(max_length=30, blank=True, null=True)
    width = models.CharField(max_length=30, blank=True, null=True)
    photo = models.ImageField(upload_to="clinic_photos/",null=True, blank=True, height_field = "height",
                                       width_field = "width")

    def __str__(self):
        return "%s - " "%s" %(self.clinic, self.photo_name)

    def clinic_photos_thumbnails_sd(self):
        thumbnails = self.thumbnail_set.filter(type="sd")
        for instance in thumbnails:
            return instance.photo.url

    def clinic_photos_thumbnails_micro(self):
        thumbnails = self.thumbnail_set.filter(type="micro")
        for instance in thumbnails:
            return instance.photo.url




class Thumbnail(models.Model):
    thumb_choices = (
        ("sd", "standard_images"),
        ("micro", "images_for_phones"),
    )

    clinic_photo = models.ForeignKey(ClinicPhotos, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=thumb_choices, default="sd")
    building_height = models.CharField(max_length=30, blank=True, null=True)
    building_width = models.CharField(max_length=30, blank=True, null=True)
    photo = models.ImageField(upload_to="thumbnail_clinic_photos/",null=True, blank=True, height_field = "building_height",
                                       width_field = "building_width")

    def __str__(self):
        return str(self.photo.path)



import os
import shutil
from PIL import Image
import random
from django.core.files import File

def create_thumb(media_path, instance, max_length, max_width):
    filename = os.path.basename(media_path)
    thumb = Image.open(media_path)
    size = (max_length, max_width)
    thumb.thumbnail(size, Image.ANTIALIAS)

    temp_loc = "%s/%s/tmp" % (settings.MEDIA_ROOT, instance.id)

    if not os.path.exists(temp_loc):
        os.makedirs(temp_loc)

    temp_file_path = os.path.join(temp_loc, filename)
    if os.path.exists(temp_file_path):
        temp_path = os.path.join(temp_loc, "%s" % (random.random()))
        os.makedirs(temp_path)
        temp_file_path = os.path.join(temp_path, filename)

    temp_image = open(temp_file_path, "w")
    thumb.save(temp_image)
    thumb_data = open(temp_file_path, "rb")

    thumb_file = File(thumb_data)
    instance.photo.save(filename, thumb_file)
    # shutil.rmtree(filename, ignore_errors=True)
    return True


def clinicPhotos_post_save_receiver(instance, sender, created, *args, **kwargs):
    if instance.photo:
        sd, sd_created = Thumbnail.objects.get_or_create(clinic_photo=instance, type="sd")
        micro, micro_created = Thumbnail.objects.get_or_create(clinic_photo=instance, type="micro")

        sd_max = (500,500)
        micro_max = (300, 300)
        media_path = instance.photo.path


        if sd_created:
            create_thumb(media_path, sd, sd_max[0], sd_max[1])

        if micro_created:
            create_thumb(media_path, micro,  micro_max[0], micro_max[1])



post_save.connect(clinicPhotos_post_save_receiver, sender=ClinicPhotos)



class MyPatients(models.Model):
    dr = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    patients = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="doc_patients", blank=True)

    def __str__(self):
        return '-'.join([str(doc) for doc in self.dr.all()])

















































#
# class corousels(models.Model):
#     photo_name = models.CharField(max_length=50)
#     height = models.CharField(max_length=50, blank=True, null=True)
#     width = models.CharField(max_length=50, blank=True, null=True)
#     photo = models.ImageField(upload_to="corousels_photos/", null=True, blank=True, height_field="height",
#                               width_field="width")
#
#     def __str__(self):
#         return "%s" %(self.photo_name)
#
#
# class corouselThumbnails(models.Model):
#     corousels_thumbnail_choices = {
#         ("sd", "standard_corousel_imgs"),
#         ("micro", "micro_corousel_imgs"),
#
#     }
#     corousels = models.ForeignKey(corousels, null=True, blank=True)
#     type = models.CharField(max_length=20, choices=corousels_thumbnail_choices, default="sd")
#     height = models.CharField(max_length=50, blank=True, null=True)
#     width = models.CharField(max_length=50, blank=True, null=True)
#     photo = models.ImageField(upload_to="thumbnail_corousel_photos/", null=True, blank=True,
#                               height_field="height",
#                                            width_field = "width")
#
#
# def corouselPhotos_post_save_receiver(instance, sender, created, *args, **kwargs):
#     if instance.photo:
#         sd, sd_created = corouselThumbnails.objects.get_or_create(corousels=instance, type="sd")
#         micro, micro_created = corouselThumbnails.objects.get_or_create(corousels=instance, type="micro")
#
#         sd_max = (1140,430)
#         micro_max = (200, 200)
#         media_path = instance.photo.path
#
#
#         if sd_created:
#             create_thumb(media_path, sd, sd_max[0], sd_max[1])
#
#         if micro_created:
#             create_thumb(media_path, micro,  micro_max[0], micro_max[1])
#
# post_save.connect(corouselPhotos_post_save_receiver, sender=corousels)