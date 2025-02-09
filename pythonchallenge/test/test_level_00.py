import logging

import pytest
import requests

from pc.level_00 import solution
from pc.utils import def_page_template

actual = pytest.fixture(solution)


def test_unit(actual: str):
    expected = "274877906944"
    assert expected == actual


@pytest.mark.skip
def test_integration(actual: str):
    url = def_page_template.format(actual)
    logging.debug(f"Visiting {url}")
    resp = requests.get(url)
    assert resp.status_code == 200
