from pathlib import Path

import pytest

from pc.level_07 import solution


def test_unit():
    img_path = (Path(__file__) / ".." / "fixture" / "level_07" / "oxygen.png").resolve(
        True
    )
    with open(img_path, "rb") as stream:
        img_data = stream.read()
    actual = solution(img_data)
    expected = "integrity"
    assert expected == actual


@pytest.mark.skip
def test_integration():
    actual = solution(None)
