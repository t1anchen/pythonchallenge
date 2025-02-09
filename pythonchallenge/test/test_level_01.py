import logging

import pytest
import requests

from pc.level_01 import decrypt, solution
from pc.utils import def_page_template


def test_decrypt():
    test_data = (
        """g fmnc wms bgblr rpylqjyrc gr zw fylb. """
        + """rfyrq ufyr amknsrcpq ypc dmp. """
        + """bmgle gr gl zw fylb gq glcddgagclr ylb """
        + """rfyr'q ufw rfgq rcvr gq qm jmle. """
        + """sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. """
        + """lmu ynnjw ml rfc spj."""
    )
    actual = decrypt(test_data)
    expected = (
        """i hope you didnt translate it by hand. """
        + """thats what computers are for. """
        + """doing it in by hand is inefficient and """
        + """that's why this text is so long. """
        + """using string.maketrans() is recommended. """
        + """now apply on the url."""
    )
    assert expected == actual


actual = pytest.fixture(solution)


def test_unit(actual):
    expected = "ocr"
    assert expected == actual


@pytest.mark.skip
def test_integration(actual):
    url = def_page_template.format(actual)
    logging.debug(f"Visiting {url}")
    resp = requests.get(url)
    assert resp.status_code == 200
