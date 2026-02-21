"""
Write a program in Python to implement PoW algorithm. 
"""


"""
Write a program in Python for mining a new block in a blockchain, and print the values of the
new block.
"""


import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.mine_block(4)

    def calculate_hash(self):
        text = str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)+str(self.nonce)
        return hashlib.sha256(text.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = "0" * difficulty
        while True:
            hash_val = self.calculate_hash()
            if hash_val.startswith(prefix):
                return hash_val
            self.nonce += 1


# -------- Mining New Block --------
genesis = Block(0, "Genesis Block", "0")

mined_block = Block(1, "Transaction Data", genesis.hash)

print("New Block Mined Successfully!\n")
print("Data:", mined_block.data)
print("Nonce:", mined_block.nonce)
print("Hash:", mined_block.hash)
