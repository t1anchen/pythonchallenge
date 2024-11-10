from pathlib import Path

import pytest

from pc.level_14 import solution


def test_unit():
    expected = "cat"
    img_path = (Path(__file__) / ".." / "fixture" / "level_14" / "wire.png").resolve(
        True
    )
    with open(img_path, "rb") as reader:
        img_data = reader.read()
    actual = solution(img_data)
    assert expected == actual


@pytest.mark.skip
def test_integration():
    expected = "cat"
    actual = solution(None)
    assert expected == actual
