"""
Create basic block of blockchain concept
Author: Soumendra Kumar Sahoo
Date: 30 sep 2017
"""
import datetime as dt
import hashlib

from internal_rules import proof_of_work


class Block:
    """Represent one unit block"""
    def __init__(self, index, timestamp, data, prev_hash, proof):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.proof = proof
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        hash_string = str(self.index) + str(self.timestamp) + \
            str(self.data) + str(self.prev_hash)
        sha.update(hash_string)
        return sha.hexdigest()


def create_genesis_block():
    return Block(0, dt.datetime.now(), 'genesis block', '0', proof=1)


def next_block(last_block):
    current_index = last_block.index + 1
    current_timestamp = dt.datetime.now()
    current_data = "Hey! I'm block " + str(current_index)
    current_hash = last_block.hash
    current_proof = proof_of_work(last_block.proof)
    return Block(current_index, current_timestamp,
                 current_data, current_hash, current_proof)
