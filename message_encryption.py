def encrypt(text, shift):
    """Encrypts the input text using Caesar cipher with the specified shift."""
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            result += new_char
        else:
            result += char  # Keep spaces and punctuation unchanged
    return result

def decrypt(text, shift):
    """Decrypts the input text using Caesar cipher with the specified shift."""
    return encrypt(text, -shift)

def menu():
    """Displays a menu and handles user input for encryption, decryption, or exiting."""
    while True:
        print("\n--- Message Encryption and Decryption ---")
        print("1. Encrypt a Message")
        print("2. Decrypt a Message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            message = input("Enter the message to encrypt: ").strip()
            shift = int(input("Enter the shift key (integer): ").strip())
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter the message to decrypt: ").strip()
            shift = int(input("Enter the shift key (integer): ").strip())
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    menu()
