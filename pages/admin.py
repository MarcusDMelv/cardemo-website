from django.contrib import admin
# import models
from .models import Team
from django.utils.html import format_html

# edit display for each dataset
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style = "border-radius: 50px;"/>'.format(object.photo.url))
    thumbnail.short_description = 'Photo'
    list_display = ('id','thumbnail', 'first_name', 'last_name', 'job_title','created_date','updated_date')
    # make dataset clickable
    list_display_links = ('id','first_name')
    search_fields = ('first_name','last_name','job_title')
    list_filter = ('job_title',)


# Register your models here.
# TODO add model 'Team'
admin.site.register(Team, TeamAdmin)
