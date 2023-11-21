import cv2
import os

def encrypt_message(img, msg):
    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    n, m, z = 0, 0, 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    return img

def decrypt_message(img, password):
    c = {}
    for i in range(255):
        c[i] = chr(i)

    message = ""
    n, m, z = 0, 0, 0

    pas = input("Enter passcode for Decryption: ")

    if password == pas:
        for _ in range(len(msg)):
            message += c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decryption message:", message)
    else:
        print("Not a valid key")

# Load the image
img = cv2.imread("Image.jpg")

# Get the secret message from the user
msg = input("Enter secret message: ")

# Get the password from the user
password = input("Enter password: ")

# Encrypt the message into the image
img = encrypt_message(img, msg)

# Save the encrypted image
cv2.imwrite("stegno.jpg", img)

# Open the encrypted image
os.system("start stegno.jpg")

# Decrypt the message from the encrypted image
decrypt_message(img, password)
