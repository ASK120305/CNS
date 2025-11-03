import math

plaintext = input("Enter the plaintext to be encrypted: ").replace(" ", "").upper()

def letter_to_num(c):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(c)

def num_to_letter(n):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[n]

def caesar_cipher_encrypt(a):
    b = letter_to_num(a)
    return num_to_letter((b + 3) % 26)

def caesar_cipher_decrypt(a):
    b = letter_to_num(a)
    return num_to_letter((b - 3) % 26)

# Encryption

pt_list = list(plaintext)
par_encryp_text = [caesar_cipher_encrypt(char) for char in pt_list]

print("After Caesar cipher:", "".join(par_encryp_text))

# Calculate rows and columns for transposition
n_chars = len(par_encryp_text)
n_cols = math.ceil(math.sqrt(n_chars))
n_rows = math.ceil(n_chars / n_cols)

# Create matrix and fill column-wise
matrix = [["" for _ in range(n_cols)] for _ in range(n_rows)]

index = 0
for col in range(n_cols):
    for row in range(n_rows):
        if index < n_chars:
            matrix[row][col] = par_encryp_text[index]
            index += 1
        else:
            matrix[row][col] = ""  # padding

print("\nMatrix:")
for row in matrix:
    print(" ".join(char if char != "" else "_" for char in row))

# Read row-wise to get final encrypted text
final_text = ""
for row in range(n_rows):
    for col in range(n_cols):
        if matrix[row][col] != "":
            final_text += matrix[row][col]

print("\nFinal Encrypted Text:", final_text)

# Decryption

def decrypt(final_text):
    n_chars = len(final_text)
    n_cols = math.ceil(math.sqrt(n_chars))
    n_rows = math.ceil(n_chars / n_cols)

    # Calculate number of full columns
    full_cols = n_chars % n_rows
    if full_cols == 0:
        full_cols = n_cols  # all columns full

    # Number of characters in each column during encryption:
    # columns before full_cols have n_rows chars,
    # others have n_rows - 1 chars (because of padding)
    col_lengths = [n_rows if c < full_cols else n_rows - 1 for c in range(n_cols)]

    # Now reconstruct matrix column-wise using col_lengths
    matrix = [["" for _ in range(n_cols)] for _ in range(n_rows)]
    index = 0
    for col in range(n_cols):
        for row in range(col_lengths[col]):
            if index < n_chars:
                matrix[row][col] = final_text[index]
                index += 1

    # Read row-wise to get Caesar cipher text
    caesar_text = ""
    for row in range(n_rows):
        for col in range(n_cols):
            if matrix[row][col] != "":
                caesar_text += matrix[row][col]

    # Reverse Caesar cipher
    decrypted_text = ""
    for char in caesar_text:
        decrypted_text += caesar_cipher_decrypt(char)

    return decrypted_text

decrypted_text = decrypt(final_text)
print("\nDecrypted Text:", decrypted_text)
