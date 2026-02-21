"""
Write a program in Python to Create a Merkle Tree in Blockchain 
"""

import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

def merkle_tree(leaves):
    nodes = []    # nodes mean all leave nodes primarily -> hashes of transactions data
    for x in leaves:
        nodes.append(hash_data(x))

    while len(nodes) > 1:
        temp = []

        for i in range(0,len(nodes),2):
            left = nodes[i]
            right = ""
            if i+1 < len(nodes):
                right = nodes[i+1]
            else:
                right = left
            temp.append(hash_data(left + right))

        nodes = temp

    return nodes[0]


transactions = ["A->B","B->C","C->D","D->E","E->F"]

root = merkle_tree(transactions)

print("Transactions:", transactions)
print("Merkle Root:", root)
