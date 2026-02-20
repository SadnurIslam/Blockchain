import hashlib
import time

class Block:
    def calculate_hash(self):
        value = str(self.index)+str(self.timestamp)+str(self.data)+str(self.prev_hash)
        return hashlib.sha256(value.encode()).hexdigest()
    
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()
        
    
    
    
blockchain = []

blockchain.append(Block(0,"abc","0"))
blockchain.append(Block(1,"bcd",blockchain[-1].hash))

for block in blockchain:
    print("Index: ",block.index)
    print("Data: ", block.data)
    print("previous hash: ", block.prev_hash)
    print("Hash: ", block.hash)
    print("-"*50)