from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(PersonModel)
admin.site.register(UserProfile)
# admin.site.register(bloodgroup)
admin.site.register(ImageUploading)

admin.site.register(PostUploading)


