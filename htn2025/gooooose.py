import cv2
import numpy as np


def extract_lsb_rgb(img):
    # Open image and convert to RGB
    data = np.array(img)  # shape: (height, width, 3)

    # Extract the least significant bit (LSB) of each RGB channel
    # This will give a 3D array of bits (0 or 1)
    lsb_bits = data & 1  # bitwise AND with 1 to keep only LSB

    # Flatten the bits to a 1D array in RGB order per pixel
    bits = lsb_bits.flatten()

    # Group bits into bytes (8 bits per byte)
    bytes_ = np.packbits(bits)

    # Convert bytes to string (stop at first 0 byte or decode error)
    message = ''
    for b in bytes_:
        if b == 0:
            break
        try:
            message += chr(b)
        except:
            break

    return message

img = cv2.imread(input("Enter the path to the image: "))
# remove alpha channel
img = img[:, :, :3]  # Keep only RGB channels
print("Extracted message:", extract_lsb_rgb(img))
