import hashlib

def calculate_hash(file_path):
    """
    Function: calculate_hash
    Purpose : To generate the SHA-256 hash value of the given file.
    """

    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                sha256.update(data)
        return sha256.hexdigest()

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


# main program
if __name__ == "__main__":
    file_path = input("Enter the path of the file: ").strip()
    result = calculate_hash(file_path)

    if result:
        print("SHA-256 Hash Value:", result)
