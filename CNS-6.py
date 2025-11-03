import random
from math import gcd

# Function to check prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a random prime number
def generate_prime(start=100, end=500):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

# Function to find modular inverse of e mod phi
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# RSA Implementation
def rsa_demo():
    print("=== RSA Key Generation ===")

    # Step 1: Generate two prime numbers
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()
    print(f"Prime numbers: p = {p}, q = {q}")

    # Step 2: Compute modulus
    n = p * q
    print(f"Modulus (n) = {n}")

    # Step 3: Compute phi(n)
    phi = (p - 1) * (q - 1)
    print(f"Totient (phi) = {phi}")

    # Step 4: Choose e (public exponent)
    e = 65537  # Common choice
    if gcd(e, phi) != 1:  # if not coprime, choose another
        e = 3
    print(f"Public exponent (e) = {e}")

    # Step 5: Compute d (private exponent)
    d = mod_inverse(e, phi)
    print(f"Private exponent (d) = {d}")

    # Keys
    public_key = (n, e)
    private_key = (n, d)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Step 6: Encryption
    message = int(input("\nEnter a number message (m < n): "))
    ciphertext = pow(message, e, n)
    print(f"Encrypted Message: {ciphertext}")

    # Step 7: Decryption
    decrypted = pow(ciphertext, d, n)
    print(f"Decrypted Message: {decrypted}")

# Run the demo
rsa_demo()
