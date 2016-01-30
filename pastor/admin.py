from django.contrib import admin

from .models import pastor


class pastorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title','social_account', 'intro',)




admin.site.register(pastor, pastorAdmin)
