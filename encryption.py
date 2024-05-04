from cryptography.fernet import Fernet
import base64

# Get message from the user
message = input("Enter your message: ")

# Get an 8 digit key
keyInput = input("Enter an eight digit key for encryption: ")

if len(keyInput) != 8:
    print("Key must be 8 bytes long.")
    exit()

# Pad the key if needed (Fernet requires 32 bytes key)
key_input = keyInput.ljust(32, ' ')

# Encode the key to base64
encoded_key = base64.urlsafe_b64encode(key_input.encode())

# Instance the Fernet class with the key
fernet = Fernet(encoded_key)

# Encrypt the message
encMessage = fernet.encrypt(message.encode())

print("Original message:", message)
print("Encrypted message:", encMessage)

# Decrypt the encrypted message
decMessage = fernet.decrypt(encMessage).decode()

print("Decrypted message:", decMessage)
