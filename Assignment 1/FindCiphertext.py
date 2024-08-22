import subprocess
import re

# Path to your binary file
binary_path = '/home/kali/SPM/encrypt.bin'

# Define a regex pattern to extract the ciphertext
ciphertext_pattern = re.compile(r'ciphertext\s*:\s*([0-9a-fA-F]+)')

# Dictionary to store results
results = {}

# Generate all hexadecimal values from 00 to FF
hex_values = [f'{i:02x}' for i in range(256)]

# Loop through all hexadecimal values
for hex_value in hex_values:
    # Run the binary file with the hexadecimal input
    process = subprocess.Popen([binary_path], 
                               stdin=subprocess.PIPE, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE,
                               text=True)  # Use text=True to handle input/output as strings
    
    # Send the hexadecimal value to the binary's stdin
    stdout, stderr = process.communicate(input=f'{hex_value}\n')
    
    # Wait for the process to complete
    process.wait()
    
    # Check if there was any error
    if process.returncode != 0:
        print(f"Error processing value '{hex_value}': {stderr}")
    else:
        # Extract ciphertext using regex
        match = ciphertext_pattern.search(stdout)
        if match:
            ciphertext = match.group(1)
            results[hex_value] = ciphertext
        else:
            print(f"Failed to extract ciphertext for value '{hex_value}'")

# Display results
for hex_value, ciphertext in results.items():
    print(f"Hex Value: {hex_value} -> Ciphertext: {ciphertext}")
