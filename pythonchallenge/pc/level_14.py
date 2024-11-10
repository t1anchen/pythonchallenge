"""Level 14: ITALY
"""

import asyncio
from io import BytesIO  # use cStringIO.StringIO if python2
from itertools import cycle
from typing import Optional
from urllib.parse import urljoin

import aiohttp
from PIL import Image

from .utils import fetch_bytes, pc_return_page_tmpl


async def fetch_from_remote():
    url = pc_return_page_tmpl.format("italy")
    async with aiohttp.ClientSession() as session:
        auth = aiohttp.BasicAuth("huge", "file")
        img_url = urljoin(url, "wire.png")
        img_data = await fetch_bytes(img_url, session, auth)
    return img_data


def solution(data: Optional[bytes]):
    """Twist line into square"""
    if data is None:
        data = asyncio.run(fetch_from_remote())

    # [2024-11-10T23:46:37+08:00] quoted from
    # http://wiki.pythonchallenge.com/level14
    #
    #   The hints tell us to spiral something round. The small image displayed
    #   on this page is deceptive; it is in fact a 10000x1 image (yes, 1 pixel
    #   high), which can be transformed into a 100x100 picture by spiralling
    #   it clockwards and inwards

    img_read = Image.open(BytesIO(data))
    delta = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])
    # Create new image by original mode of the image with 100x100
    img_write = Image.new(img_read.mode, (100, 100))
    x, y, x_origin = -1, 0, 0
    doubled_steps = 200
    while doubled_steps // 2 > 0:
        x_delta, y_delta = next(delta)
        for i in range(doubled_steps // 2):
            x, y = x + x_delta, y + y_delta
            img_write.putpixel((x, y), img_read.getpixel((x_origin, 0)))
            x_origin += 1
        doubled_steps -= 1
    img_write.show()  # it's a lovely kitty
    return "cat"


# [2024-11-10T23:49:53+08:00] alternative solution based on math from
# official guide
#
#     The basic idea behind this solution is that the value of x and y
#     depend entirely on the three parameters: width, height and n,
#     where n is an integer greater than or equal to 0. The only minor
#     advantage to this solution is that you don't need to keep track
#     of nearly as many variables as they can all be computed from the
#     input (after hard-coding width and height dependant pieces). It's
#     even possible to go backwards if you feel like rendering the
#     output image a line at a time.

# def getpixel(t):
#     t = (100*100-1) - t
#     shell = int((math.sqrt(t) + 1)/2)
#     if shell == 0:
#         leg = 0
#     else:
#         leg = int((t - (2*shell-1)**2)/2/shell)
#     elem = t - (2*shell-1)**2-2*shell*leg-shell+1

#     if leg == 0:
#         x = shell
#         y = elem
#     elif leg == 1:
#         x = -elem
#         y = shell
#     elif leg == 2:
#         x = -shell
#         y = -elem
#     else:
#         x = elem
#         y = -shell
#     return (49+x,50-y)

# inim = Image.open("wire.png")
# outim = Image.new("RGB", (100,100))

# for i,px in enumerate(inim.getdata()):
#     outim.putpixel(getpixel(i), px)

# outim.show()
