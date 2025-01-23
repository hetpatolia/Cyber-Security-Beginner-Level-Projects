import random
import string
import os

def generate_password(length=12):
    """Generate a strong, random password."""
    if length < 8 or length > 16:
        length = random.randint(8, 16)
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def store_password(password, liked):
    """Store password with user choice in a file in the same directory."""
    current_dir = os.path.dirname(__file__)  # Get the directory of the script
    filename = os.path.join(current_dir, "password_records.txt")
    entry_count = 1
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            if len(lines) > 1:
                entry_count = len(lines)
    with open(filename, "a") as file:
        if entry_count == 1:
            file.write(f"{'No.':<5}{'Generated Password':<30}{'User Choice (Liked/Unliked)'}\n")
        file.write(f"{entry_count:<5}{password:<30}{liked}\n")
    print(f"Passwords stored in: {filename}")

def menu():
    """Main menu for generating passwords and handling user feedback."""
    while True:
        print("\n--- Password Generator ---")
        print("1. Generate a Password")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ").strip()
        
        if choice == '1':
            password = generate_password()
            print(f"Generated Password: {password}")
            user_feedback = input("Do you like this password? (yes/no): ").strip().lower()
            liked = "Liked" if user_feedback in ["yes", "y"] else "Unliked"
            store_password(password, liked)
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    menu()
