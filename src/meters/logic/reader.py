"""Logic related to parsing and creating models from flow files."""

import csv
from pathlib import Path
from io import TextIOWrapper
from typing import Generator, Iterable, List, Optional

from django.core.management.base import CommandError

from pydantic import ValidationError

from meters.forms import MeterReadingForm
from meters.logic import types


def filtered_csv_rows(
    csv_reader: Iterable[List[str]],
) -> Generator[List[Optional[str]], None, None]:
    """Filter the results of the csv.reader iterable."""
    for row in csv_reader:
        # Rows are terminated by a delimiter, resulting in empty end fields
        # also explicitly use 'None' if a field was not specified
        yield [field or None for field in row[:-1]]


def import_readings_from_file(file: TextIOWrapper, filename: str) -> int:
    """Import readings from a file."""
    reading_count: int = 0
    form_fields = {"flow_file": filename}

    csv_rows = filtered_csv_rows(csv.reader(file, delimiter="|"))

    types.FileHeader(*next(csv_rows))  # Validate file header

    for row in csv_rows:
        group_number, *fields = row
        if group_number == types.TRAILER_GROUP:
            types.FileTrailer(group_number, *fields)  # Validate file trailer
            break

        try:
            flow_group = types.FlowGroup.from_fields(group_number, *fields)
            reading_count += 1
        except ValidationError as exception:
            raise CommandError(f"Invalid flow file entry was provided: {exception}")
        else:
            form_fields.update(flow_group.get_form_fields())

        if type(flow_group) is types.RegisterReadingsGroup:
            form = MeterReadingForm(form_fields)
            if form.is_valid():
                form.save()

    return reading_count
