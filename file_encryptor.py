from cryptography.fernet import Fernet
import os

# Function to generate and write a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open('encryption_key.key', 'wb') as key_file:
        key_file.write(key)
    print("Key generated and saved to 'encryption_key.key'.")

# Function to load the encryption key from the file
def load_key():
    with open('encryption_key.key', 'rb') as key_file:
        return key_file.read()

# Function to encrypt a file with path input
def encrypt_file():
    filename = input("Enter the full path of the file to encrypt (e.g., C:\\path\\to\\file.txt): ")
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        return

    key = load_key()
    fernet = Fernet(key)

    with open(filename, 'rb') as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File '{filename}' encrypted successfully.")

# Function to decrypt a file with path input
def decrypt_file():
    filename = input("Enter the full path of the file to decrypt (e.g., C:\\path\\to\\file.txt): ")
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        return

    key = load_key()
    fernet = Fernet(key)

    with open(filename, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"File '{filename}' decrypted successfully.")

# Main program menu
def main():
    while True:
        print("\nFile Encryptor/Decryptor")
        print("1. Generate Encryption Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            generate_key()
        elif choice == '2':
            encrypt_file()
        elif choice == '3':
            decrypt_file()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
