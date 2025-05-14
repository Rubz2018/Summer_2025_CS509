"""
We need the alphabet because we convert letters into numerical values to be 
able to use mathematical opeartions (Note we encrypt the space as well)
"""
alphabet  = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 4

def caeser_encrypt(plain_text):
    # The encrypted message
    cipher_text = ''
    # consider all the letters in the plain_text
    plain_text = plain_text.upper()
    for c in  plain_text:
        """
        find the numerical representation (index) associated with
        that character in the alphabet.
        We make the alphabet case insensitive.
        """
        index = alphabet.find(c)
        """
        caser encryption is just a simple shift of characters according to
        the key use modular arithmatic to transform the values within 
        the range [0,num_of_letters_in_alphabet] 
        """
        index = (index+key) % len(alphabet)
        # Keep appending the cipher text
        cipher_text = cipher_text + alphabet[index]

    return cipher_text

def caeser_decrypt(cipher_text):
    # The de crypted message
    plain_text = ''
    
    for c in  cipher_text:
        index = alphabet.find(c)
        index = (index-key)% len(alphabet)
        # Keep appending the plain text
        plain_text = plain_text + alphabet[index]

    return plain_text

if  __name__ == '__main__':
    m = 'Welcome to the Cryptography and Network Security course'
    encrypted = caeser_encrypt(m)
    print(f"The encrypted message is:{encrypted} ")
    print(f"And the decrypted message is:{caeser_decrypt(encrypted)} ")