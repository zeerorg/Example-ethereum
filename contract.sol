pragma solidity ^0.4.18;

contract CPABE {
    /**
     * The encrypted document stored with id
     *
     
    struct Document {
        bytes data;
        address owner;
    }
    

    mapping (bytes32 => Document) public documents;
    
    */

    bytes document;
    /**
     *   mapping of document id to public address and encrypted key
     *   The requester queries this to get his assigned key.
     */
    /* mapping (bytes32 => mapping (address => bytes)) public access; */
    bytes access;

    function CPABE() public {}

    /**
     * This call is made to get the encrypted document from blockchain
     */
    function getDocument(bytes32 docId) view public returns (bytes) {
        // return documents[docId].data;
        return document;
    }

    /**
     * This call is made to retrieve the attribute key,
     * which has been encrypted by the public key of requester.
     */
    function getEncKey(bytes32 docId) view public returns (bytes) {
        // return access[docId][msg.sender];
        return access;
    }

    /**
     * This call will give access to requester
     */
    function giveAccess(bytes32 docId, address requester, bytes encKey) public {
        // Can implement signature checking
        // require(documents[docId].owner == msg.sender);  // check if call was made by owner himself
         // access[docId][requester] = encKey;
         access = encKey;
    }

    /**
     * Upload a new document
     */
    function newDocument(bytes32 docId, bytes encDoc) public {
        /*
        documents[docId].owner = msg.sender;
        documents[docId].data = encDoc;
        listDoc.push(docId)
        */
        document = encDoc;
    }

}
