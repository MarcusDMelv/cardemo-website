from django.contrib import admin
# import models
from .models import Team

# edit display for each dataset
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'job_title','created_date','updated_date')
    # make dataset clickable
    list_display_links = ('id','first_name')
    search_fields = ('first_name','last_name','job_title')
    list_filter = ('job_title',)


# Register your models here.
# TODO add model 'Team'
admin.site.register(Team, TeamAdmin)
