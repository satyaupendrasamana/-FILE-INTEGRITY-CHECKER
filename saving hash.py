import hashlib

def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def store_hash(file_path, hash_value):
    """Store the hash value in a reference file."""
    with open("hashes.txt", "a") as hash_file:
        hash_file.write(f"{file_path} {hash_value}\n")
    print("Hash stored successfully!")

# Example usage
file_path = input("Enter the file path: ")
file_hash = calculate_hash(file_path)

if file_hash:
    print(f"SHA-256 Hash: {file_hash}")
    store_hash(file_path, file_hash)
