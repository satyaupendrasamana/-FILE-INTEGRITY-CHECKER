# file_integrity_checker.py
# -----------------------------------------------------------
# This script provides a simple File Integrity Checker tool.
# It calculates, stores, and verifies SHA-256 hash values of
# files to detect unauthorized changes or modifications.
# -----------------------------------------------------------

import hashlib

def calculate_hash(file_path):
    """
    Calculate the SHA-256 hash of a file.

    Args:
        file_path (str): Path of the target file.

    Returns:
        str: Hash value in hexadecimal format, or None if file not found.
    """
    try:
        hasher = hashlib.sha256()
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
    Store the hash value of a file in a local reference file (hashes.txt).

    Args:
        file_path (str): The path of the file.
        hash_value (str): The calculated SHA-256 hash value.
    """
    try:
        with open("hashes.txt", "a") as hash_file:
            hash_file.write(f"{file_path} {hash_value}\n")
        print("[Info] Hash stored successfully in 'hashes.txt'")
    except Exception as e:
        print(f"[Error] Could not store hash: {e}")


def check_integrity(file_path):
    """
    Compare the current hash of a file with its previously stored hash.

    Args:
        file_path (str): Path of the file to check.
    """
    try:
        with open("hashes.txt", "r") as hash_file:
            for line in hash_file:
                stored_path, stored_hash = line.strip().split(" ", 1)
                if stored_path == file_path:
                    current_hash = calculate_hash(file_path)
                    if current_hash == stored_hash:
                        print("[✔] File is intact (No modification detected).")
                    else:
                        print("[⚠] WARNING: File has been modified!")
                    return
        print("[!] No record found for this file. Please store its hash first.")
    except FileNotFoundError:
        print("[!] No stored hashes found. Run the hash generator first.")


def main():
    """
    Main menu-driven block for user interaction.
    """
    print("=== FILE INTEGRITY CHECKER ===")
    print("1. Store file hash")
    print("2. Check file integrity")

    choice = input("Enter your choice (1/2): ").strip()
    file_path = input("Enter the file path: ").strip()

    if choice == "1":
        file_hash = calculate_hash(file_path)
        if file_hash:
            print(f"SHA-256 Hash: {file_hash}")
            store_hash(file_path, file_hash)

    elif choice == "2":
        check_integrity(file_path)

    else:
        print("[Error] Invalid choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()
