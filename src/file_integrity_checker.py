# file_integrity_checker.py
# ------------------------------------------------------------
# This script generates the SHA-256 hash value for any file.
# It serves as a part of the File Integrity Checker project,
# helping to verify file authenticity and detect alterations.
# ------------------------------------------------------------

import hashlib

def calculate_hash(file_path):
    """
    Calculates the SHA-256 hash of the given file.

    Args:
        file_path (str): Path to the target file.

    Returns:
        str: Hexadecimal hash string if successful, None otherwise.
    """
    try:
        sha256 = hashlib.sha256()

        # Read file in chunks to handle large files efficiently
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        print(f"[Error] File not found: {file_path}")
        return None


def main():
    """
    Main driver function for user interaction.
    """
    print("=== FILE HASH GENERATOR ===")
    path = input("Enter the path of the file: ").strip()

    hash_value = calculate_hash(path)
    if hash_value:
        print(f"SHA-256 Hash Value: {hash_value}")
    else:
        print("[!] Unable to generate hash. Please check the file path.")


if __name__ == "__main__":
    main()
