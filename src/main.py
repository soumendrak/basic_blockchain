"""
Process flow of the Blockchain
Author: Soumendra Kumar Sahoo
Date: 30 sep 2017
"""
from block import create_genesis_block, next_block


def main():
    # Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # How many blocks should we add to the chain
    # after the genesis block
    num_of_blocks_to_add = 10

    # Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Tell everyone about it!
        print("Block #{} has been added to the blockchain!".format(
            block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))

if __name__ == '__main__':
    main()