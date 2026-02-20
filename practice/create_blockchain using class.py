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
        
    
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        
    def create_genesis_block(self):
        return Block(0,"Genesis block","0")
    
    def add_block(self,data):
        new_block = Block(len(self.chain),data,self.chain[-1].hash)
        self.chain.append(new_block)
    
bc = Blockchain()

bc.add_block("abc")
bc.add_block("bcd")

with open("abc.txt", "w") as file:
    file.write("")
with open("abc.txt", "a") as file:
    for block in bc.chain:
        file.write(f"Index: {block.index}\n")
        file.write(f"Data: {block.data}\n")
        file.write(f"Previous Hash: {block.prev_hash}\n")
        file.write(f"Hash: {block.hash}\n")
        file.write("-"*50 + "\n")