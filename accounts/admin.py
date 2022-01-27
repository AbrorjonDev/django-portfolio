from django.contrib import admin
from .models import *

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'whois', 'internship', 'image')

class JobApplyingAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_type', 'requirements', 'company_info', 'contacts', 'opportunities')

admin.site.register(Skills)
admin.site.register(News)
admin.site.register(Contacts)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(JobApplying, JobApplyingAdmin)