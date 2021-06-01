from django.contrib import admin
from .models import Slider3, models, team
from django.utils.html import format_html

class dashboardTeam(admin.ModelAdmin):

    def profile(self,object):
        return format_html('<img src={} width="35"/>'.format(object.photo.url))



    list_display = ('id', 'profile', 'first_name', 'role', 'cretaed_date')
    list_display_links =('first_name', 'id')
    search_fields =('first_name',  'role')
# Register your models here.

admin.site.register(Slider3)
admin.site.register(team, dashboardTeam)