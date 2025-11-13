# caesar_cipher/caesar.py
# ------------------------------------------------------------
# Simple Caesar Cipher demonstration for encryption/decryption.
# ------------------------------------------------------------

def caesar_encrypt(text, shift):
    """Encrypt text using a Caesar cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    """Decrypt text encrypted with a Caesar cipher."""
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    print("=== Caesar Cipher Tool ===")
    choice = input("Encrypt (E) or Decrypt (D)? ").strip().lower()
    message = input("Enter text: ")
    shift = int(input("Enter shift (e.g., 3): "))

    if choice == "e":
        print("Encrypted:", caesar_encrypt(message, shift))
    elif choice == "d":
        print("Decrypted:", caesar_decrypt(message, shift))
    else:
        print("Invalid choice.")
