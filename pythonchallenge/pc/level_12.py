import asyncio
import logging
import os
from enum import Enum
from io import BytesIO
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin

import aiohttp
from PIL import Image

from .utils import fetch_bytes, fetch_first_img, pc_return_page_tmpl


class IMG_HEADER(Enum):
    JPEG = b"\xFF\xD8\xFF\xE0"
    PNG = b"\x89PNG\x0D\x0A\x1A\x0A"
    GIF = b"GIF87a"


async def fetch_from_remote():
    url = pc_return_page_tmpl.format("evil")
    async with aiohttp.ClientSession() as session:
        auth = aiohttp.BasicAuth("huge", "file")
        img_data = await fetch_first_img(url, session, auth)
        evil1 = Image.open(BytesIO(img_data))
        # evil1.show() # 5 decks
        evil2_url = urljoin(url, "evil2.jpg")
        img_data = await fetch_bytes(evil2_url, session, auth)
        evil2 = Image.open(BytesIO(img_data))
        # evil2.show() # not jpg, _.gfx
        evil2_gfx_url = urljoin(url, "evil2.gfx")
        evil2_gfx = await fetch_bytes(evil2_gfx_url, session, auth)
        logging.debug(f"{len(evil2_gfx)=}")
        evil3_url = urljoin(url, "evil3.jpg")
        img_data = await fetch_bytes(evil3_url, session, auth)
        evil3 = Image.open(BytesIO(img_data))
        # evil3.show() # no more evils

        # [2024-11-10T00:20:36+08:00] it looks like
        # http://www.pythonchallenge.com/pc/return/evil4.jpg shows error, but
        # this jpg contains important hints for Level 13. It prompted "Bert is
        # evil".
    return evil2_gfx


def solution(data: Optional[bytes]):
    if data is None:
        data = asyncio.run(fetch_from_remote())
    decks = [[] for _ in range(5)]
    # decks = [BytesIO() for _ in range(5)]

    # dispatch bytes to decks
    for i in range(len(data)):
        decks[(i % 5)].append(data[i])
    for i in range(5):
        decks[i] = bytes(decks[i])

    # identify image types
    suffixes = [""] * 5
    for i in range(5):
        if decks[i].startswith(IMG_HEADER.PNG.value):
            suffixes[i] = ".png"
        elif decks[i].startswith(IMG_HEADER.JPEG.value):
            suffixes[i] = ".jpg"
        elif decks[i].startswith(IMG_HEADER.GIF.value):
            suffixes[i] = ".gif"

    # [2024-11-09T17:16:06+08:00] quoted from
    # http://wiki.pythonchallenge.com/level12,
    #
    #     The fourth image may not load in all PNG viewers, because it has
    #     been truncated to fit in the pile of images; Firefox is tolerant
    #     enough to show what it can; you can also try and pad the data with
    #     zeros until it can be loaded (use PIL to automate this). As is,
    #     PIL can create an Image from the fourth piece, but cannot save it
    #     (im.save() and im.show() fail).
    #
    # therefore preserving images can be done by file.write instead of im.save

    tmp_dir_path = Path(os.getenv("ONE_R1NG_TMP_DIR", "."))
    prefix = "pythonchallenge-level_12"
    for i, deck in enumerate(decks):
        with open(
            tmp_dir_path / (f"{prefix}-img{i:02d}" + suffixes[i]), "wb"
        ) as writer:
            writer.write(deck)

    # [2024-11-09T21:32:36+08:00] Use firefox to open the images
    #
    # img00.jpg -> dis
    # img01.png -> pro
    # img02.gif -> port
    # img03.png -> ional (img only shows as half)
    # img04.jpg -> ity (with striked)

    return "disproportional"


# def solution():
# evil.html -> evil1.jpg -> 5 decks
# evil2.jpg -> not jpg - -.gfx
# evil3.jpg -> no more evils
# url = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
# auth_ctx = ("huge", "file")
# res = requests.get(url, auth=auth_ctx)
# # https://www.cs.duke.edu/courses/cps124/fall01/code/gfx_reader/docs/gfx_format.html
# gfx_stream = res.iter_content()
# decks = [[] for i in range(5)]
# i = cycle(range(5))
# for gfx_byte in gfx_stream:
#     decks[next(i)].append(gfx_byte)  # dispatch card to 5 decks
# for i in range(5):
#     with open("img{0:02d}.gfx".format(i), "wb") as f:
#         f.write(b"".join(decks[i]))  # Python3 byte string
# TODO: get font from gfx image
# img00.gfx -> dis
# img01.gfx -> pro
# img02.gfx -> port
# img03.gfx -> ional
# img04.gfx -> i̶t̶y̶ (abandoned, strikethrough combining U+0336) # if python2, add coding utf8 ahead of this file

# return "disproportional"


# def clean():
#     filenames = ["img{0:02d}.gfx".format(i) for i in range(5)]
#     for fn in filenames:
#         os.remove(fn)
