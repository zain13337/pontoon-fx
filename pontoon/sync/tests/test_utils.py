from pontoon.sync.tests import LOCALE_SEPARATOR_TEST_PATH
from pontoon.sync.utils import uses_undercore_as_separator


def test_uses_undercore_as_separator():
    assert (uses_undercore_as_separator(LOCALE_SEPARATOR_TEST_PATH)) is True
