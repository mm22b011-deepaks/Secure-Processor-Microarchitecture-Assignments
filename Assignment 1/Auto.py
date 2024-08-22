import subprocess
import re

# Define the plaintexts
plaintexts = ['00', '01', '03', '04', '05', '06', '07', '08', '09', '0a','0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14']

# Path to your binary file
binary_path = '/home/kali/SPM/encrypt.bin'

# Dictionary to store results
results = {}

# Define a regex pattern to extract the ciphertext
ciphertext_pattern = re.compile(r'ciphertext\s*:\s*([0-9a-fA-F]+)')

# Loop through plaintexts
for plaintext in plaintexts:
    # Run the binary file with the plaintext input
    process = subprocess.Popen([binary_path], 
                               stdin=subprocess.PIPE, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE,
                               text=True)  # Use text=True to handle input/output as strings
    
    # Send the plaintext to the binary's stdin
    stdout, stderr = process.communicate(input=f'{plaintext}\n')
    
    # Wait for the process to complete
    process.wait()
    
    # Check if there was any error
    if process.returncode != 0:
        print(f"Error processing plaintext '{plaintext}': {stderr}")
    else:
        # Extract ciphertext using regex
        match = ciphertext_pattern.search(stdout)
        if match:
            ciphertext = match.group(1)
            results[plaintext] = ciphertext
        else:
            print(f"Failed to extract ciphertext for plaintext '{plaintext}'")

# Display results
for plaintext, ciphertext in results.items():
    print(f"Plaintext: {plaintext} -> Ciphertext: {ciphertext}")
