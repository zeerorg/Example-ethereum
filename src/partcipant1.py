import eth_utils

def init_module(_w3, _contract):
    global w3, contract_instance
    w3 = _w3
    contract_instance = _contract

'''
functionality required : 
1. Encrypt and Upload document to ethereum blockchain
2. Download the encrypted document
3. Download any requested attribute key
4. Take a requester public key and attributes,
     and upload their attribute key to blockchain after encrypting it with their public key
'''

if __name__ == '__main__':
    from src.cpabe_interact import *

account = w3.eth.accounts[1]

