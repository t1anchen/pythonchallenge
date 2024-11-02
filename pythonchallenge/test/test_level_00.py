import logging

import pytest
import requests

from pc import def_template
from pc.level_00 import solution

actual = pytest.fixture(solution)


def test_unit(actual: str):
    expected = "274877906944"
    assert expected == actual


def test_integration(actual: str):
    url = def_template.format(actual)
    logging.debug(f"Visiting {url}")
    resp = requests.get(url)
    assert resp.status_code == 200
