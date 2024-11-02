import logging

import requests

from pc.level_01 import decrypt, solution

from . import def_template


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


def test_solution():
    actual = solution()
    expected = "ocr"
    assert expected == actual
    url = def_template.format(actual)
    logging.debug(f"Visiting {url}")
    resp = requests.get(url)
    assert resp.status_code == 200
