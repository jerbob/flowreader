"""Database models used in the 'meters' app."""

from django.db import models


class MeterReading(models.Model):
    """Represents a reading taken from a provided meter point."""

    mpan_number = models.CharField(
        max_length=21,
        verbose_name="MPAN",
        help_text="Meter Point Administration Number.",
    )
    meter_serial_number = models.TextField(
        help_text="Serial number of the meter this reading was taken from."
    )
    reading = models.DecimalField(decimal_places=1, max_digits=255)
    reading_datetime = models.DateTimeField()
    flow_file = models.CharField(
        max_length=255, help_text="Flow file this reading was taken from."
    )
