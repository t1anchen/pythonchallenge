import re
import requests
from nose.tools import nottest
import pc.level_00
import pc.level_01
import pc.level_12
import pc.level_13

def_template = 'http://www.pythonchallenge.com/pc/def/{0}.html'
pc_return_tmpl = 'http://www.pythonchallenge.com/pc/return/{0}'

def test_level_00():
    template = def_template
    try:
        r = requests.get(template.format(pc.level_00.solution()))
    except:
        raise

    next_entry = [re.sub(r'(.*)URL=(.*)\.html\"\>', r'\2', line.decode()) # Python3 `line' would be bytestring
                  for line in r.iter_lines() if re.match(r'.*URL.*', line.decode())]
    actual = next_entry[0]
    expected = 'map'
    assert actual == expected

def test_level_01():
    template = def_template
    test_data = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. ''' + \
                '''rfyrq ufyr amknsrcpq ypc dmp. ''' + \
                '''bmgle gr gl zw fylb gq glcddgagclr ylb ''' + \
                '''rfyr'q ufw rfgq rcvr gq qm jmle. ''' + \
                '''sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. ''' + \
                '''lmu ynnjw ml rfc spj.'''
    actual = pc.level_01.decrypt(test_data)
    expected = '''i hope you didnt translate it by hand. ''' + \
        '''thats what computers are for. ''' + \
        '''doing it in by hand is inefficient and ''' + \
        '''that's why this text is so long. ''' + \
        '''using string.maketrans() is recommended. ''' + \
        '''now apply on the url.'''
    assert expected == actual
    actual = pc.level_01.solution()
    expected = 'ocr'
    assert expected == actual

def test_level_12():
    actual = pc.level_12.solution()
    expected = 'disproportional'
    assert expected == actual
    pc.level_12.clean()

def test_level_13():
    actual = pc.level_13.solution()
    expected = 'ITALY'
    assert expected == actual
