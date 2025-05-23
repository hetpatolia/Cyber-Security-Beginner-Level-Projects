import hashlib
import os
import json

def calculate_hash(file_path, algorithm='sha256'):
    """Calculate the hash of a file using the specified hashing algorithm."""
    try:
        hasher = hashlib.new(algorithm)
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None

def generate_file_hashes(directory, output_file='file_hashes.json', algorithm='sha256'):
    """Generate hashes for all files in a directory and save them to a JSON file."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path, algorithm)
            if file_hash:
                file_hashes[file_path] = file_hash
    
    with open(output_file, 'w') as json_file:
        json.dump(file_hashes, json_file, indent=4)
    print(f"File hashes saved to {output_file}")

def check_file_integrity(directory, hash_file='file_hashes.json', algorithm='sha256'):
    """Check the integrity of files by comparing their current hashes with saved hashes."""
    try:
        with open(hash_file, 'r') as json_file:
            stored_hashes = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: Hash file not found - {hash_file}")
        return
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            current_hash = calculate_hash(file_path, algorithm)
            stored_hash = stored_hashes.get(file_path)
            
            if current_hash and stored_hash:
                if current_hash == stored_hash:
                    print(f"File OK: {file_path}")
                else:
                    print(f"File Modified: {file_path}")
            elif not stored_hash:
                print(f"New File Detected: {file_path}")
            elif not current_hash:
                print(f"File Missing: {file_path}")

if __name__ == "__main__":
    print("File Integrity Checker")
    print("1. Generate File Hashes")
    print("2. Check File Integrity")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        directory = input("Enter the directory to scan: ")
        output_file = input("Enter output hash file name (default: file_hashes.json): ") or 'file_hashes.json'
        generate_file_hashes(directory, output_file)
    elif choice == '2':
        directory = input("Enter the directory to check: ")
        hash_file = input("Enter the hash file name (default: file_hashes.json): ") or 'file_hashes.json'
        check_file_integrity(directory, hash_file)
    else:
        print("Invalid choice.")
