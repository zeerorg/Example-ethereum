# Python ethereum contract tutorial

### To run this, requirements:

1. python 3.6. Install from : [Python](https://www.python.org/downloads/)
2. Then do: `pip install pipenv`
3. clone this repository and `cd` into it.
4. execute: `pipenv install`. This will install all python dependencies required to run tutorial.

We need a test ethereum chain to communicate to it.
You can use [Ganache](http://truffleframework.com/ganache/). It is a nice GUI tool to create and monitor a test ethereum chain.

1. After starting test chain, execute: `pipenv run python`
2. Type `from deploy_contract import *`, in the shell.

You might get a lot of warnings, ignore them for now.

Warning like : 
```
/home/rishabh/.local/share/virtualenvs/eth_pyth-ZMQ0Mj2Y/lib/python3.6/site-packages/eth_utils/string.py:23: DeprecationWarning: The `force_obj_to_text` function has been deprecated and will be removed in a subsequent release of the eth-utils library. UTF8 cannot encode some byte values in the 0-255 range which makes naive coersion between bytes and text representations impossible without explicitly declared encodings.
  "declared encodings.".format(fn.__name__
```
Can be ignored.

If you get `1` in the end that means program executed successfully.

Now to cast a vote type: `vote_for_candidate()`. This will cast a vote for "Rama". Available candidates are: "Nick, "Rama", "John"

To get the votes type: `get_votes()`. This will print the number of votes for "Rama".

Open `ganache` to see the number of transactions which have occurred.
