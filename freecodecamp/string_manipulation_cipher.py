text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        # 1. Handle Non-Letters
        # If the character is a space or punctuation, keep it as-is
        if not char.isalpha():
            final_message += char
        else:        
            # 2. Key Rotation
            # Use modulo (%) to loop the key. If the key is 'abc' and the 
            # message is long, it will go a-b-c-a-b-c...
            key_char = key[key_index % len(key)]
            key_index += 1

            # 3. Calculate the Shift (Offset)
            # Find the numerical position of the key character (a=0, b=1, etc.)
            offset = alphabet.index(key_char)
            
            # Find the numerical position of the message character
            index = alphabet.find(char)
            
            # 4. Apply Direction (Encrypt or Decrypt)
            # If direction is 1, we add the offset (Encrypt)
            # If direction is -1, we subtract the offset (Decrypt)
            # Modulo 26 (% len(alphabet)) ensures the result wraps around the alphabet
            new_index = (index + offset * direction) % len(alphabet)
            
            # 5. Build the result
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    # Calls vigenere with default direction (1)
    return vigenere(message, key)
    
def decrypt(message, key):
    # Calls vigenere with direction (-1) to reverse the shift
    return vigenere(message, key, -1)

# --- Execution ---
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')

# This will take 'mrttaqrhknsw ih puggrur' and shift it backward using 'happycoding'
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')