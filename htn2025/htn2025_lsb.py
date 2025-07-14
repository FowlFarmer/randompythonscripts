import numpy as np
from PIL import Image

def extract_lsb_rgb(image_path):
    # Open image and convert to RGB
    img = Image.open(image_path).convert('RGB')
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

if __name__ == '__main__':
    msg = extract_lsb_rgb(input())
    print('Extracted message:', msg)
