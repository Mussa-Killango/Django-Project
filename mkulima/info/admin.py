from django.contrib import admin

from .models import FarmItem


class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(FarmItem, InfoAdmin)
