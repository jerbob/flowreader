"""Forms for use in the meters app."""

from django.forms import ModelForm

from meters.models import MeterReading


class MeterReadingForm(ModelForm):
    """Form for validating and creating MeterReadings."""

    class Meta:
        model = MeterReading
        fields = [
            "mpan_number",
            "meter_serial_number",
            "reading",
            "reading_datetime",
            "flow_file",
        ]
