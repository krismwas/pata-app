from django.contrib import admin

# Register your models here.
from .models import Rating, DoctorReviewOpinionCount, ReportedAbuse

admin.site.register(Rating)

admin.site.register(DoctorReviewOpinionCount)

admin.site.register(ReportedAbuse)