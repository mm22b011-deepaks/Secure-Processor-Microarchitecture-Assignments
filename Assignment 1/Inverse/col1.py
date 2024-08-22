# Define the S-Box table (example)
S_BOX = [  0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,  0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,  0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,  0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,  0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,  0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,  0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,  0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,  0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,  0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,  0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,  0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,  0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,  0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,  0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,  0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,  0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,  0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,  0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88,  0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,  0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,  0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,  0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9,  0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,  0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6,  0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,  0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,  0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,  0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94,  0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,  0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68,  0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]


LOOKUP_TABLE = [
    0x8D,
    0x01,
    0x02,
    0x04,
    0x08,
    0x10,
    0x20,
    0x40,
    0x80,
    0x1B,
    0x36,
    0x6C,
    0xD8,
    0xAB,
    0x4D,
    0x9A,
    0x2F,
    0x5E,
    0xBC,
    0x63,
    0xC6,
    0x97,
    0x35,
    0x6A,
    0xD4,
    0xB3,
    0x7D,
    0xFA,
    0xEF,
    0xC5,
    0x91,
    0x39,
    0x72,
    0xE4,
    0xD3,
    0xBD,
    0x61,
    0xC2,
    0x9F,
    0x25,
    0x4A,
    0x94,
    0x33,
    0x66,
    0xCC,
    0x83,
    0x1D,
    0x3A,
    0x74,
    0xE8,
    0xCB,
    0x8D,
    0x01,
    0x02,
    0x04,
    0x08,
    0x10,
    0x20,
    0x40,
    0x80,
    0x1B,
    0x36,
    0x6C,
    0xD8,
    0xAB,
    0x4D,
    0x9A,
    0x2F,
    0x5E,
    0xBC,
    0x63,
    0xC6,
    0x97,
    0x35,
    0x6A,
    0xD4,
    0xB3,
    0x7D,
    0xFA,
    0xEF,
    0xC5,
    0x91,
    0x39,
    0x72,
    0xE4,
    0xD3,
    0xBD,
    0x61,
    0xC2,
    0x9F,
    0x25,
    0x4A,
    0x94,
    0x33,
    0x66,
    0xCC,
    0x83,
    0x1D,
    0x3A,
    0x74,
    0xE8,
    0xCB,
    0x8D,
    0x01,
    0x02,
    0x04,
    0x08,
    0x10,
    0x20,
    0x40,
    0x80,
    0x1B,
    0x36,
    0x6C,
    0xD8,
    0xAB,
    0x4D,
    0x9A,
    0x2F,
    0x5E,
    0xBC,
    0x63,
    0xC6,
    0x97,
    0x35,
    0x6A,
    0xD4,
    0xB3,
    0x7D,
    0xFA,
    0xEF,
    0xC5,
    0x91,
    0x39,
    0x72,
    0xE4,
    0xD3,
    0xBD,
    0x61,
    0xC2,
    0x9F,
    0x25,
    0x4A,
    0x94,
    0x33,
    0x66,
    0xCC,
    0x83,
    0x1D,
    0x3A,
    0x74,
    0xE8,
    0xCB,
    0x8D,
    0x01,
    0x02,
    0x04,
    0x08,
    0x10,
    0x20,
    0x40,
    0x80,
    0x1B,
    0x36,
    0x6C,
    0xD8,
    0xAB,
    0x4D,
    0x9A,
    0x2F,
    0x5E,
    0xBC,
    0x63,
    0xC6,
    0x97,
    0x35,
    0x6A,
    0xD4,
    0xB3,
    0x7D,
    0xFA,
    0xEF,
    0xC5,
    0x91,
    0x39,
    0x72,
    0xE4,
    0xD3,
    0xBD,
    0x61,
    0xC2,
    0x9F,
    0x25,
    0x4A,
    0x94,
    0x33,
    0x66,
    0xCC,
    0x83,
    0x1D,
    0x3A,
    0x74,
    0xE8,
    0xCB,
    0x8D,
    0x01,
    0x02,
    0x04,
    0x08,
    0x10,
    0x20,
    0x40,
    0x80,
    0x1B,
    0x36,
    0x6C,
    0xD8,
    0xAB,
    0x4D,
    0x9A,
    0x2F,
    0x5E,
    0xBC,
    0x63,
    0xC6,
    0x97,
    0x35,
    0x6A,
    0xD4,
    0xB3,
    0x7D,
    0xFA,
    0xEF,
    0xC5,
    0x91,
    0x39,
    0x72,
    0xE4,
    0xD3,
    0xBD,
    0x61,
    0xC2,
    0x9F,
    0x25,
    0x4A,
    0x94,
    0x33,
    0x66,
    0xCC,
    0x83,
    0x1D,
    0x3A,
    0x74,
    0xE8,
    0xCB,
    0x8D,
]

def _r_con(n: int) -> bytes:
    if not 0 <= n < 256:
        raise ValueError(f"Wrong n: {n}")
    return bytes([LOOKUP_TABLE[n], 0, 0, 0])

def _sub_word(word: bytes) -> bytes:
    if len(word) != 4:
        raise ValueError(f"Wrong word length: {len(word)}")
    return bytes([S_BOX[b] for b in word])

def _rot_word(word: bytes) -> bytes:
    if len(word) != 4:
        raise ValueError(f"Wrong word length: {len(word)}")
    return word[1:] + bytes([word[0]])

def hex_key_to_column_major_matrix(hex_key: str) -> list:
    # Ensure the hex string is 32 characters long (16 bytes)
    if len(hex_key) != 32:
        raise ValueError("Hex key must be 32 characters long")

    # Convert the hex string to bytes
    key_bytes = bytes.fromhex(hex_key)

    # Create a 4x4 column-major matrix storing hex strings
    matrix = [[f"{key_bytes[row + 4 * col]:02x}" for col in range(4)] for row in range(4)]
    
    return matrix

def calculate_first_column(hex_key: str, round_number: int) -> list:
    # Convert hex string to matrix
    given_matrix = hex_key_to_column_major_matrix(hex_key)
    
    # Get the 3rd column of the given matrix
    third_column = bytes([int(given_matrix[i][3], 16) for i in range(4)])
    
    # Rotate, substitute, and prepare the ready byte
    rotated = _rot_word(third_column)
    ready_byte = _sub_word(rotated)
    
    # Calculate Rcon
    rcon = _r_con(round_number)
    
    # XOR Rcon with 1st column of the given matrix
    first_column = bytes([int(given_matrix[i][0], 16) for i in range(4)])
    xor_result = bytes([rcon[i] ^ first_column[i] for i in range(4)])
    
    # XOR the result with the ready byte
    new_first_column = bytes([xor_result[i] ^ ready_byte[i] for i in range(4)])
    
    return [f"{byte:02x}" for byte in new_first_column]

# Example usage
hex_key = "f025a22f306634666234323865333935"  # Example 16-byte AES key
round_number = 1  # Specify the round number
new_first_column = calculate_first_column(hex_key, round_number)
print("New 1st column of the matrix:", new_first_column)
