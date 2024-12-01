import random
import string

def generate_password(length):
    # Define character sets for password complexity
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt user for desired password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

# Run the main function
if __name__ == "__main__":
    main()
