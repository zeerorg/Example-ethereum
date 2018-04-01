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