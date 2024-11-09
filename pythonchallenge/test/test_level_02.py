import gzip
import logging
import re
from pathlib import Path

import pytest
import requests

from pc.level_02 import solution
from pc.utils import def_page_template


def test_unit():
    expected = "equality"
    test_data_path = (Path(__file__) / ".." / "fixture" / "level_02.txt.gz").resolve(
        strict=True
    )
    with gzip.open(test_data_path, mode="rt", encoding="utf_8") as reader:
        actual = solution(reader.read())
        assert expected == actual


@pytest.mark.skip
def test_integration():
    expected = "equality"
    url = def_page_template.format("ocr")
    logging.debug(f"Visiting {url}")
    resp = requests.get(url)
    matched = re.findall(r"<!--([^>]*)-->", resp.text)
    assert len(matched) >= 2
    haystack = matched[1]
    actual = solution(haystack)
    assert expected == actual
