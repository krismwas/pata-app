from django import forms
# from django.contrib.auth.models import User
from .models import Profile, locationn, specialty, ClinicPhotos, Clinic
from django.contrib.auth import get_user_model

class FormClinicUpdate(forms.ModelForm):

    user = forms.ModelMultipleChoiceField(label="doctors who work at the clinic. unselecting removes one from the clinic", queryset=get_user_model().objects.all())
    clinic_name = forms.CharField(max_length=50)
    class Meta:
        model = Clinic
        fields = [
            'user', 'clinic_name', 'clinic_location', 'owner'
        ]

    #this is show only users for a particular clinic only
    def __init__(self, clinic_id, *args, **kwargs):
        super(FormClinicUpdate, self).__init__(*args, **kwargs)
        clinicobj = Clinic.objects.get(id=clinic_id)
        self.fields['user'].queryset = clinicobj.user.all()



class formAddclinic(forms.ModelForm):
    clinic_name = forms.CharField(max_length=50)
    class Meta:
        model = Clinic
        fields = [
            'clinic_name','clinic_location'
        ]

class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'photo'
        ]


class ClinicPhotoForm(forms.ModelForm):
    class Meta:
        model = ClinicPhotos
        fields = [
            'photo'
        ]


class FormDoctorUser(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
    )
    last_name = forms.CharField(required=True)
    class Meta:
        model = get_user_model()
        fields = [
            'first_name', 'last_name'
        ]

class FormDoctorProfile(forms.ModelForm):
    education = forms.CharField(required=True)
    specialty = forms.ModelChoiceField(queryset=specialty.objects.all(), empty_label="Please enter your specialty")
    board_certifications = forms.CharField(required=True)
    class Meta:
        model = Profile
        fields = [
            'education',"specialty","board_certifications"
        ]

class FormPatientProfile(forms.ModelForm):
    mobile_no = forms.IntegerField()

    class Meta:
        model = Profile
        fields = [
            'mobile_no'
        ]


class FormPatientUser(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Please enter your first name"
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Please enter your last name"
        }
    ))

    class Meta:
        model = get_user_model()
        fields = [
            'last_name','first_name'
        ]


class form_doctors_contact(forms.Form):
    first_name = forms.CharField(label="first name", widget=forms.TextInput(
        attrs={
            "placeholder": "Please enter your first name"
        }
    ))
    mobile_no = forms.CharField(label="Mobile number",widget=forms.TextInput(
        attrs={
            "placeholder": "Please enter your mobile number, we can use to contact you "
        }
    ))

    clinic_name = forms.CharField(label="Clinic name",widget=forms.TextInput(
        attrs={
            "placeholder": "please your clinic name "
        }
    ))

    location = forms.ModelChoiceField(queryset=locationn.objects.all(), empty_label="select location")


