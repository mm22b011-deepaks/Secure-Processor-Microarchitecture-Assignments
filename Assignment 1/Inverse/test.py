def hex_key_to_column_major_matrix(hex_key: str) -> list:
    # Ensure the hex string is 32 characters long (16 bytes)
    if len(hex_key) != 32:
        raise ValueError("Hex key must be 32 characters long")

    # Convert the hex string to bytes
    key_bytes = bytes.fromhex(hex_key)

    # Create a 4x4 column-major matrix storing hex strings
    matrix = [[f"{key_bytes[row + 4 * col]:02x}" for col in range(4)] for row in range(4)]
    
    return matrix

def generate_new_matrix(given_matrix: list) -> list:
    # Initialize the new matrix with empty lists for each row
    new_matrix = [[0] * 4 for _ in range(4)]
    
    # Copy the first column of the given matrix to the new matrix
    for i in range(4):
        new_matrix[i][0] = given_matrix[i][0]

    # Compute the 2nd column of the new matrix
    for i in range(4):
        new_matrix[i][1] = f"{int(given_matrix[i][0], 16) ^ int(given_matrix[i][1], 16):02x}"

    # Compute the 3rd column of the new matrix (using the 2nd column of the new matrix)
    for i in range(4):
        new_matrix[i][2] = f"{int(given_matrix[i][1], 16) ^ int(given_matrix[i][2], 16):02x}"

    # Compute the 4th column of the new matrix (using the 3rd column of the new matrix)
    for i in range(4):
        new_matrix[i][3] = f"{int(given_matrix[i][2], 16) ^ int(given_matrix[i][3], 16):02x}"

    return new_matrix

def display_matrix(matrix: list) -> None:
    for row in matrix:
        print(" ".join(row))

# Example usage
hex_key = "f025a22fc0439649a277a471c7449d44"
given_matrix = hex_key_to_column_major_matrix(hex_key)
new_matrix = generate_new_matrix(given_matrix)
display_matrix(new_matrix)
