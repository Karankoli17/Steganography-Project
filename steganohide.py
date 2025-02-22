from PIL import Image
import numpy as np

def encode_text():
    image_path = input("Enter the path of the image: ")
    message = input("Enter the secret message: ")
    output_path = input("Enter the output image path: ")
    
    image = Image.open(image_path).convert('RGB')
    pixels = np.array(image, dtype=np.uint8)
    
    message += "@@@"  # End marker to detect extraction
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    data_index = 0
    total_pixels = pixels.shape[0] * pixels.shape[1] * 3
    if len(binary_message) > total_pixels:
        print("Error: Message is too long to hide in this image.")
        return
    
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # Iterate over R, G, B channels
                if data_index < len(binary_message):
                    pixel_value = pixels[i, j, k]
                    pixel_value = (pixel_value & 254) | int(binary_message[data_index])
                    pixels[i, j, k] = np.uint8(pixel_value)
                    data_index += 1
    
    encoded_image = Image.fromarray(pixels)
    encoded_image.save(output_path)
    print(f"Message encoded and saved to {output_path}")

def decode_text():
    image_path = input("Enter the path of the image to decode: ")
    image = Image.open(image_path)
    pixels = np.array(image, dtype=np.uint8)
    
    binary_message = ""
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):
                binary_message += str(pixels[i, j, k] & 1)
    
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if message.endswith("@@@"):
            break
        message += char
    
    print("Decoded Message:", message.replace("@@@", ""))

if __name__ == "__main__":
    choice = input("Do you want to encode or decode? (e/d): ").strip().lower()
    if choice == 'e':
        encode_text()
    elif choice == 'd':
        decode_text()
    else:
        print("Invalid choice. Please enter 'e' for encode or 'd' for decode.")
