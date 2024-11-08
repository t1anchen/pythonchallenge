import gzip
import logging
import re
from pathlib import Path

import pytest
import requests

from pc import def_page_template
from pc.level_03 import solution


def test_unit():
    expected = "linkedlist"
    test_data_path = (Path(__file__) / ".." / "fixture" / "level_03.txt.gz").resolve(
        strict=True
    )
    with gzip.open(test_data_path, mode="rt", encoding="utf_8") as reader:
        actual = solution(reader.read())
        assert expected == actual


@pytest.mark.skip
def test_integration():
    expected = "linkedlist"
    url = def_page_template.format("equality")
    logging.debug(f"Visiting {url}")
    resp = requests.get(url)
    matched = re.findall(r"<!--([^>]*)-->", resp.text)
    assert len(matched) >= 1
    haystack = matched[0]
    actual = solution(haystack)
    assert expected == actual
