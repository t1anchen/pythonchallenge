import logging
from typing import Optional
from urllib.parse import urljoin

import aiohttp
from bs4 import BeautifulSoup

def_page_template = "http://www.pythonchallenge.com/pc/def/{0}.html"
def_template = "http://www.pythonchallenge.com/pc/def/{0}"
pc_return_tmpl = "http://www.pythonchallenge.com/pc/return/{0}"
pc_return_page_tmpl = "http://www.pythonchallenge.com/pc/return/{0}.html"
base_url = "http://www.pythonchallenge.com"


async def fetch_html_page(
    url: str,
    session: aiohttp.ClientSession,
    auth: Optional[aiohttp.BasicAuth] = None,
) -> str:
    logging.debug(f"Visitng {url}")
    async with session.get(url, auth=auth) as resp:
        html_page = await resp.text()
    return html_page


async def fetch_bytes(
    url: str,
    session: aiohttp.ClientSession,
    auth: Optional[aiohttp.BasicAuth] = None,
) -> bytes:
    logging.debug(f"Downloading {url}")
    async with session.get(url, auth=auth) as resp:
        data = await resp.read()
    return data


async def fetch_first_img(
    url: str,
    session: aiohttp.ClientSession,
    auth: Optional[aiohttp.BasicAuth] = None,
) -> bytes:
    logging.debug(f"Visitng {url}")
    async with session.get(url, auth=auth) as resp:
        html_page = await resp.text()
    parser = BeautifulSoup(html_page, "html.parser")
    img_tag = parser.find("img")
    assert "src" in img_tag.attrs
    img_url = urljoin(url, img_tag["src"])
    logging.debug(f"Downloading {img_url}")
    async with session.get(img_url, auth=auth) as resp:
        img_data = await resp.read()
    return img_data
