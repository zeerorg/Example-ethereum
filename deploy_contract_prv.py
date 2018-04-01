import warnings

from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider("http://localhost:7545"))
w3.isConnected()

candidates = ["Rama", "Nick", "John"]

# Contract source code
def main():
    global contract_instance, w3
    import eth_utils
    from web3.contract import ConciseContract
    import json

    with open('compiled_contract.json') as f:
        compiled_sol = json.load(f)["contracts"]["contract.sol:Voting"]

    abi = json.loads(compiled_sol["abi"])

    # create contract for deployment
    contract = w3.eth.contract(abi=abi, bytecode=compiled_sol['bin'])

    # deploy contract
    tx_hash = contract.deploy(
        transaction={'from': w3.eth.accounts[0], 'gas': 410000},
        args=[eth_utils.force_obj_to_bytes(candidates)]
    )

    # Get deployment receipt and get contract address from it
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    contract_address = tx_receipt['contractAddress']

    # get main contract instance
    contract_instance = w3.eth.contract(abi, contract_address, ContractFactoryClass=ConciseContract)

    contract_instance.voteForCandidate(eth_utils.force_obj_to_bytes("Rama"), transact={'from': w3.eth.accounts[0]})

    print(contract_instance.totalVotesFor(eth_utils.force_obj_to_bytes("Rama")))


def vote_for_candidate(candidate="Rama", from_acc=w3.eth.accounts[0]):
    import eth_utils
    return contract_instance.voteForCandidate(eth_utils.force_obj_to_bytes(candidate), transact={'from': from_acc})


def get_votes(candidate="Rama"):
    import eth_utils
    return contract_instance.totalVotesFor(eth_utils.force_obj_to_bytes(candidate))

def get_all_votes():
    import eth_utils
    return {key: value for (key, value) in map(lambda candidate: (candidate, get_votes(candidate)), candidates)}


main()
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     main()
