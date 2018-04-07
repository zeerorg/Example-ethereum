import warnings

from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider("http://localhost:7545"))
if w3.isConnected():
    print("Connected")
else:
    print("Not connected")

def create_contract():
    global contract_instance, w3
    import eth_utils
    from web3.contract import ConciseContract
    import json

    with open('compiled_contract.json') as f:
        compiled_sol = json.load(f)["contracts"]["contract.sol:CPABE"]

    abi = json.loads(compiled_sol["abi"])

    # create contract for deployment
    contract = w3.eth.contract(abi=abi, bytecode=compiled_sol['bin'])

    # deploy contract
    tx_hash = contract.deploy(
        transaction={'from': w3.eth.accounts[0], 'gas': 41000000}
    )

    # Get deployment receipt and get contract address from it
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    contract_address = tx_receipt['contractAddress']

    print(contract_address)

    # get main contract instance
    contract_instance = w3.eth.contract(abi=abi, address=contract_address, ContractFactoryClass=ConciseContract)

def connect_contract(address):
    global contract_instance, w3
    import eth_utils
    from web3.contract import ConciseContract
    import json

    with open('compiled_contract.json') as f:
        compiled_sol = json.load(f)["contracts"]["contract.sol:CPABE"]

    abi = json.loads(compiled_sol["abi"])

    contract_instance = w3.eth.contract(abi=abi, address=address, ContractFactoryClass=ConciseContract)
