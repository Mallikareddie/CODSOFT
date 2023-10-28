import random
import string

def generate_password(length):
    combine = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(combine) for i in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print(" Please enter a positive number.")
        else:
            password = generate_password(length)
            print("Generated Password: ", password)
    except ValueError:
        print("Invalid input.")

main()