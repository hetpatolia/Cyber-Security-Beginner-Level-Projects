import os

def dictionary_attack(target_password, dictionary_file_path):
    """Attempt to crack the password using a dictionary attack."""
    try:
        # Ensure the file exists
        if not os.path.isfile(dictionary_file_path):
            print(f"Error: Dictionary file '{dictionary_file_path}' not found.")
            return None

        print(f"Attempting to crack the password using dictionary file at: {dictionary_file_path}")
        with open(dictionary_file_path, 'r') as file:
            dictionary = file.readlines()

        for count, word in enumerate(dictionary, 1):
            word = word.strip()  # Remove any extra whitespace/newlines
            print(f"Attempt {count}: Trying '{word}'...")
            if word == target_password:
                print(f"Password cracked! The correct password is: {word}")
                return word  # Return the cracked password
        
        print("Password not found in the dictionary.")
        return None
    except FileNotFoundError:
        print(f"Error: Dictionary file '{dictionary_file_path}' not found.")
        return None

def menu():
    """Main menu for dictionary attack functionality."""
    while True:
        print("\n--- Dictionary Attack ---")
        print("1. Try to crack a password")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ").strip()
        
        if choice == '1':
            target_password = input("Enter the target password (for testing): ").strip()
            dictionary_file_path = input("Enter the full path of the dictionary file (e.g., C:\\path\\to\\dictionary.txt): ").strip()
            cracked_password = dictionary_attack(target_password, dictionary_file_path)
            if cracked_password:
                print(f"Cracked password: {cracked_password}")
            else:
                print("Failed to crack the password.")
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    menu()
