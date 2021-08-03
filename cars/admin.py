from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style = "border-radius: 50px;"/>'.format(object.car_photo.url))
    thumbnail.short_description = 'Photo'
    list_display = ('thumbnail','car_title','model','year','city','is_featured')
    list_display_links = ('thumbnail','car_title',)
    list_editable = ('is_featured',)
    search_fields = ('car_title','year')
    list_filter = ('city','body_style')


admin.site.register(Car,CarAdmin)

