"""
We need the alphabet because we convert letters into numerical values to be 
able to use mathematical opeartions (Note we encrypt the space as well)
"""
alphabet  = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vigenere_encrypt(plain_text, vigenere_key):
    # The encrypted message
    cipher_text = ''
    # consider all the letters in the plain_text
    plain_text = plain_text.upper()
    vigenere_key = vigenere_key.upper()
    key_index = 0

    for character in plain_text:
        """
        number of the shift = index of the character in the alphabet + index of the character in the key
        """
        index = alphabet.find(character)
        key = alphabet.find(vigenere_key[key_index])
        index = (index + key) % len(alphabet)
        # Keep appending the cipher text
        cipher_text = cipher_text + alphabet[index]
        # increasing the key index because we consider the next letter
        key_index += 1
        if key_index == len(vigenere_key):
            key_index = 0

    return cipher_text

def vigenere_decrypt(cipher_text, vigenere_key):
    # The decrypted message
    plain_text = ''
    cipher_text = cipher_text.upper()
    vigenere_key = vigenere_key.upper()
    key_index = 0

    for character in cipher_text:
        index = alphabet.find(character)
        key = alphabet.find(vigenere_key[key_index])
        index = (index - key) % len(alphabet)
        # Keep appending the plain text
        plain_text = plain_text + alphabet[index]
        key_index = key_index + 1
        if key_index == len(vigenere_key):
            key_index = 0

    return plain_text

if  __name__ == '__main__':
    text = 'cryptography is quite important in the cryptocurrency'
    encrypted = vigenere_encrypt(text, 'ANIMAL')
    print(f"The encrypted message is:{encrypted} ")
    print(f"And the decrypted message is:{vigenere_decrypt(encrypted, 'ANIMAL' )} ")