from django.contrib import admin

from .models import report


class reportAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time')





admin.site.register(report, reportAdmin)
