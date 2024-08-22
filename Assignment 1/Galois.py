import re

# Galois Field multiplication helper function
def gmul(a, b):
    p = 0
    while b:
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x1b
        b >>= 1
    return p & 0xFF  # Ensure result is within 0x00 to 0xFF

# Inverse MixColumns transformation for a single column
def inverse_mix_columns(column):
    c0 = (gmul(column[0], 0x0e) ^ gmul(column[1], 0x0b) ^ gmul(column[2], 0x0d) ^ gmul(column[3], 0x09)) & 0xFF
    c1 = (gmul(column[0], 0x09) ^ gmul(column[1], 0x0e) ^ gmul(column[2], 0x0b) ^ gmul(column[3], 0x0d)) & 0xFF
    c2 = (gmul(column[0], 0x0d) ^ gmul(column[1], 0x09) ^ gmul(column[2], 0x0e) ^ gmul(column[3], 0x0b)) & 0xFF
    c3 = (gmul(column[0], 0x0b) ^ gmul(column[1], 0x0d) ^ gmul(column[2], 0x09) ^ gmul(column[3], 0x0e)) & 0xFF
    return [c0, c1, c2, c3]

# Path to your text file containing the data
text_file_path = '/home/kali/SPM/Ciphertexts'

# Initialize a 2D matrix to store the first four nibbles of the ciphertexts
C = [[None for _ in range(4)] for _ in range(256)]

# Key elements
keys = [0xc7, 0xc1, 0x00, 0x00]  # k1, k2, k3, k4

# Regex pattern to extract hex value and ciphertext
pattern = re.compile(r'Hex Value:\s*([0-9a-fA-F]{2})\s*->\s*Ciphertext:\s*([0-9a-fA-F]+)')

# Read and process the text file
with open(text_file_path, 'r') as file:
    for line in file:
        match = pattern.search(line)
        if match:
            hex_value = int(match.group(1), 16)  # Convert hex value to integer (0 to 255)
            ciphertext = match.group(2)

            # Extract the first four nibbles (8 hex digits)
            C[hex_value][0] = int(ciphertext[0:2], 16)  # First 2 nibbles (1st byte)
            C[hex_value][1] = int(ciphertext[2:4], 16)  # Next 2 nibbles (2nd byte)
            C[hex_value][2] = int(ciphertext[4:6], 16)  # Next 2 nibbles (3rd byte)
            C[hex_value][3] = int(ciphertext[6:8], 16)  # Last 2 nibbles (4th byte)

# XOR each element with the corresponding key and store the result
xor_matrix = [[(C[i][j] ^ keys[j]) & 0xFF for j in range(4)] for i in range(256)]

# Apply the Inverse MixColumns transformation and store the single element result
output_matrix = [None for _ in range(256)]

for i in range(256):
    inv_mixed = inverse_mix_columns(xor_matrix[i])
    # Take the first byte after the Inverse MixColumns as the output
    output_matrix[i] = inv_mixed[0]  # Ensure it's within 0x00 to 0xFF

# Display the output matrix
for i in range(256):
    print(f"Galois {i:02x}: Output = {output_matrix[i]:02x}")
