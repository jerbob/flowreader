"""Type definitions and constraints for flow readings."""

from datetime import datetime
from decimal import Decimal

from typing import ClassVar, Optional, Union

from pydantic import validator
from pydantic.types import conint, constr
from pydantic.dataclasses import dataclass

from typing_extensions import Final, Literal


TRAILER_GROUP: Final[str] = "ZPT"


@dataclass
class FileHeader:
    """Type constraints for a D0010 flow file header."""

    group_name: Union[Literal["ZHF"], Literal["ZHV"]]

    # pyright: reportGeneralTypeIssues=false
    # Pydantic's constr() calls are not fully PEP 484 compliant

    file_identifier: constr(min_length=10, max_length=10)
    flow_version_number: constr(min_length=8, max_length=8, regex=r"D.{4}\d{3}")
    from_role_code: constr(min_length=1, max_length=1)
    from_participant: constr(min_length=4, max_length=4)
    to_role_code: constr(min_length=1, max_length=1)
    to_participant: constr(min_length=4, max_length=4)
    creation_time: constr(min_length=14, max_length=14)

    sending_application: Optional[constr(min_length=5, max_length=5)]
    receiving_application: Optional[constr(min_length=5, max_length=5)]
    broadcast: Optional[constr(min_length=1, max_length=1)]
    test_data_flag: Optional[constr(min_length=4, max_length=4)]


@dataclass
class FlowGroup:
    """Generic base class for flow reading groups."""

    group_number: conint(ge=26, le=33)

    @classmethod
    def from_fields(cls, *fields) -> "FlowGroup":
        """Validate group number, and return the relevant FlowGroup instance."""
        first_field, *fields = fields
        number = cls(first_field).group_number

        for flow_group in cls.__subclasses__():
            # Find the FlowGroup with this group number
            if flow_group.group_number == number:
                return flow_group(*fields)

        raise NotImplementedError(
            "The FlowGroup for this group ID has not been implemented."
        )


@dataclass
class MPANCoreGroup(FlowGroup):
    """Type constraints for the 'MPAN Cores' flow group."""

    group_number: ClassVar[int] = 26

    mpan_core_id: constr(min_length=1, max_length=13)
    bsc_validation_status: constr(min_length=1, max_length=1)


@dataclass
class MeterReadingGroup(FlowGroup):
    """Type constraints for the 'Meter/Reading Types' flow group."""

    group_number: ClassVar[int] = 28

    mpan_core_id: constr(min_length=1, max_length=13)
    bsc_validation_status: constr(min_length=1, max_length=1)


@dataclass
class RegisterReadingsGroup(FlowGroup):
    """Type constraints for the 'Register Readings' flow group."""

    group_number: ClassVar[int] = 30

    meter_register: str
    reading_datetime: datetime
    register_reading: Decimal

    md_reset_time: Optional[str]
    md_reset_number: Optional[int]
    meter_reading_flag: Optional[str]

    reading_method: constr(min_length=1, max_length=1)

    @validator("reading_datetime", pre=True)
    def parse_datetime(cls, value: str) -> datetime:
        """Parse the datetime format for D0010 files."""
        return datetime.strptime(value, "%Y%m%d%H%M%S")


@dataclass
class FileTrailer:
    """Type constraints for a D0010 flow file trailer."""

    group_name: Literal["ZPT"]

    file_identifier: constr(min_length=10, max_length=10)
    total_group_count: int
    checksum: Optional[constr(min_length=10, max_length=10)]
    flow_count: int
    file_completion_timestamp: constr(min_length=14, max_length=14)
