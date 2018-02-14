import warnings

from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider("http://localhost:7545"))
w3.isConnected()


# Contract source code
def main():
    global contract_instance, w3
    import eth_utils

    from solc import compile_source
    from web3.contract import ConciseContract

    contract_source_code = '''
    pragma solidity ^0.4.18;
    // We have to specify what version of compiler this code will compile with
    
    contract Voting {
      /**
      * A map of candidate names to integer values
      */
      mapping (bytes32 => uint8) public votesReceived;
    
      /**
            List of candidates. bytes32 array is used since ethereum doesn't support strings
       */
      bytes32[] public candidateList;
    
      /* Constructor called when we deploy app to blockchain
      we will pass an array of candidates who will be contesting in the election
      */
      function Voting(bytes32[] candidateNames) public {
        candidateList = candidateNames;
      }
    
      // This function returns the total votes a candidate has received so far
      function totalVotesFor(bytes32 candidate) view public returns (uint8) {
        require(validCandidate(candidate));
        return votesReceived[keccak256(candidate)];
      }
    
      // This function increments the vote count for the specified candidate. This
      // is equivalent to casting a vote
      function voteForCandidate(bytes32 candidate) public {
        require(validCandidate(candidate));
        votesReceived[keccak256(candidate)] += 1;
      }
    
      // checks if a candidate is valid or not
      function validCandidate(bytes32 candidate) view public returns (bool) {
        for (uint i = 0; i < candidateList.length; i++) {
          if (candidateList[i] == candidate) {
            return true;
          }
        }
        return false;
      }
    }
    '''

    compiled_sol = compile_source(contract_source_code)
    contract_interface = compiled_sol['<stdin>:Voting']

    # create contract for deployment
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

    # deploy contract
    tx_hash = contract.deploy(
        transaction={'from': w3.eth.accounts[0], 'gas': 410000},
        args=[eth_utils.force_obj_to_bytes(["Rama", "Nick", "John"])]
    )

    # Get deployment receipt and get contract address from it
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    contract_address = tx_receipt['contractAddress']

    # get main contract instance
    contract_instance = w3.eth.contract(contract_interface['abi'], contract_address, ContractFactoryClass=ConciseContract)

    contract_instance.voteForCandidate(eth_utils.force_obj_to_bytes("Rama"), transact={'from': w3.eth.accounts[0]})

    print(contract_instance.totalVotesFor(eth_utils.force_obj_to_bytes("Rama")))


def vote_for_candidate(candidate="Rama", from_acc=w3.eth.accounts[0]):
    import eth_utils
    return contract_instance.voteForCandidate(eth_utils.force_obj_to_bytes(candidate), transact={'from': from_acc})


def get_votes(candidate="Rama"):
    import eth_utils
    return contract_instance.totalVotesFor(eth_utils.force_obj_to_bytes(candidate))


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    main()
