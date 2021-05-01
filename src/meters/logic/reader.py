"""Logic related to parsing and creating models from flow files."""

import csv
from pathlib import Path
from io import TextIOWrapper
from typing import Generator, Iterable, List, Optional

from meters.forms import MeterReadingForm
from meters.logic.types import (
    TRAILER_GROUP,
    FlowGroup,
    FileHeader,
    FileTrailer,
    MPANCoreGroup,
    MeterReadingGroup,
    RegisterReadingsGroup,
)


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
    csv_rows = filtered_csv_rows(csv.reader(file, delimiter="|"))

    header = FileHeader(*next(csv_rows))
    form_fields = {"flow_file": filename}

    for row in csv_rows:
        group_number, *fields = row

        if group_number == TRAILER_GROUP:
            trailer = FileTrailer(group_number, *fields)
            break

        flow_group = FlowGroup.from_fields(group_number, *fields)
        form_fields.update(flow_group.get_form_fields())

        if type(flow_group) is RegisterReadingsGroup:
            form = MeterReadingForm(form_fields)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)

            reading_count += 1

    return reading_count
