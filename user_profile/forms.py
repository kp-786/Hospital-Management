from django import forms
from .models import *

class ProfileUpdateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.RadioSelect)
    
    class Meta:
        model = UserProfile
        fields = ('name','phone','email','gender','age','address','blood_group')

class DoctorProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.RadioSelect)
    
    class Meta:
        model = UserProfile
        fields = ('name','phone','email','gender','age','address','department','salary','status')
        