from pathlib import Path

import pytest

from pc.level_12 import solution


# @pytest.mark.skip
def test_unit():
    expected = "disproportional"
    img_path = (Path(__file__) / ".." / "fixture" / "level_12" / "evil2.gfx").resolve(
        True
    )
    with open(img_path, "rb") as reader:
        img_data = reader.read()
    actual = solution(img_data)
    assert expected == actual


@pytest.mark.skip
def test_integration():
    expected = "disproportional"
    actual = solution(None)
    assert expected == actual
