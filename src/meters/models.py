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
    meter_register = models.CharField(
        help_text="The meter register used to take this reading.", max_length=2
    )
    reading = models.DecimalField(
        decimal_places=1,
        max_digits=255,
        help_text="Decimal value for this meter reading.",
    )
    reading_datetime = models.DateTimeField(help_text="Time this reading was taken at.")
    flow_file = models.CharField(
        max_length=255, help_text="Flow file this reading was taken from."
    )

    def __str__(self) -> str:
        """Get a string representation of this reading for the admin site."""
        return f"Reading {self.pk}: Meter {self.meter_serial_number}"
