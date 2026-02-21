from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

# ---------- KEY GENERATION ----------
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()


# ---------- MESSAGE ----------
message = input("Enter message: ").encode()


# ---------- DIGITAL SIGNATURE (AUTHENTICITY) ----------
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)


# ---------- ENCRYPTION (CONFIDENTIALITY) ----------
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)


print("\nEncrypted Message:", ciphertext)
print("Signature:", signature)


# ---------- RECEIVER SIDE ----------

# Decrypt message
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nDecrypted Message:", decrypted.decode())


# Verify signature
try:
    public_key.verify(
        signature,
        decrypted,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature Valid → Message Authentic ✅")

except:
    print("Signature Invalid → Message Tampered ❌")