"""
Write a program in Python to Prove Membership and Non-membership in a Merkle Tree
Blockchain
"""


import hashlib

def h(x):
    return hashlib.sha256(x.encode()).hexdigest()

def build_tree(data):
    level = [h(x) for x in data]
    tree = [level]

    while len(level) > 1:
        new = []
        for i in range(0,len(level),2):
            left = level[i]
            right = level[i+1] if i+1 < len(level) else left
            new.append(h(left+right))
        tree.append(new)
        level = new

    return tree

def prove_membership(tree, data):
    member = False
    for leaf in tree[0]:
        if leaf == h(data):
            member = True
            break
        
    if member:
        print(f"{data} is a member of the Merkle Tree.")
    else:
        print(f"{data} is NOT a member of the Merkle Tree.")



# Transactions
tx = ["A","B","C","D"]
tree = build_tree(tx)

root = tree[-1][0]
print("Merkle Root:", root)

# Membership proof for "C"
prove_membership(tree, "C")
# Non-membership proof for "E"
prove_membership(tree, "E")
