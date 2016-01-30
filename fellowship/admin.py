from django.contrib import admin

from .models import fellowship


class fellowshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro',)


admin.site.register(fellowship, fellowshipAdmin)
