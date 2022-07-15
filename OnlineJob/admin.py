from django.contrib import admin

from .models import Company, Job, Note, Profile, ControlPanel, Applicant



admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Profile)
admin.site.register(Note)
admin.site.register(ControlPanel)
admin.site.register(Applicant)