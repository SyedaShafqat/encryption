# Fernet Encryption and Decryption
This program demonstrates encrypting and decrypting a message using the Fernet encryption scheme in Python. It takes a message and an 8-digit key from the user, encrypts the message using Fernet encryption, then decrypts the encrypted message using the same key.
## Fernet
Fernet is a symmetric encryption algorithm provided by the cryptography library in Python. It generates secure encryption keys and allows for easy encryption and decryption of data.
## Fernet Encryption and Decryption Code
```
# Instance the Fernet class with the key
fernet = Fernet(encoded_key)

# Encrypt the message
encMessage = fernet.encrypt(message.encode())

# Decrypt the encrypted message
decMessage = fernet.decrypt(encMessage).decode()

```
## base64
In Fernet encryption, the key is encoded to base64 to ensure it's in a format compatible with Fernet's requirements for key input, enabling secure encryption and decryption operations.
```
encoded_key = base64.urlsafe_b64encode(key_input.encode())
```
## Output Image

![Output Image](https://github.com/SyedaShafqat/encryption/blob/master/encrpt.png)

