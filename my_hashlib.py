import hashlib

def generate_sha256_hash(input_string):
    # Create a new sha256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the bytes of the input string
    sha256_hash.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string to hash: ")
    hashed_value = generate_sha256_hash(input_string)
    print(f"SHA-256 Hash: {hashed_value}")
