from django.contrib import admin

from .models import Company, Applicant, Job, Profile



admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(Profile)