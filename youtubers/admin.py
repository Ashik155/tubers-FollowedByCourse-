from django.contrib import admin
from .models import youtuber
from django.utils.html import format_html
 # Register your models here.


class ytbuersDashBoard(admin.ModelAdmin):
    def profile(self,object):
        return format_html('<img src={} width="35"/>'.format(object.photo.url))

    list_display = ('id', 'profile', 'name','subs_count','is_featured','camera_type')
    search_fields = ('name','category', 'camera_type')
    list_display_links =('id', 'name')
    list_filter = ('city','category')
    list_editable = ('camera_type', 'is_featured')


admin.site.register(youtuber, ytbuersDashBoard)