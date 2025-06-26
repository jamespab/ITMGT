def scytale_decipher(message, shift):
   original_message = ""
   length = len(message)
   for i in range(0, length):
       char_position = shift*i - length * int((i*shift)/length) + int((i*shift)/length)
       original_message = original_message + message[char_position]
    return original_message