import requests
from itertools import cycle
import os

def solution():
    # evil.html -> evil1.jpg -> 5 decks
    # evil2.jpg -> not jpg - -.gfx
    # evil3.jpg -> no more evils
    url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
    auth_ctx = ('huge', 'file')
    res = requests.get(url, auth=auth_ctx)
    # https://www.cs.duke.edu/courses/cps124/fall01/code/gfx_reader/docs/gfx_format.html
    gfx_stream = res.iter_content()
    decks = [[] for i in range(5)]
    i = cycle(range(5))
    for gfx_byte in gfx_stream:
        decks[next(i)].append(gfx_byte) # dispatch card to 5 decks
    for i in range(5):
        with open('img{0:02d}.gfx'.format(i), 'wb') as f:
            f.write(b''.join(decks[i])) # Python3 byte string
    # TODO: get font from gfx image
    # img00.gfx -> dis
    # img01.gfx -> pro
    # img02.gfx -> port
    # img03.gfx -> ional
    # img04.gfx -> i̶t̶y̶ (abandoned, strikethrough combining U+0336)

    return 'disproportional'

def clean():
    filenames = ['img{0:02d}.gfx'.format(i) for i in range(5)]
    for fn in filenames:
        os.remove(fn)
