from pc.level_04 import solution
import pytest
import time
import logging


def test_integration():
    tick_start = time.perf_counter()
    actual = solution()
    tick_end = time.perf_counter()
    logging.debug(f"aiohttp elapsed: {tick_end - tick_start} secs")
    # aiohttp elapsed: 60.11620320001384 secs
    expected = "peak"
    assert expected == actual


@pytest.mark.skip
def test_integration2():
    """Using built-in urllib to perform http request"""
    from urllib.request import urlopen
    from urllib.parse import urlencode
    import logging
    import re
    from collections import deque

    tick_start = time.perf_counter()
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    n = "12345"
    n_jump = 0
    while n.isdigit():
        params = {"nothing": n}
        with urlopen(url + "?" + urlencode(params)) as resp:
            resp_text = resp.read().decode()
        numbers = re.findall(r"\d+", resp_text)
        if "Divide" in resp_text or "divide" in resp_text:
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
    tick_end = time.perf_counter()
    logging.debug(f"urllib elapsed: {tick_end - tick_start} secs")
    #  urllib elapsed: 144.08658619999187 secs
    assert n == "peak"
