from django.contrib import admin

# Register your models here.
from . models import User

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    

admin.site.register(User, UserAdmin)
