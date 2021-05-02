"""Management command to import and save meter readings from a flow file."""

from pathlib import Path
from django.core.management.base import BaseCommand, CommandError

from pydantic import ValidationError

from meters.logic.reader import import_readings_from_file


class Command(BaseCommand):
    """Management command to import and save meter readings from a flow file."""

    help = "Import and save MeterReadings from the provided file/s."

    def add_arguments(self, parser) -> None:
        """Add arguments for this command."""
        parser.add_argument("files", nargs="+", type=str)

    def handle(self, *args, **options) -> None:
        """Read the provided files and import from them."""
        file_count: int = 0
        reading_count: int = 0

        for file_path in options.get("files", ()):
            path = Path(file_path).resolve()
            if path.exists():
                with path.open() as file:
                    try:
                        count = import_readings_from_file(file)
                    except ValidationError as exception:
                        raise CommandError(
                            f"Invalid flow file entry was provided: {exception}"
                        )
                    else:
                        file_count += 1
                        reading_count += count
            else:
                raise CommandError(f"File {path} does not exist.")

        self.stdout.write(f"Imported {reading_count} readings from {file_count} files.")
