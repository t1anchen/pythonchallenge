import asyncio
import logging
import xmlrpc.client
from typing import Optional
from xmlrpc import client

import aiohttp

from .utils import fetch_first_link_in_area, pc_return_page_tmpl


async def fetch_from_remote():
    url = pc_return_page_tmpl.format("disproportional")
    async with aiohttp.ClientSession() as session:
        auth = aiohttp.BasicAuth("huge", "file")
        endpoint = await fetch_first_link_in_area(url, session, auth)
        return endpoint


# [2024-11-09T23:55:41+08:00] From code of xmlrpc/client.py, it is found that
# accept_gzip_encoding is hard coded in Transport.

#   class Trasport:
#   ...
#       accept_gzip_encoding = True
#   ...
#       if self.accept_gzip_encoding and gzip:
#           connection.putrequest("POST", handler, skip_accept_encoding=True)
#           headers.append(("Accept-Encoding", "gzip"))
#   ...

# Thus, neither overriding `request` method nor modifying `headers` can affect
# the behaviour. The reason why it is hardcoded is unknown, but the issue can be
# mitigated by inheriting Transport class and set `accept_gzip_encoding` to
# False

# [2024-11-10T00:01:55+08:00] By the way, DO NOT TRUST ANY AI-GENERATED CODE.
# THE EFFECTIVENESS OF CODE MUST BE VERIFIED BEFORE TAKING INTO REALWORLD USAGE.

# [2024-11-10T00:03:19+08:00] Scientific method, debugger and reading/testing
# code is your friend rather than a stupid AI collecting any unverified
# information (which means bias, error and misinformation) from the world.

# [2024-11-10T00:30:46+08:00] It is required to override Transport class,
# otherwise the default behaviour of xmlrpc.client enforces connection with
# gzipped and throws "Not a gzipped file. b(\n\n)" error. Perplexity.AI provided
# incorrect answer with false/outdated information that took me 2 hours to
# debugging, investigating and correcting the misinformation.


class NoGzipTransport(xmlrpc.client.Transport):
    accept_gzip_encoding = False


def solution(endpoint: Optional[str]):
    if endpoint is None:
        endpoint = asyncio.run(fetch_from_remote())
    logging.debug(f"{endpoint=}")
    proxy = client.ServerProxy(endpoint, transport=NoGzipTransport())
    available_methods: list[str] = proxy.system.listMethods()
    logging.debug(f"{available_methods=}")
    invokable_method_name = next(
        (
            method_name
            for method_name in available_methods
            if not method_name.startswith("system")
        ),
        "",
    )  # phone
    assert invokable_method_name
    logging.debug(proxy.system.methodHelp(invokable_method_name))
    # Returns the phone of a person
    logging.debug(proxy.system.methodSignature(invokable_method_name))
    # [['string', 'string']]

    # [2024-11-10T00:21:50+08:00] Considering the method argment should be a
    # person (name), and the person might be related in the previous level
    # (Level 12)
    resp = proxy.phone("Bert")
    logging.debug(f"{resp=}")
    # 555-ITALY
    return "italy"


# def solution():
#     """1. Inspect page, found location (326, 177, 45) is actually the 5 button
#     2. Click that button, it jumps to a php page with XML RPC service
#     3. In [xx]: client.system.listMethods()
#        Out[xx]:
#        ['phone',
#         'system.listMethods',
#         'system.methodHelp',
#         'system.methodSignature',
#         'system.multicall',
#         'system.getCapabilities']
#     4. In [xx]: client.system.methodHelp('phone')
#        Out[xx]: 'Returns the phone of a person'
#     5. In [xx]: client.system.methodSignature('phone')
#        Out[xx]: [['string', 'string']]      # accept a string and return a string
#     5. http://www.pythonchallenge.com/pc/return/evil4.jpg -> Bert
#     """
#     client = xmlrpc.client.ServerProxy(
#         "http://www.pythonchallenge.com/pc/phonebook.php"
#     )
#     res = client.phone("Bert")
#     alphabet_seq = re.findall(r"[^\d\W]+", res)  # remove numbers and punctuations
#     return alphabet_seq[0] if len(alphabet_seq) > 0 else ""
