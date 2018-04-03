# Python ethereum contract tutorial

### To run this, requirements:

1. python 3.6. Install from : [Python](https://www.python.org/downloads/)
2. Then do: `pip install pipenv`
3. clone this repository and `cd` into it.
4. execute: `pipenv install`. This will install all python dependencies required to run tutorial.

We need a test ethereum chain to communicate to it.
You can use [Ganache](http://truffleframework.com/ganache/). It is a nice GUI tool to create and monitor a test ethereum chain.

1. After starting test chain, execute: `pipenv run python`
2. Type `from src.contract_int import *`.

You might get a lot of warnings, ignore them for now.

Warning like : 
```
/home/rishabh/.local/share/virtualenvs/eth_pyth-ZMQ0Mj2Y/lib/python3.6/site-packages/eth_utils/string.py:23: DeprecationWarning: The `force_obj_to_text` function has been deprecated and will be removed in a subsequent release of the eth-utils library. UTF8 cannot encode some byte values in the 0-255 range which makes naive coersion between bytes and text representations impossible without explicitly declared encodings.
  "declared encodings.".format(fn.__name__
```
Can be ignored.

If you get `connected` in the end that means the program executed successfully.

Open `ganache` to see that the contract has been deployed.

### compiling contract to json
Three things are needed : abi definition, byte representation, opcode representation
1. install `solc` from [download solc](http://solidity.readthedocs.io/en/v0.4.21/installing-solidity.html)
2. run: `solc --combined-json abi,bin,opcodes contract.sol > compiled_contract.json`
3. To see json output more clearly do : `python -m json.tool compiled_contract.json`

## Tips:
1. Decrease the cost of gas to lower value (maybe 20) in ganache.

## New web3 (4.0.0) api
The web3 python api was recently updated to match the web3 json api, this broke some things in the current project.
1. Replace use of `eth_utils.force_obj_To_bytes` with `web3.utils.to_bytes` which takes positional argument `text` to convert text to bytes.
2. `w3.eth.contract` now takes arguments with name i.e. to supply abi and address we do `w3.eth.contract(abi=som_abi, address=transaction_address, ContractFactoryClass=ContractClass)`

## Install cpabe
1. Download cpabe, libbswabe from [cpabe](http://acsc.cs.utexas.edu/cpabe/index.html)
2. Download pbc from [pbc](https://crypto.stanford.edu/pbc/)
3. Add `export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/lib` and `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib` to your .bashrc and reload shell.
3. First build pbc by doing `./configure; make; sudo make install`
4. THen build libbswabe by doing `./configure -with-pbc-include=$HOME/pbc-0.5.14/include/ -with-pbc-lib=/usr/local/lib/`, `make LDFLAGS="-lgmp -lcrypto -L/usr/lib/x86_64-linux-gnu -lglib-2.0 -lbswabe -lgmp -lpbc"` and `sudo make install`
5. Then build cpabe by doing `./configure -with-pbc-include=$HOME/pbc-0.5.14/include/ -with-pbc-lib=/usr/local/lib/`, `make LDFLAGS="-lgmp -lcrypto -L/usr/lib/x86_64-linux-gnu -lglib-2.0 -lbswabe -lgmp -lpbc"` and `sudo make install`.
6. If you get errors while compiling cpabe there might be semicolon missing in one of the files (yeah idk..)
7. Ignore any warnings.
8. Run: `cpabe-setup` to confirm that it is working.
