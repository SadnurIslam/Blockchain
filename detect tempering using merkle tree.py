import hashlib

# ---------- Hash Function ----------
def h(data):
    return hashlib.sha256(data.encode()).hexdigest()


# ---------- Build Tree ----------
def build_tree(tx_list):
    tree = []
    level = [h(tx) for tx in tx_list]
    tree.append(level)

    while len(level) > 1:
        new = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i+1] if i+1 < len(level) else left
            new.append(h(left + right))
        tree.append(new)
        level = new

    return tree


# ---------- Generate Proof ----------
def get_proof(tree, index):
    proof = []

    for level in tree[:-1]:
        sibling = index ^ 1
        if sibling < len(level):
            proof.append(level[sibling])
        index //= 2

    return proof


# ---------- Verify Transaction ----------
def verify(tx, proof, root):
    current = h(tx)

    for p in proof:
        current = h(current + p)

    return current == root


# ---------- MAIN ----------
transactions = [
    "A pays B 10",
    "B pays C 5",
    "C pays D 2",
    "D pays E 1"
]

tree = build_tree(transactions)
root = tree[-1][0]

print("Merkle Root:", root)

# choose transaction
target = "C pays D 2"
index = transactions.index(target)

proof = get_proof(tree, index)

print("\nProof hashes:")
for p in proof:
    print(p)

# verify authenticity
print("\nAuthentic Transaction?",
      verify(target, proof, root))


# ---------- Tampering Test ----------
fake = "C pays D 2000"

print("After Tampering:",
      verify(fake, proof, root))