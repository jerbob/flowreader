"""Test business logic related to the 'meters' app."""

from django.conf import settings
from django.test import TestCase

from meters.logic import reader


FILES_DIR = settings.BASE_DIR.parent / "files"


class ReaderTestCase(TestCase):
    """Test case for relevant logic in meters.logic.reader."""

    def setUp(self) -> None:
        """Set up relevant test data paths."""
        self.valid_flow_file = FILES_DIR / "DTC5259515123502080915D0010.uff"

    def test_import_valid_flow_file(self) -> None:
        """Test that valid flow files can be imported successfully."""
        with self.valid_flow_file.open() as file:
            count = reader.import_readings_from_file(file)
        self.assertEqual(count, 35)
