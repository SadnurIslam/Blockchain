"""
Write a Program in Python to Verify Hash Properties
"""

"""
Properties of hash functions:
1. Deterministic: The same input will always produce the same hash output.
2. Fixed Output Length: Hash functions produce a hash of fixed length, regardless of the input size.
3. Pre-image Resistance: It should be computationally infeasible to reverse-engineer the original input from its hash output.
4. Collision Resistance: It should be computationally infeasible to find two different inputs that produce the same hash output.
5. Avalanche Effect: A small change in the input should produce a significantly different hash output.
"""

import hashlib

msg1 = input("Enter first message: ")
msg2 = input("Enter second message: ")

hash1 = hashlib.sha256(msg1.encode()).hexdigest()
hash2 = hashlib.sha256(msg2.encode()).hexdigest()

print("\nHash 1:", hash1)
print("Hash 2:", hash2)

print("\nLength of Hash:", len(hash1))

if hash1 == hash2:
    print("Hashes are equal (rare collision)")
else:
    print("Hashes are different → Small change = Big difference")
