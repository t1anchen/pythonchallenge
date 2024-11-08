import pytest

from pc.level_10 import solution


def test_unit():
    data = "a = [1, 11, 21, 1211, 111221,"
    expected = 5808
    actual = solution(data)
    assert expected == actual


@pytest.mark.skip
def test_integration():
    expected = 5808
    actual = solution(None)
    assert expected == actual
