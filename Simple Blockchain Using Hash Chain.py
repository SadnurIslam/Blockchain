"""
Write a Python program to Demonstrate a Simple Implementation of a Blockchain Using Hash
Codes as a Chain of Blocks
"""


import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()


# -------- Create Blocks --------
chain = []

genesis = Block(0, "Genesis Block", "0")
chain.append(genesis)

for i in range(1,5):
    prev = chain[-1]
    block = Block(i, f"Block {i} Data", prev.hash)
    chain.append(block)


# -------- Traverse --------
print("Traversing Blockchain:\n")

for block in chain:
    print("Index:", block.index)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Prev Hash:", block.previous_hash)
    print("Hash:", block.hash)
    
    print("-"*40)
