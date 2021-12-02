from django.contrib import admin
from .models import Profile, Work, Technical, Software


# Register your models here.
admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Technical)
admin.site.register(Software)