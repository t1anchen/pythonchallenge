import asyncio
import bz2
import re
from typing import Optional, Tuple
from urllib.parse import urljoin, urlsplit

import aiohttp
from bs4 import BeautifulSoup

from . import def_page_template, pc_return_tmpl


def str2bytes(s) -> bytes:
    """convert str with '\\x00...' to bytes"""
    return bytes(s, "utf_8").decode("unicode_escape").encode("latin1")


async def fetch_from_remote():
    url = def_page_template.format("integrity")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp_text = await resp.text()
        # logging.debug(f"{resp_text=}")
        parser = BeautifulSoup(resp_text, "html.parser")
        area_tag = parser.find("area")
        assert "href" in area_tag.attrs
        url = urljoin(url, area_tag["href"])
        hint = urlsplit(url).path
        un, pw = next(
            (
                (matched.group("un"), matched.group("pw"))
                for matched in re.finditer(
                    r"<!-- un: '(?P<un>.+)' pw: '(?P<pw>.+)' -->",
                    resp_text.replace("\n", " "),
                )
            ),
            ("", ""),
        )
        un_bytes, pw_bytes = str2bytes(un), str2bytes(pw)
        # logging.debug(f"{un_bytes=} {pw_bytes=}")
        return un_bytes, pw_bytes, hint


def solution(data: Optional[Tuple[bytes, bytes, str]]):
    if data is None:
        data = asyncio.run(fetch_from_remote())
    un, pw, hint = data
    return (bz2.decompress(un).decode(), bz2.decompress(pw).decode(), hint)
    # "huge", "file", "/pc/return/good.html"


# class SolutionTest(unittest.TestCase):

#     def setUp(self):
#         self.prefix = "http://www.pythonchallenge.com/pc/return/"
#         self.suffix = ".html"

#     def test_solution(self):
#         actual = solution()
#         # It would be identified by pep8, but this is ascii art, who cares!
#         expected = ("huge", "file")
#         self.assertEquals(actual, expected)
#         # Trick: hockey is consist of letters of oxygen
#         origin_url = "".join([self.prefix, "good", self.suffix])
#         try:
#             r = requests.get(origin_url, auth=expected)
#         except:
#             raise
#         self.assertTrue(r.ok)
#         next_entry = [
#             re.sub(r"(.*)URL=(.*)\.html\"\>", r"\2", line)
#             for line in r.iter_lines()
#             if re.match(r".*URL.*", line)
#         ]
#         r.close()
#         if len(next_entry) != 0:
#             r = requests.get(
#                 "".join([self.prefix, next_entry[0], self.suffix], auth=expected)
#             )
#             logging.warn("Level 09 is %s with %s" % (r.url, expected))
#         else:
#             logging.warn("Level 09 is %s with %s" % (origin_url, expected))


# if __name__ == "__main__":
#     unittest.main(failfast=True)
