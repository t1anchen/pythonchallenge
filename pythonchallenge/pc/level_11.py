import asyncio
import logging
from io import BytesIO
from itertools import product
from typing import Optional
from urllib.parse import urljoin

import aiohttp
from bs4 import BeautifulSoup
from PIL import Image

from .utils import pc_return_page_tmpl


async def fetch_from_remote():
    url = pc_return_page_tmpl.format("5808")
    async with aiohttp.ClientSession() as session:
        auth = aiohttp.BasicAuth("huge", "file")
        logging.debug(f"Visitng {url}")
        async with session.get(url, auth=auth) as resp:
            html_page = await resp.text()
        parser = BeautifulSoup(html_page, "html.parser")
        img_tag = parser.find("img")
        assert "src" in img_tag.attrs
        img_url = urljoin(url, img_tag["src"])
        async with session.get(img_url, auth=auth) as resp:
            img_data = await resp.read()
        return img_data


def solution(data: Optional[bytes]):
    if data is None:
        data = asyncio.run(fetch_from_remote())
    img_read = Image.open(BytesIO(data))
    M, N = img_read.size
    even = Image.new("RGB", (M // 2, N // 2))
    odd = Image.new("RGB", (M // 2, N // 2))
    for x, y in product(range(M), range(N)):
        if x % 2 == 0 and y % 2 == 0:
            even.putpixel((x >> 1, y >> 1), img_read.getpixel((x, y)))
        elif x % 2 == 0 and y % 2 == 1:
            odd.putpixel((x >> 1, (y - 1) >> 1), img_read.getpixel((x, y)))
        elif x % 2 == 1 and y % 2 == 0:
            even.putpixel(((x - 1) >> 1, y >> 1), img_read.getpixel((x, y)))
        else:
            odd.putpixel(((x - 1) >> 1, (y - 1) >> 1), img_read.getpixel((x, y)))
    # even.show("even")
    odd.show("odd")
    return "evil"
