"""Logic related to parsing and creating models from flow files."""

import csv
from pathlib import Path
from io import TextIOWrapper
from typing import Generator, Iterable, List, Optional

from meters.models import MeterReading
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


def import_readings_from_file(file: TextIOWrapper) -> int:
    """Import readings from a file."""
    reading_count: int = 0
    csv_rows = filtered_csv_rows(csv.reader(file, delimiter="|"))

    form_fields = {}
    header = FileHeader(*next(csv_rows))

    for row in csv_rows:
        group_number, *fields = row

        if group_number == TRAILER_GROUP:
            trailer = FileTrailer(group_number, *fields)
            break

        flow_group = FlowGroup.from_fields(group_number, *fields)

        if type(flow_group) is MPANCoreGroup:
            form_fields["mpan_number"] = flow_group.mpan_core_id

        elif type(flow_group) is MeterReadingGroup:
            form_fields["meter_serial_number"] = flow_group.mpan_core_id

        elif type(flow_group) is RegisterReadingsGroup:
            form_fields["reading"] = flow_group.register_reading
            form_fields["reading_datetime"] = flow_group.reading_datetime
            print(form_fields)
            reading_count += 1
            form_fields.clear()

    return reading_count
