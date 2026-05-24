#Caesar Cipher game
#encryption and decryption are included

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift letter in the alphabet
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char  # keep punctuation/space/numbers unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # just reverse the shift

print("===== Caesar Cipher Game =====")

while True:
    print("\nSelect an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift number (e.g., 3): "))
        encrypted = encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
        
    elif choice == '2':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the original shift number used: "))
        decrypted = decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")
        
    elif choice == '3':
        print("Goodbye!")
        break
        
    else:
        print("Invalid input. Please try again.")
