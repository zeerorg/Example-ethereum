from web3 import utils
from Crypto.PublicKey import RSA
from src import cpabe
import random
my_docs = {}

def init_module(_w3, _contract):
    global w3, contract_instance, account
    w3 = _w3
    contract_instance = _contract
    account = w3.eth.accounts[1]

'''
functionality required : 
1. Encrypt and Upload document to ethereum blockchain
2. Download the encrypted document
3. Download any requested attribute key
4. Take a requester public key and attributes,
     and upload their attribute key to blockchain after encrypting it with their public key
'''

def uploadDoc():
    document = './share.txt'
    cpabe.gen_pair()
    cpabe.encrypt_report(document)

    with open('{}.cpabe'.format(document), 'rb') as f:
        encDoc = f.read()

    docId = '00'+str(random.randint(0, 9))
    contract_instance.newDocument(utils.encoding.to_bytes(text=docId),\
                                    encDoc, transact={'from': account})
    my_docs[docId] = encDoc


def download_doc(docId):
    downloaded = contract_instance.getDocument(utils.encoding.to_bytes(text=docId), transact={'from': account})
    # save the doc
    with open("./{}.cpabe".format(docId), 'wb') as f:
        f.write(downloaded)

    # decrypt the doc
    cpabe.dec_file(name, docId)
    pass


def download_key(docId):
    encKey = contract_instance.getEncKey(utils.encoding.to_bytes(text=docId), transact={'from': account})
    attr_key = key.decrypt(encKey)

    with open("./key/{}_priv_key", 'w') as f:
        f.write(attr_key)
    pass

# requester_address should be web3 account address
def give_access(docId, requester_address, requester_pubkey, requester_name):
    # generate attribute key
    cpabe.gen_priv_key(name)

    # encrypt attribute key
    with open("./key/{}_priv_key".format(name)) as f:
        key_to_put = f.read()

    encKey = RSA.importKey(requester_pubkey).encrypt(key_to_put)[0]

    # put attribute key to blockchain
    contract_instance.giveAccess(utils.encoding.to_bytes(text=docId),\
                                 requester_address,\
                                 utils.encoding.to_bytes(text=encKey),
                                 transact={'from': account})
    pass


if __name__ == '__main__':
    from src.cpabe_interact import *

name = "rish"
key = RSA.generate(2048)
