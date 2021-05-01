"""Registered admin model classes for the admin site."""

from django.contrib import admin

from .models import MeterReading


@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    list_display = [
        "mpan_number",
        "meter_serial_number",
        "meter_register",
        "reading",
        "reading_datetime",
    ]
    search_fields = ["mpan_number", "meter_serial_number"]
