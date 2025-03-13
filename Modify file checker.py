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

def check_integrity(file_path):
    """Compare the current hash with the stored hash to check integrity."""
    try:
        with open("hashes.txt", "r") as hash_file:
            for line in hash_file:
                stored_path, stored_hash = line.strip().split(" ", 1)
                if stored_path == file_path:
                    current_hash = calculate_hash(file_path)
                    if current_hash == stored_hash:
                        print("✅ File is intact (No modification detected).")
                    else:
                        print("⚠️ WARNING: File has been modified!")
                    return
        print("⚠️ No record found for this file. Please store its hash first.")
    except FileNotFoundError:
        print("⚠️ No stored hashes found. Please generate and store hashes first.")

# User choice menu
print("Choose an option:")
print("1. Store file hash")
print("2. Check file integrity")

choice = input("Enter your choice (1/2): ")

file_path = input("Enter the file path: ")

if choice == "1":
    file_hash = calculate_hash(file_path)
    if file_hash:
        print(f"SHA-256 Hash: {file_hash}")
        store_hash(file_path, file_hash)
elif choice == "2":
    check_integrity(file_path)
else:
    print("Invalid choice! Please enter 1 or 2.")
