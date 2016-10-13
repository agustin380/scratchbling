from django.contrib import admin

from .models import BackScratcher


@admin.register(BackScratcher)
class BackScratcherAdmin(admin.ModelAdmin):
    pass
