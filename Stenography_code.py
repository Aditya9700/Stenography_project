import cv2
import os
def print_banner():
    print("=" * 50)
    print("       THE IMAGE STEGANOGRAPHY TOOL")
    print("=" * 50)

def encrypt_message(image_path, secret_message, passcode):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: The Imageis not found! Please check the path.")
        return

    char_to_int = {chr(i): i for i in range(255)}
    x, y, channel = 0, 0, 0

    for char in secret_message:
        image[y, x, channel] = char_to_int[char]
        x += 1
        y += 1
        channel = (channel + 1) % 3

    encrypted_image_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_image_path, image)
    print("\nEncryption successful!! Encrypted image saved as 'encryptedImage.jpg'\n")
    os.system(f'start {encrypted_image_path}')
    return image, passcode

def decrypt_message(image, passcode, original_passcode, message_length):
    print("\n=== DECRYPTION MODE ===")
    user_passcode = input("Enter passcode for decryption: ")
    
    if user_passcode == original_passcode:
        decrypted_message = ""
        x, y, channel = 0, 0, 0
        int_to_char = {i: chr(i) for i in range(255)}
        
        for _ in range(message_length):
            decrypted_message += int_to_char[image[y, x, channel]]
            x += 1
            y += 1
            channel = (channel + 1) % 3

        print("\nDecrypted message: ", decrypted_message)
    else:
        print("\nWrong password! Decryption failed.")

if __name__ == "__main__":
    print_banner()
    image_path = "newimage.jpg"
    # Replace with the correct image path
    secret_message = input("Enter secret message: ")
    passcode = input("Enter a passcode: ")
    
    encrypted_image, stored_passcode = encrypt_message(image_path, secret_message, passcode)
    
    if encrypted_image is not None:
        decrypt_message(encrypted_image, stored_passcode, passcode, len(secret_message))
