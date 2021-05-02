"""Test custom logic attached to pydantic models or dataclasses."""

from django.test import TestCase

import pytest

from meters.logic import types


class FlowGroupTestCase(TestCase):
    """Test custom logic on FlowGroup and descendants."""

    def test_group_not_implemented(self) -> None:
        """Test that unimplemented group types raise NotImplementedError."""
        with pytest.raises(NotImplementedError):
            types.FlowGroup.from_fields(27)
