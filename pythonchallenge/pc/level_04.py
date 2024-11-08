import asyncio
import re
from collections import deque

import aiohttp
import requests


# [2024-11-02T23:57:45+08:00] The entire walkthrough will cost at least 1 min
# (averagely 79.79s if using aiohttp, slower if using requests). Based on the
# latest testing result, it will stop after bouncing 250 times.
async def trampoline_fetch():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    n = "12345"
    n_jump = 0
    async with aiohttp.ClientSession() as session:
        while len(re.findall(r"\d+", n)) > 0:
            if n_jump > 400:
                break
            params = {"nothing": n}
            async with session.get(url, params=params) as resp:
                resp_text = await resp.text("utf_8")
            numbers = re.findall(r"\d+", resp_text)
            if re.search("[Dd]ivide", resp_text):
                n = str(int(n) // 2)
            elif len(numbers) > 1:
                # misleading number case (82682)
                n = deque(numbers, maxlen=1).pop()
            elif len(numbers) > 0:
                n = numbers[0]
            elif re.search("html", resp_text):
                # end case
                n = re.sub(r"(.+)\.html", r"\1", resp_text)
            # logging.debug(f"{n_jump=} {resp_text=} {n=}")
            n_jump += 1
    return n


def solution():
    n = asyncio.run(trampoline_fetch())
    return n  # 'peak'
