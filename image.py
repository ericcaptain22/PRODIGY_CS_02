from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Example encryption operation: swapping pixel values
            r ^= key
            g ^= key
            b ^= key
            encrypted_pixels.append((r, g, b))

    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    width, height = img.size
    pixels = img.load()

    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Reverse the encryption operation
            r ^= key
            g ^= key
            b ^= key
            decrypted_pixels.append((r, g, b))

    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.show()
    print("Image decrypted successfully!")

# Example usage
image_path = "/home/ericcaptain22/Pictures/Batman.jpg"
encryption_key = 110
encrypt_image(image_path, encryption_key)

encrypted_image_path = "encrypted_image.png"
decrypt_image(encrypted_image_path, encryption_key)