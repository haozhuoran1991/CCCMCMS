from django.contrib import admin

from home.models import daily_motto
from home.models import SundaySchool


class mottoAdmin(admin.ModelAdmin):
    list_display = ('motto','pub_date','update_time')


class SundaySchoolAdmin(admin.ModelAdmin):
    list_display = ( 'name','teacher','classroom','intro')



admin.site.register(daily_motto, mottoAdmin)
admin.site.register(SundaySchool, SundaySchoolAdmin)