# Data Integrity Example using Hashing

import hashlib

original_data = "Hello Blockchain"
stored_hash = hashlib.sha256(original_data.encode()).hexdigest()

# later verification
new_data = input("Enter data to verify: ")
new_hash = hashlib.sha256(new_data.encode()).hexdigest()

if new_hash == stored_hash:
    print("Data is authentic ✅")
else:
    print("Data is tampered ❌")