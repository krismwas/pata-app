from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.
class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dr_rated = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE, related_name="doc_rated")
    rating_value = models.IntegerField(default=100)
    verified = models.BooleanField(default=False)
    review = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    # helpful_count = models.IntegerField(default=0)

    def __str__(self):
        return "%s" %(self.user)

    def instance_review_count(self):
        return self.doctorreviewopinioncount_set.count()

    #this is all opinions minus the opinion of patient who clicked yes
    # def my_opinion_minus_others(self):
    #     opionion_count = self.doctorreviewopinioncount_set.all().count()
    #     return opionion_count - 1

class DoctorReviewOpinionCount(models.Model):
    rating = models.ForeignKey(Rating, null=True, blank=True,
                               on_delete=models.CASCADE)
    helpful_count = models.IntegerField(default=0)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                blank=True, null=True)

    def __str__(self):
        return "%s" % (self.patient)

class ReportedAbuse(models.Model):
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 null=True, blank=True)
    review_obj = models.ForeignKey(Rating, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        x = ReportedAbuse.objects.filter(review_obj=self.review_obj).count()
        return "%s-%s" %(self.review_obj, x)





