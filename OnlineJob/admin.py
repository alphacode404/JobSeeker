from django.contrib import admin

from .models import Company, Applicant, Job, Note, Profile



admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(Profile)
admin.site.register(Note)