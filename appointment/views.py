from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from user_profile.models import UserProfile
from .models import *
from .forms import *

# Create your views here.

class AppointmentsForPatientView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'accounts:login'
    
    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)

class AppointmentsForDoctorView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'accounts:login'
    
    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user)

class MedicalHistoryView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'accounts:login'
    
    def get_queryset(self):
        return Prescription.objects.filter(patient=self.request.user)

class PrescriptionListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'accounts:login'
    
    def get_queryset(self):
        return Prescription.objects.filter(doctor=self.request.user)

@login_required(login_url='/login/')
def PrescriptionCreateView(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user
            prescription.save()
            return redirect('appointment:doctor_prescriptions')  
    else:
        form = PrescriptionForm()
    return render(request, 'appointment/prescription_create.html', {'form': form})     

@login_required(login_url='/login/')
def AppointmentCreateView(request):
    form_class = AppointmentForm
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return redirect('appointment:rec_dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/appointment_create.html', {'form': form})

@login_required(login_url = '/login/')
def recdashboard(request):
    if request.method == 'GET' and request.user.user_type == 'R':
        context = {
            'totalApp': len(Appointment.objects.all()),
            'compApp': len(Appointment.objects.filter(status='Completed')),
            'pendApp': len(Appointment.objects.filter(status='Pending')),
            'app_list': Appointment.objects.all(),
            'pat_list': UserProfile.objects.filter(user__user_type='P')[:5]
        }
        return render(request, 'appointment/rec_dashboard.html', context=context)

@login_required(login_url='/login/')
def hrdashboard(request):
    if request.method == "GET" and request.user.user_type == 'HR':
        context = {
            'totalPat': len(User.objects.filter(user_type='P')),
            'totalDoc': len(User.objects.filter(user_type='D')),
            'onDutyDoc': len(UserProfile.objects.filter(status='Active').filter(user__user_type='D')),
            'doc_list': UserProfile.objects.filter(user__user_type='D')
        }
        return render(request, 'appointment/hr_dashboard.html', context=context)
