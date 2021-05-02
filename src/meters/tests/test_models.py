"""Test properties and methods on models in the 'meters' app."""

from decimal import Decimal

from django.test import TestCase
from django.utils import timezone

from meters import models


class MeterReadingTestCase(TestCase):
    """Test methods on the 'MeterReading' model."""

    def setUp(self) -> None:
        """Set up a valid MeterReading model for tests."""
        self.meter_reading = models.MeterReading.objects.create(
            mpan_number="2000055433806",
            meter_serial_number="D13C01717",
            meter_register="01",
            reading=Decimal("7242.0"),
            reading_datetime=timezone.now(),
            flow_file="DTC5259515123502080915D0010.uff",
        )

    def test_model_str(self) -> None:
        """Test the __str__ method on MeterReadings."""
        self.assertEqual(str(self.meter_reading), f"Reading 1: Meter D13C01717")
