import asyncio
import logging
import re
from io import BytesIO

import aiohttp
from bs4 import BeautifulSoup
from PIL import Image

from . import def_page_template, def_template


async def fetch_from_remote():
    url = def_page_template.format("oxygen")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            html_page = await resp.text("utf_8")
        parser = BeautifulSoup(html_page, "html.parser")
        logging.debug(f"{parser.find("body")=}")
        img_tag = parser.find("img")
        assert "src" in img_tag.attrs
        url = def_template.format(img_tag["src"])
        async with session.get(url) as resp:
            img_data = await resp.read()
        return img_data


def solution(data: bytes):
    if data is None:
        data = asyncio.run(fetch_from_remote())
    img = Image.open(BytesIO(data))
    logging.debug(f"Reading image {img.size}")
    grey_line = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
    unique_pixels_at_line = grey_line[::7]
    ords = [r for r, g, b, a in unique_pixels_at_line if r == g == b]
    hint = "".join(map(chr, ords))
    logging.debug(f"{hint=}")
    # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
    nums = re.findall(r"\d+", hint)
    ans = "".join(map(chr, map(int, nums)))
    logging.debug(f"{ans=}")
    return ans  # integrity
