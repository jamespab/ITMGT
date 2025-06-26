def shift_letter(letter, shift):
    if letter == " ":
        return " "
    else:
        if letter.isalpha():
            code_number = ord('A') if letter.isupper() else ord('a')
            offset = (ord(letter) - code_number + shift) % 26
            return chr(code_number + offset)



def caesar_cipher(message, shift):
    result = ""
    for char in message:
        if char == " ":
            result += " "
        elif char.isalpha():
            base_number = ord('A')
            offset = (ord(char) - base_number + shift) % 26
            result += chr(base_number + offset)
    return result


def shift_by_letter(letter, letter_shift):
    if letter == " ":
        actual_letter = " "
    elif letter.isalpha():
        shift_by = ord(letter_shift) - ord('A')
        shifted_letter = ((ord(letter) - ord('A') + shift_by) % 26) + ord('A')
        actual_letter = chr(shifted_letter)
    return str(actual_letter)

def vigenere_cipher(message, key):
    result = ""
    key_length = int(len(key))
    key_index = 0
    for char in message:
        if char.isalpha():
            key_counter = int(key_index % key_length)
            shift = ord(key[key_counter]) - ord('A')
            shifted_character = ((ord(char) - ord('A') + shift) % 26) + ord('A')
            result += chr(shifted_character)
            key_index += 1 
        else:
            result += char
            key_index += 1
    return result


def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_"

    if len(message) % shift == 0:
        x = len(message)
        columns = x // shift
        scytale_cipher = ['_'] * x
        for i in range(x):
            amount_per_row = i // columns
            column = i % columns
            scytale_cipher[amount_per_row + column * shift] = message[i]
        return "".join(scytale_cipher)
    

def scytale_decipher(message, shift):
   original_message = ""
   length = len(message)
   for i in range(0, length):
       char_position = shift*i - length * int((i*shift)/length) + int((i*shift)/length)
       original_message = original_message + message[char_position]
    return original_message