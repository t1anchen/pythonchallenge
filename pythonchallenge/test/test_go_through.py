import re

import requests

import pc.level_00
import pc.level_01
import pc.level_04
import pc.level_12
import pc.level_13
import pc.level_14
import pc.level_15
import pc.level_16
import pc.level_17

def_template = "http://www.pythonchallenge.com/pc/def/{0}.html"
pc_return_tmpl = "http://www.pythonchallenge.com/pc/return/{0}"


# def test_level_00():
#     template = def_template
#     try:
#         r = requests.get(template.format(pc.level_00.solution()))
#     except:
#         raise

#     next_entry = [
#         re.sub(
#             r"(.*)URL=(.*)\.html\"\>",  # Python3 `line' would be bytestring
#             r"\2",
#             line.decode(),
#         )
#         for line in r.iter_lines()
#         if re.match(r".*URL.*", line.decode())
#     ]
#     actual = next_entry[0]
#     expected = "map"
#     assert actual == expected


def test_level_12():
    actual = pc.level_12.solution()
    expected = "disproportional"
    assert expected == actual
    pc.level_12.clean()


def test_level_13():
    actual = pc.level_13.solution()
    expected = "ITALY"
    assert expected == actual


def test_level_14():
    actual = pc.level_14.solution()
    expected = "cat"
    assert expected == actual


def test_level_15():
    actual = pc.level_15.solution()
    expected = "mozart"
    assert expected == actual


def test_level_16():
    actual = pc.level_16.solution()
    expected = "romance"
    assert expected == actual


def test_level_17():
    actual = pc.level_17.solution()
    expected = "balloons"
    assert expected == actual
