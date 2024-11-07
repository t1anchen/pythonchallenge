from pathlib import Path

import pytest

from pc.level_06 import solution


def fetch_from_local():
    zip_file_path = (
        Path(__file__) / ".." / "fixture" / "level_06" / "channel.zip"
    ).resolve()
    with open(zip_file_path, "rb") as reader:
        return reader.read()


def test_unit():
    zip_file_data = fetch_from_local()
    actual = solution(zip_file_data)
    expected = [
        "****************************************************************",
        "****************************************************************",
        "**                                                            **",
        "**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **",
        "**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **",
        "**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **",
        "**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **",
        "**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **",
        "**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **",
        "**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **",
        "**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **",
        "**                                                            **",
        "****************************************************************",
        " **************************************************************",
        "",
    ]
    assert expected == actual


@pytest.mark.skip
def test_integration():
    actual = solution()
