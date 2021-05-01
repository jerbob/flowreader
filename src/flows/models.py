from django.db import models


class MeterReading(models.Model):
    """Represents a reading taken from a provided meter point."""

    mpan = models.CharField(
        max_length=21, verbose_name="Meter Point Administration Number."
    )
    flow_file = models.CharField(
        max_length=255, verbose_name="Flow file this reading was taken from."
    )
    meter_serial_number = models.TextField(
        verbose_name="Serial number of the meter this reading was taken from."
    )
