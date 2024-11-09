from pathlib import Path

import pytest

from pc.level_11 import solution


def test_unit():
    expected = "evil"
    img_path = (Path(__file__) / ".." / "fixture" / "level_11" / "cave.jpg").resolve(
        True
    )
    with open(img_path, "rb") as reader:
        img_data = reader.read()
    actual = solution(img_data)
    assert expected == actual


@pytest.mark.skip
def test_integration():
    expected = "evil"
    actual = solution(None)
    assert expected == actual
