import logging

import pytest
import requests

from pc.level_00 import solution

from . import def_template


def test_solution():
    expected = "274877906944"
    actual = solution()
    assert expected == actual
    url = def_template.format(actual)
    logging.debug(f"Visiting {url}")
    resp = requests.get(url)
    assert resp.status_code == 200
