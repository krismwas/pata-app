from django.views.generic import View
from .models import Rating, DoctorReviewOpinionCount, ReportedAbuse
from doctor.models import Profile
from django.http import JsonResponse, Http404
from django.contrib.auth import get_user_model
# Create your views here.


class NoAjax(View):
    def post(self, request, *args, **kwargs):
        if not self.request.is_ajax():
            return JsonResponse({}, status=400)
        if not self.request.user.is_authenticated:
            return JsonResponse({}, status=401)

        review_id = request.POST.get("review_id")
        if review_id is None:
            return JsonResponse({}, status=400)
        review_id = review_id.strip()

        review = Rating.objects.filter(id=review_id).exists()

        if review:
            review_obj = Rating.objects.get(id=review_id)
            all_review_obj_opinion_count = review_obj.doctorreviewopinioncount_set.all().exists()
            # print(all_review_obj_opinion_count)
            if not all_review_obj_opinion_count:
                # print("zzzzzzzzzzzzzzz")
                data = {"success":"doesnotexists"}
                return JsonResponse(data)
            if all_review_obj_opinion_count:
                # print("liiiiiiiiiiiiiiiiiiz")
                doctor_review_opion_count_obj = DoctorReviewOpinionCount.objects.filter(
                    patient=self.request.user).exists()
                if doctor_review_opion_count_obj:
                    doctor_review_opion_count_obj = DoctorReviewOpinionCount.objects.filter(
                        patient=self.request.user).delete()
                    data = {"success": True}
                    return JsonResponse(data)

        data={}
        return JsonResponse(data)


class ReportAbuseAjax(View):
    def post(self, request, *args, **kwargs):
        if not self.request.is_ajax():
            return JsonResponse({}, status=400)
        if not self.request.user.is_authenticated:
            return JsonResponse({}, status=401)
        # print("ththththhthth")
        review_id = request.POST.get("review_id")
        review = Rating.objects.filter(id=review_id).exists()
        if review:
            rating_obj = Rating.objects.get(id=review_id)
            reported_abuse_obj = ReportedAbuse.objects.filter(reporter=self.request.user, review_obj=rating_obj).exists()
            if reported_abuse_obj:
                data={
                    "success":"already_submitted"
                }
                return JsonResponse(data)

            # rating_obj = Rating.objects.get(id=review_id)
            # print("---------------")
            report_abuse = ReportedAbuse.objects.create(reporter=self.request.user, review_obj= rating_obj)
            report_abuse.save()
            data={
                "success":True
            }
            return JsonResponse(data)

        data={}
        return JsonResponse(data)


class HelpfulCountAjax(View):
    model=get_user_model()

    def post(self, request, *args, **kwargs):
        if not self.request.is_ajax():
            return JsonResponse({}, status=400)
        if not self.request.user.is_authenticated:
            return JsonResponse({}, status=401)

        review_id = request.POST.get("review_id")

        review = Rating.objects.filter(id=review_id).exists()

        if review:
            review_obj = Rating.objects.get(id=review_id)
            all_review_obj_opinion_count = review_obj.doctorreviewopinioncount_set.all().exists()
            # print(all_review_obj_opinion_count)
            if not all_review_obj_opinion_count:
                print("oooooooooooooo")
                doctor_review_opion_count_obj = DoctorReviewOpinionCount.objects.\
                    create(rating=review_obj, helpful_count=1, patient=self.request.user)
                doctor_review_opion_count_obj.save()
                data={"success":True}
                return JsonResponse(data)
            if all_review_obj_opinion_count:
                print("liiiiiiiiiiiiiiiiiiz")
                doctor_review_opion_count_obj = DoctorReviewOpinionCount.objects.filter(patient=self.request.user).exists()
                if doctor_review_opion_count_obj:
                    data = {"success":"already"}
                    return JsonResponse(data)
                elif not doctor_review_opion_count_obj:
                    doctor_review_opion_obj = DoctorReviewOpinionCount.objects. \
                        create(rating=review_obj, helpful_count=1, patient=self.request.user)
                    doctor_review_opion_obj.save()
                    data = {"success":True}
                    return JsonResponse(data)

        data={}
        return JsonResponse(data)


class DoctorRatingAjaxView(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not self.request.is_ajax():
            return JsonResponse({}, status=400)
        if not self.request.user.is_authenticated:
            return JsonResponse({}, status=401)

        user = request.user
        doctor_id = request.POST.get("doctor_id")
        if doctor_id is None:
            return JsonResponse({}, status=400)
        if self.request.user.id == int(doctor_id):
            return JsonResponse({}, status=400)

        rating_vaue = request.POST.get("rating_vaue")
        if rating_vaue is None:
            return JsonResponse({}, status=400)
        rating_vaue = rating_vaue.strip()
        try:
            doc_obj = self.model.objects.get(id=doctor_id)
        except:
            raise Http404

        try:
            rating_obj = Rating.objects.get(user=user, dr_rated=doc_obj)
        except:
            rating_obj = Rating.objects.create(user=user, dr_rated=doc_obj)
        rating_obj.rating_value = int(rating_vaue)
        rating_obj.save()

        data = {
            "success": True
        }
        return JsonResponse(data)


class DoctorAjaxReviewMessage(View):
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({}, status=400)
        if not request.user.is_authenticated:
            return JsonResponse({}, status=401)
        success = False
        review_msg = request.POST.get("msgrvw")
        if review_msg is None:
            return JsonResponse({}, status=400)
        review_msg = review_msg.strip()
        # if not rvmsgdic:
        #     return JsonResponse({}, status=404)
        # print(request.POST.get("msgrvw"))
        user = self.request.user
        doctor_id = request.POST.get("doctor_id")
        # review_msg = request.POST.get("msgrvw")

        try:
            doc_obj = self.model.objects.get(id=doctor_id)
            # print(doc_obj)
        except:
            raise Http404
        try:
            rating_obj = Rating.objects.get(user=user, dr_rated=doc_obj)
        except:
            rating_obj = Rating.objects.create(user=user, dr_rated=doc_obj)
        if self.request.user == doc_obj:
            docSelf=True
            data={"docSelf":docSelf}
            return JsonResponse(data)
        rating_obj.review = review_msg
        rating_obj.save()
        success = True
        data = {
            "success": success
        }
        return JsonResponse(data)
