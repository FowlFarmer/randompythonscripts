import cv2
import numpy as np

def schematic(byte: int) -> bool:
    b0 = (byte >> 7) & 1
    b1 = (byte >> 6) & 1
    b2 = (byte >> 5) & 1
    b3 = (byte >> 4) & 1
    b4 = (byte >> 3) & 1
    b5 = (byte >> 2) & 1
    b6 = (byte >> 1) & 1
    b7 = byte & 1

    g1 = b1 & b2
    g2 = b6 ^ b7
    g3 = g1 | b4
    g4 = b5 & g2
    g5 = 1 - b0
    g6 = b3 & g3
    g7 = g6 | g4
    g8 = g5 & g6
    g9 = g6 | g7
    g10 = g8 & g9
    return g10

# Load image as RGB
img = cv2.imread(input("Enter the path to the image: "))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# Flatten RGB channels into a 1D array of bytes (0-255)
# redchannel = img[:, :, 0]
# greenchannel = img[:, :, 1]
# bluechannel = img[:, :, 2]
# flat_pixels = bluechannel.flatten()
flat_pixels = img.flatten()
decoded_bits = []
for i in range(0, len(flat_pixels)):
    decoded_bit = schematic(flat_pixels[i])
    decoded_bits.append(decoded_bit)

# Group decoded bits into bytes (8 bits per byte) and convert to chars
message_bytes = []
for i in range(0, len(decoded_bits) - 7, 8):
    val = 0
    for bit_index in range(8):
        val |= (decoded_bits[i + bit_index] << (7-bit_index))
    message_bytes.append(val)

# Convert bytes to string (ignore errors if non-ASCII)
decoded_message = ''.join(chr(b) for b in message_bytes if b != 0)

with open('decoded_mural2.txt', 'w', encoding='utf-8') as f:
    f.write(decoded_message)

