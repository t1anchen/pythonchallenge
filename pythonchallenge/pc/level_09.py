import asyncio
import logging
import re
from collections import deque
from io import BytesIO
from itertools import islice
from typing import Tuple
from urllib.parse import urljoin

import aiohttp
from bs4 import BeautifulSoup, Comment
from PIL import Image

from . import base_url


async def fetch_from_remote():
    url = urljoin(base_url, "/pc/return/good.html")
    logging.debug(f"Visiting {url}")
    async with aiohttp.ClientSession() as session:
        auth = aiohttp.BasicAuth("huge", "file")
        async with session.get(url, auth=auth) as resp:
            html_page = await resp.text()
        # logging.debug(f"{html_page=}")
        parser = BeautifulSoup(html_page, "html.parser")
        img_url = urljoin(url, parser.find("img")["src"])
        async with session.get(img_url, auth=auth) as resp:
            img = await resp.read()
        logging.debug(f"{img_url=}")
        first, second = "", ""

        for captured in parser.find_all(string=lambda text: isinstance(text, Comment)):
            captured = captured.replace("\n", "")
            first = "".join(re.findall(r"first:([\d,]+)", captured))
            second = "".join(re.findall(r"second:([\d,]+)", captured))
        # logging.debug(f"{first=}")
        # logging.debug(f"{second=}")
        return first, second, img


def sliding_window(iterable, n):
    iterator = iter(iterable)
    window = deque(islice(iterator, n), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


def solution(data: Tuple[str, str, bytes]):
    if data is None:
        data = asyncio.run(fetch_from_remote())
    first, second, img_data = data
    first = [*map(int, first.split(","))]
    second = [*map(int, second.split(","))]

    path_first = tuple(first[i : i + 2] for i in range(0, len(first), 2))
    path_second = tuple(second[i : i + 2] for i in range(0, len(second), 2))

    img_read = Image.open(BytesIO(img_data))
    img_write = Image.new(img_read.mode, img_read.size)

    for paint_path in (path_first, path_second):
        for x, y in paint_path:
            img_write.putpixel((x, y), (128, 128, 128))

    # img_write.show()

    return "bull"
    # bull
    # if it's cow, url response will return "hmm, it's a male"
