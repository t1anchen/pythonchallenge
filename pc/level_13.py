'''Level 13: disproportional
'''

import re
import xmlrpc.client # Python3, use xmlrpclib if python2

def solution():
    '''1. Inspect page, found location (326, 177, 45) is actually the 5 button
    2. Click that button, it jumps to a php page with XML RPC service
    3. In [xx]: client.system.listMethods()
       Out[xx]:
       ['phone',
        'system.listMethods',
        'system.methodHelp',
        'system.methodSignature',
        'system.multicall',
        'system.getCapabilities']
    4. In [xx]: client.system.methodHelp('phone')
       Out[xx]: 'Returns the phone of a person'
    5. In [xx]: client.system.methodSignature('phone')
       Out[xx]: [['string', 'string']]      # accept a string and return a string
    5. http://www.pythonchallenge.com/pc/return/evil4.jpg -> Bert
    '''
    client = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    res = client.phone('Bert')
    alphabet_seq = re.findall(r'[^\d\W]+', res) # remove numbers and punctuations
    return alphabet_seq[0] if len(alphabet_seq) > 0 else ''
