import numpy as np

# Example inverse functions (implement these)
def inverse_subbytes(state):
    # Apply the inverse S-Box substitution
    pass

def inverse_shiftrows(state):
    # Apply inverse shift rows
    pass

def inverse_mixcolumns(state):
    # Apply inverse mix columns
    pass

def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

def bytes_to_matrix(byte_array):
    return np.array([list(byte_array[i:i + 4]) for i in range(0, 16, 4)], dtype=np.uint8)

def matrix_to_bytes(matrix):
    return matrix.flatten()

def reverse_key_expansion(last_round_key, num_rounds):
    # Convert the last round key to a 4x4 matrix
    state = bytes_to_matrix(last_round_key)
    
    # List to store round keys
    round_keys = [state]
    
    # Reverse the key expansion process
    for round in range(num_rounds - 1, 0, -1):
        # Apply the inverse transformations
        state = inverse_subbytes(state)
        state = inverse_shiftrows(state)
        if round < num_rounds - 1:
            state = inverse_mixcolumns(state)
        
        # XOR with the previous round key to get the current round key
        state = np.bitwise_xor(state, round_keys[-1])
        round_keys.append(state)
    
    # Return the original key
    return matrix_to_bytes(round_keys[-1])

# Example last round key in hex string format
last_round_key_hex = "c7c1a5f428c519944c8e2e2564ce0f01"
last_round_key = hex_to_bytes(last_round_key_hex)

# Number of rounds for AES-like cipher
num_rounds = 4

# Find the original key
original_key = reverse_key_expansion(last_round_key, num_rounds)
print(f"Original Key: {original_key.hex()}")
