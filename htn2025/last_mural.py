import numpy as np
from PIL import Image

def encode_lsb_rgb(image_path, message, output_path):
    # Open image and convert to RGB
    img = Image.open(image_path).convert('RGB')
    data = np.array(img)  # shape: (height, width, 3)

    # Flatten image data to 1D array
    flat_data = data.flatten()

    # Convert message to bytes, append a zero byte as terminator
    msg_bytes = message.encode('utf-8') + b'\x00'

    # Convert bytes to bits
    bits = np.unpackbits(np.frombuffer(msg_bytes, dtype=np.uint8))

    if len(bits) > len(flat_data):
        raise ValueError("Message is too long to encode in this image.")

    # Clear LSB of image data
    flat_data &= 0xFE  # zero out the LSB

    # Set LSB to message bits
    flat_data[:len(bits)] |= bits

    # Reshape to original image shape
    encoded_data = flat_data.reshape(data.shape)

    # Save new image
    encoded_img = Image.fromarray(encoded_data.astype('uint8'), 'RGB')
    encoded_img.save(output_path)

    print(f'Message encoded and saved to {output_path}')

if __name__ == '__main__':
    img_path = input("Input image path: ")
    msg = input("Message to encode: ")
    out_path = input("Output image path: ")
    encode_lsb_rgb(img_path, msg, out_path)
