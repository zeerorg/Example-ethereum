import eth_utils

def init_module(_w3, _contract):
    global w3, contract_instance
    w3 = _w3
    contract_instance = _contract



if __name__ == '__main__':
    from src.cpabe_interact import *

account = w3.eth.accounts[2]

