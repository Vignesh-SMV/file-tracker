import tkinter
from tkinter import filedialog
from tkinter import Tk
from PIL import Image
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate RSA key pair



# Load public key from file
with open("public_key.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

# Load private key from file
with open("private_key.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

# Function to hide RSA encrypted message in an image
def hide_rsa_message(image_path, message):
    img = Image.open(image_path)
    width, height = img.size

    # Encrypt message using RSA
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_message = base64.b64encode(cipher_rsa.encrypt(message.encode()))

    binary_message = ''.join(format(byte, '08b') for byte in encrypted_message)
    message_length = len(binary_message)

    index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            for i in range(3):
                if index < message_length:
                    pixel[i] = pixel[i] & ~1 | int(binary_message[index])
                    index += 1
            img.putpixel((x, y), tuple(pixel))

    img.save(image_path)

def des(top,message_to_hide,original_image_path):
    message_to_hide = message_to_hide.get()
    hide_rsa_message(original_image_path, message_to_hide)

    print("Image successfully secured.", message_to_hide)
    top.destroy()
def toplevel(root,original_image_path):
    top = tkinter.Toplevel(root)
    top.configure(width=500,height=500)
    label=tkinter.Label(top, text="Enter the G-mail Address :")
    label.pack()
    entry=tkinter.Entry(top)
    entry.pack()
    button=tkinter.Button(top,text="secure",command=lambda:des(top,entry,original_image_path))
    button.pack()
    #message_to_hide = input("Enter the Gmail id : ")

    top.mainloop()

def secure():
    root = Tk()
    root.withdraw()  # Hide the main window

    original_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if not original_image_path:
        print("No image selected.")
        return

    #choice = input("Enter 1 to hide a message, 2 to extract a message: ")
    toplevel(root,original_image_path)






