from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    
    list_filter = ['blood_group', 'gender', 'status']


admin.site.register(UserProfile, UserAdmin)    