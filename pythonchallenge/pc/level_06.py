import asyncio
import logging
import re
import zipfile
from io import BytesIO

import aiohttp

from .utils import def_page_template, def_template


async def get_hint():
    async with aiohttp.ClientSession() as session:
        url = def_page_template.format("channel")
        logging.debug(f"Visiting {url}")
        async with session.get(url) as resp:
            html_page = await resp.text("utf_8")
        hint = "".join(re.findall(r"<!-- <-- (.+) -->", html_page))
        logging.debug(f"{hint=}")
        return hint


async def fetch_from_remote():
    hint = await get_hint()
    async with aiohttp.ClientSession() as session:
        url = def_template.format(".".join(["channel", hint]))
        logging.debug(f"Visiting {url}")
        async with session.get(url) as resp:
            zip_file_data = await resp.read()
        return zip_file_data


def solution(data: bytes):
    if data is None:
        data = asyncio.run(fetch_from_remote())
    zip_file = zipfile.ZipFile(BytesIO(data))
    n_member = 0
    member_stat = {}
    for fi in zip_file.filelist:
        member_stat[fi.filename] = 0
        # logging.debug(f"{fi=}")
        n_member += 1
    logging.debug(f"{n_member=}")
    with zip_file.open("readme.txt") as stream:
        logging.debug(stream.read().decode())

    comments_from_zip = []

    member = "90052.txt"  # start member
    n_jump = 0
    while True:
        logging.debug(f"{n_jump=} Reading {member}")
        zip_info = zip_file.getinfo(member)
        member_stat[member] += 1
        with zip_file.open(member) as member_stream:
            next_number = "".join(re.findall(r"\d+$", member_stream.read().decode()))
        comments_from_zip.append(zip_info.comment)
        if next_number:
            member = f"{next_number}.txt"
            n_jump += 1
        else:
            break

    # [2024-11-07T23:22:49+08:00] from member_stat, it reveals that every files
    # in the package except readme.txt will be visited.

    total_comments = (b"".join(comments_from_zip)).decode().split("\n")
    for line in total_comments:
        logging.debug(line)

    return total_comments  # hockey

    # [2024-11-07T23:44:45+08:00] Aftre visiting
    # http://www.pythonchallenge.com/pc/def/hockey.html, it prompts "it's in the
    # air. look at the letters. ". Go back the comments, it founds the ascii art
    # diagrams consist of "oxygen" letters.

    # final jump to http://www.pythonchallenge.com/pc/def/oxygen.html
