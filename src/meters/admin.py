"""Registered admin model classes for the admin site."""

from django.contrib import admin

from .models import MeterReading


@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    ...
