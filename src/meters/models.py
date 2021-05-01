"""Database models used in the 'meters' app."""

from django.db import models


class MeterReading(models.Model):
    """Represents a reading taken from a provided meter point."""

    mpan = models.CharField(
        max_length=21,
        verbose_name="MPAN",
        help_text="Meter Point Administration Number.",
    )
    flow_file = models.CharField(
        max_length=255, help_text="Flow file this reading was taken from."
    )
    meter_serial_number = models.TextField(
        help_text="Serial number of the meter this reading was taken from."
    )
