import asyncio
from itertools import groupby, islice
from typing import Optional
from urllib.parse import urljoin

import aiohttp
from bs4 import BeautifulSoup


async def fetch_from_remote():
    url = "http://www.pythonchallenge.com/pc/return/bull.html"
    async with aiohttp.ClientSession() as session:
        auth = aiohttp.BasicAuth("huge", "file")
        async with session.get(url, auth=auth) as resp:
            html_page = await resp.text()
        parser = BeautifulSoup(html_page, "html.parser")
        area_tag = parser.find("area")
        assert "href" in area_tag.attrs
        url = urljoin(url, area_tag["href"])
        async with session.get(url, auth=auth) as resp:
            seq_text = await resp.text()
        return seq_text.strip()


def look_and_say_seq():
    """OEIS A005150

    Reference
    ---------

    - http://oeis.org/A005150
    - https://mathworld.wolfram.com/LookandSaySequence.html
    """
    x = "1"
    while True:
        yield x
        x = "".join(str(len(list(g))) + k for k, g in groupby(x))
        # 2.62 ms ± 42.2 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
        # x = "".join(str(sum(1 for _ in g)) + k for k, g in groupby(x))
        # 4.12 ms ± 29.5 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)


def solution(data: Optional[str]):
    if data is None:
        data = asyncio.run(fetch_from_remote())
    x_30 = next(islice(look_and_say_seq(), 30, None))
    return len(x_30)
