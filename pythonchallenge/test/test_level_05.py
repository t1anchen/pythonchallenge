from pathlib import Path

import pytest

from pc.level_05 import solution


def fetch_from_local():
    pickle_file_path = (
        Path(__file__) / ".." / "fixture" / "level_05" / "banner.p"
    ).resolve(True)
    with open(pickle_file_path, "rb") as reader:
        return reader.read()


# [2024-11-03T01:14:43+08:00] DO NOT concatenate them as single string in this
# code file, as the trailing whitespace chars would be automatically stripped
# when saving. Use list instead.
expected = pytest.fixture(
    lambda: [
        "                                                                                               ",
        "              #####                                                                      ##### ",
        "               ####                                                                       #### ",
        "               ####                                                                       #### ",
        "               ####                                                                       #### ",
        "               ####                                                                       #### ",
        "               ####                                                                       #### ",
        "               ####                                                                       #### ",
        "               ####                                                                       #### ",
        "      ###      ####   ###         ###       #####   ###    #####   ###          ###       #### ",
        "   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     #### ",
        "  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   #### ",
        " ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  #### ",
        " ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  #### ",
        "####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  #### ",
        "####           ####     ####   ##########    ####     ####  ####     #### ##############  #### ",
        "####           ####     ####  ###    ####    ####     ####  ####     #### ####            #### ",
        "####           ####     #### ####     ###    ####     ####  ####     #### ####            #### ",
        " ###           ####     #### ####     ###    ####     ####  ####     ####  ###            #### ",
        "  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   #### ",
        "   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    #### ",
        "      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######",
        "                                                                                               ",
    ]
)


def test_unit(expected):
    pickle_file_data = fetch_from_local()
    actual = solution(pickle_file_data)
    assert expected == actual


@pytest.mark.skip
def test_integration(expected):
    actual = solution(None)
    assert expected == actual
