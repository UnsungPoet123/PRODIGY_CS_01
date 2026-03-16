def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                shifted = (ord(char) - ascii_offset + shift) % 26
            elif mode == "decrypt":
                shifted = (ord(char) - ascii_offset - shift) % 26

            result += chr(shifted + ascii_offset)
        else:
            result += char

    return result


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Type 'encrypt' or 'decrypt': ").lower()

output = caesar_cipher(message, shift, mode)

print("Result:", output)