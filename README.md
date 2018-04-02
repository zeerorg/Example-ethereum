# Python ethereum contract tutorial

### To run this, requirements:

1. python 3.6. Install from : [Python](https://www.python.org/downloads/)
2. Then do: `pip install pipenv`
3. clone this repository and `cd` into it.
4. execute: `pipenv install`. This will install all python dependencies required to run tutorial.

We need a test ethereum chain to communicate to it.
You can use [Ganache](http://truffleframework.com/ganache/). It is a nice GUI tool to create and monitor a test ethereum chain.

1. After starting test chain, execute: `pipenv run python`
2. Type `from src.cpabe_interact import *`.

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
