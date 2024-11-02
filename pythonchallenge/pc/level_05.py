import asyncio
import logging
import pickle

import aiohttp
from bs4 import BeautifulSoup

from . import def_page_template, def_template


async def fetch_from_remote():
    async with aiohttp.ClientSession() as session:
        url = def_page_template.format("peak")
        logging.debug(f"Visiting {url}")
        async with session.get(url) as resp:
            html_page = await resp.text("utf_8")
        parser = BeautifulSoup(html_page, "html.parser")
        peakhell_tag = parser.find("peakhell")
        assert peakhell_tag is not None
        assert "src" in peakhell_tag.attrs
        pickle_file = peakhell_tag["src"]
        logging.debug(f"Found {pickle_file}")
        download_url = def_template.format(pickle_file)
        logging.debug(f"Downloading {download_url}")
        async with session.get(download_url) as resp:
            pickle_file_data = await resp.read()
        return pickle_file_data


def solution(data: bytes):
    if data is None:
        data = asyncio.run(fetch_from_remote())
    banner = pickle.loads(data)
    # logging.debug(f"{banner=}")
    ans = []
    for group in banner:
        ans.append("".join(c * n_c for c, n_c in group))
    return ans  # channel
