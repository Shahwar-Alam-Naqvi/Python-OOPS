import hashlib

# Function to calculate checksum
def calculate_checksum(data):
    # Calculating checksum using SHA-256
    checksum = hashlib.sha256(data.encode()).hexdigest()
    return checksum

# Original data
data = "Important data"
checksum_original = calculate_checksum(data)
print("Original Checksum:", checksum_original)

# Simulating data modification
data_modified = "Important data with modification"
checksum_modified = calculate_checksum(data_modified)
print("Modified Checksum:", checksum_modified)

# Checking data integrity
if checksum_original == checksum_modified:
    print("Data is intact")
else:
    print("Data has been tampered with")
