import pytest

from pc.level_13 import solution


@pytest.mark.skip
def test_integration():
    expected = "italy"
    actual = solution(None)
    assert expected == actual
