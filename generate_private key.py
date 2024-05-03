import os
import hashlib
import base58

# Constants for the secp256k1 curve
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
a = 0
b = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# Define the generator point G
G = (Gx, Gy)

def generate_private_key():
    # Generate 32 random bytes (256 bits)
    random_bytes = os.urandom(32)
    # Convert bytes to integer
    private_key = int.from_bytes(random_bytes, byteorder="big")
    return private_key

def point_addition(P, Q):
    if P == "O":
        return Q
    if Q == "O":
        return P
    x1, y1 = P
    x2, y2 = Q
    if P != Q:
        s = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    else:
        s = ((3 * x1 * x1 + a) * pow(2 * y1, -1, p)) % p
    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return (x3, y3)

def point_double(P):
    return point_addition(P, P)

def point_scalar_multiplication(k, P):
    result = "O"
    while k > 0:
        if k & 1:
            result = point_addition(result, P)
        P = point_double(P)
        k >>= 1
    return result

def compress_point(P):
    x, y = P
    return (x, y % 2)

def derive_public_key(private_key):
    # Derive the public key
    public_key_point = point_scalar_multiplication(private_key, G)
    public_key_compressed = compress_point(public_key_point)
    return public_key_compressed

def encode_wif_private_key(private_key):
    # Encode the private key in Wallet Import Format (WIF)
    prefix = b"\x80"
    private_key_bytes = private_key.to_bytes(32, byteorder="big")
    suffix = b"\x01"  # Indicates compressed format
    wif_private_key_bytes = prefix + private_key_bytes + suffix
    checksum = hashlib.sha256(hashlib.sha256(wif_private_key_bytes).digest()).digest()[:4]
    wif_private_key = base58.b58encode(wif_private_key_bytes + checksum)
    return wif_private_key.decode("utf-8")

def encode_public_key(public_key):
    # Encode the public key in Base58Check encoding
    prefix = b"\x00"
    public_key_bytes = public_key[0].to_bytes(32, byteorder="big")
    public_key_bytes_compressed = bytes([2 + (public_key[1] % 2)]) + public_key_bytes
    checksum = hashlib.sha256(hashlib.sha256(prefix + public_key_bytes_compressed).digest()).digest()[:4]
    encoded_public_key = base58.b58encode(prefix + public_key_bytes_compressed + checksum)
    return encoded_public_key.decode("utf-8")

# Generate a private key
private_key = generate_private_key()
print("Private Key:", private_key)

# Derive the corresponding public key
public_key = derive_public_key(private_key)
print("Public Key (Compressed):", public_key)

# Encode the private key in Wallet Import Format (WIF)
wif_private_key = encode_wif_private_key(private_key)
print("WIF Private Key:", wif_private_key)

# Encode the public key in Base58Check encoding
encoded_public_key = encode_public_key(public_key)
print("Encoded Public Key:", encoded_public_key)
