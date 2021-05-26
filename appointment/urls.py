from django.urls import path
from . import views

app_name = 'appointment'

urlpatterns = [
    path("appointments/p/", views.AppointmentsForPatientView.as_view(), name="patient_appointments"),
    path("appointments/d/", views.AppointmentsForDoctorView.as_view(), name="doctor_appointments"),
    path("medHistory/", views.MedicalHistoryView.as_view(), name="med_history"),
    path("prescriptions/", views.PrescriptionListView.as_view(), name="doctor_prescriptions"),
    path("prescription/create", views.PrescriptionCreateView, name="doc_prescription_create"),
    path("appointment/create", views.AppointmentCreateView, name="appointment_create"),
    path("recdashboard/", views.recdashboard, name="rec_dashboard"),
    path("hrdashboard/", views.hrdashboard, name="hr_dashboard"),
]