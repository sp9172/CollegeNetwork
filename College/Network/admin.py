from django.contrib import admin
from . models import PersonModel,UserProfile,bloodgroup

# Register your models here.

admin.site.register(PersonModel)
admin.site.register(UserProfile)
admin.site.register(bloodgroup)