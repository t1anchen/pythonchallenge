from pc.level_08 import solution
import pytest


@pytest.mark.skip
def test_unit():
    data = (
        b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084",
        b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08",
        "/pc/return/good.html",
    )
    actual = solution(data)
    expected = ("huge", "file", "/pc/return/good.html")
    assert expected == actual


def test_integration():
    actual = solution(None)
    expected = ("huge", "file", "/pc/return/good.html")
    assert expected == actual
