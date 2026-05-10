import random


def main():
    letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "1234567890"
    special_chars = "!@#$%^&*(){}[]/*`~+-.<>?"
    dataset = letters + numbers + special_chars
    password = ""
    for char in range(16):
        password += random.choice(dataset)
    print(f"Password: {password}")


if __name__ == "__main__":
    main()
