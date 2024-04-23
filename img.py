from tkinter import filedialog
from tkinter import Tk
from PIL import Image
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
from code import get_info


# Load private key from file
with open("private_key.pem", "rb") as f:
    private_key = RSA.import_key(f.read())


# Function to extract RSA encrypted message from an image
def extract_rsa_message(image_path):
    img = Image.open(image_path)
    width, height = img.size

    binary_message = ""
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for i in range(3):
                binary_message += str(pixel[i] & 1)

    encrypted_message = bytes(int(binary_message[i:i+8], 2) for i in range(0, len(binary_message), 8))

    # Decrypt message using RSA
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher_rsa.decrypt(base64.b64decode(encrypted_message))

    return decrypted_message.decode()

def extract(original_image_path):
    root = Tk()
    root.withdraw()  # Hide the main window

    #original_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if not original_image_path:
        print("No image selected.")
        return

    mail = extract_rsa_message(original_image_path)
    print("Extracted message:", mail)

    get_info(mail)
    print(mail)
    print("img file executed")

