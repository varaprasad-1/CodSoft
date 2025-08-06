import random
import string

def generate_password(length):
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower+ upper + digits + symbols

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    password += random.choices(all_chars, k=length - 3)
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        user_length = int(input("\nEnter desired password length: "))
        while user_length < 4:
            print("\nPassword length should be at least 4 characters.")
            user_length = int(input("Enter desired password length (greater than 4): "))
            

        password = generate_password(user_length)
        print(f"\nGenerated Password: {password}\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the generator only if this script is executed directly
if __name__ == "__main__":
    main()
