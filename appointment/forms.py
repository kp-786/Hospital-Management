from django import forms
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class DateInput(forms.DateInput):
    input_type = 'date'

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('patient', 'symptoms', 'prescription')
    
    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['patient'].queryset = User.objects.filter(user_type='P')


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['patient'].queryset = User.objects.filter(user_type='P')
            self.fields['doctor'].queryset = User.objects.filter(user_type='D')
            self.fields['date'].label = 'Date (DD-MM-YYYY)'
            self.fields['time'].label = 'Time 24 hr (HH:MM)'
    