# saving_hash.py
# --------------------------------------------------------
# This script handles the calculation and storage of file
# hash values using the SHA-256 algorithm.
# --------------------------------------------------------

import hashlib

def calculate_hash(file_path):
    """
    Calculates the SHA-256 hash of a given file.

    Args:
        file_path (str): Path to the file that needs hashing.

    Returns:
        str: Hexadecimal hash value of the file, or None if not found.
    """
    try:
        hasher = hashlib.sha256()

        # Read the file in chunks to handle large files efficiently
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)
                if not chunk:
                    break
                hasher.update(chunk)

        return hasher.hexdigest()

    except FileNotFoundError:
        print(f"[Error] File not found: {file_path}")
        return None


def store_hash(file_path, hash_value):
    """
    Stores the file path and its hash value in a reference file.

    Args:
        file_path (str): The original file path.
        hash_value (str): The calculated SHA-256 hash value.
    """
    try:
        with open("hashes.txt", "a") as hash_file:
            hash_file.write(f"{file_path} {hash_value}\n")
