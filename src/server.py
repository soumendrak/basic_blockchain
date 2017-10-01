"""
Blockchain server to keep track of the transactions
Author: Soumendra Kumar Sahoo
Date: 30 sep 2017
"""
from flask import Flask, request
import datetime as dt
import json
import main
import pdb

from block import Block
from config_reader import hostname, port
from internal_rules import proof_of_work


node = Flask(__name__)
# Store the transactions which
# this node has in a list
this_nodes_transactions = []
miner_address = 'ABubabuy21628bsabubyol1267'


@node.route('/txn', methods=['POST', 'OPTIONS'])
def transaction():
    # On each new POST request,
    # we extract the transaction data
    new_txn = request.get_json()
    # Then we add the transaction to our list
    this_nodes_transactions.append(new_txn)
    # Because the transaction was successfully
    # submitted, we log it to our console
    print "New transaction"
    print "FROM: {}".format(new_txn['from'])
    print "TO: {}".format(new_txn['to'])
    print "AMOUNT: {}\n".format(new_txn['amount'])
    # Then we let the client know it worked out
    return "Transaction submission successful\n"


@node.route('/mine', methods=['GET'])
def mine():
    blockchain = main.retrieve_blockchain()
    # Get the last proof of work
    last_block = blockchain[-1]
    # pdb.set_trace()
    # last_proof = last_block.data['proof-of-work']
    last_proof = last_block.proof
    # Find the proof of work for
    # the current block being mined
    # Note: The program will hang here until a new
    #       proof of work is found
    proof = proof_of_work(last_proof)
    # Once we find a valid proof of work,
    # we know we can mine a block so
    # we reward the miner by adding a transaction
    this_nodes_transactions.append(
        {"from": "network", "to": miner_address, "amount": 1}
    )
    # Now we can gather the data needed
    # to create the new block
    new_block_data = {
        # "proof-of-work": proof,
        "transactions": list(this_nodes_transactions)
    }
    new_block_index = last_block.index + 1
    # new_block_timestamp = this_timestamp = dt.datetime.now()
    new_block_timestamp = dt.datetime.now()
    last_block_hash = last_block.hash
    # Empty transaction list
    this_nodes_transactions[:] = []
    # Now create the
    # new block!
    mined_block = Block(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash,
        proof
    )
    blockchain.append(mined_block)
    # Let the client know we mined a block
    return json.dumps({
        "index": new_block_index,
        "timestamp": str(new_block_timestamp),
        "data": new_block_data,
        "hash": last_block_hash
    }) + "\n"


if __name__ == '__main__':
    node.run(host=hostname, port=int(port), debug=True)
