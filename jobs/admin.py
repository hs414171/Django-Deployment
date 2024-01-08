from django.contrib import admin
from jobs.models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title','company','city','state','salary_per_month')
    search_fields = ('title','company','city','state')
admin.site.register(Job,JobAdmin)