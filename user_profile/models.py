from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

BLOOD_GROUPS = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    name = models.CharField(max_length=40)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(max_length=17, validators=[phone_regex], blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True)
    blood_group = models.CharField(choices=BLOOD_GROUPS, max_length=3, blank=True)
    med_rps = models.FileField(upload_to='profile/med_rps', blank=True)
    case_paper = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    attendance = models.IntegerField(blank=True, null=True)
    status = models.CharField(choices=[('Active', 'Active'),('Inactive','Inactive')],null=True, blank=True, max_length=8)
    
    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return "Profile for {}".format(self.user)