# detects if the blockchain/hash values have been tampered with by recomputing the hash of each block and comparing it to the stored hash. It also checks that each block's previous_hash matches the hash of the previous block, ensuring the integrity of the chain.

def is_chain_valid(chain):

    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i-1]

        # recompute hash
        if current.hash != current.calculate_hash():
            return False

        # check chain link
        if current.previous_hash != previous.hash:
            return False

    return True


print("Valid Blockchain?" , is_chain_valid(bc.chain))