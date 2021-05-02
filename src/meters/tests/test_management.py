"""Test management commands associated with the 'meters' app."""

from io import StringIO
from typing import Tuple

from django.conf import settings
from django.core.management import call_command, CommandError
from django.test import TestCase

import pytest


FILES_DIR = settings.BASE_DIR.parent / "files"


class ImportFlowFileTestCase(TestCase):
    """Test the './manage.py import_flow_file' command."""

    def setUp(self) -> None:
        """Set up paths to flow files for testing."""
        self.valid_flow_file = str(FILES_DIR / "DTC5259515123502080915D0010.uff")
        self.invalid_flow_file = str(FILES_DIR / "INVALID.uff")
        self.nonexistent_flow_file = "NONEXISTENT.uff"

    def import_files(self, *files: str) -> Tuple[str, str]:
        """Call the import_flow_file management command, and return output."""
        stdout, stderr = StringIO(), StringIO()
        call_command("import_flow_file", files, stdout=stdout, stderr=stderr)
        return stdout.getvalue(), stderr.getvalue()

    def test_import_valid_flow_file(self) -> None:
        """Test that valid flow files can be imported successfully."""
        stdout, _ = self.import_files(self.valid_flow_file)
        self.assertIn("Imported 35 readings from 1 files", stdout)

    def test_import_invalid_flow_file(self) -> None:
        """Test that invalid flow files raise the relevant CommandError."""
        with pytest.raises(CommandError):
            _, stderr = self.import_files(self.invalid_flow_file)
            self.assertIn("Invalid flow file entry was provided", stderr)

    def test_import_nonexistent_flow_file(self) -> None:
        """Test that nonexistent flow files raise the relevant CommandError."""
        with pytest.raises(CommandError):
            _, stderr = self.import_files(self.nonexistent_flow_file)
            self.assertIn("File {self.nonexistent_flow_file} does not exist.", stderr)
