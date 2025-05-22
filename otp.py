# We need the alphabet because we convert Letter into numerical values to be able to use
#mathematical operation (Note we encrypt space as well)
from random import randint
import matplotlib.pylab as plt



ALPHABET =  ' ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

# one time pad (OTP)
def encrypt(text, key):
    text = text.upper()
    cipher_text = ''

    for index, char in enumerate(text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        
        # encrypted letter = char's value in the plain text + random value (using mod len(ALPHABET))
        encrypted_char_index = (char_index + key_index) % len(ALPHABET)
        
        # convert the encrypted index back to a character and append to cipher_text
        cipher_text += ALPHABET[encrypted_char_index]

    return cipher_text

def decrypt(cipher_text, key):
    plain = ''

    for index, char in enumerate(cipher_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain += ALPHABET[(char_index - key_index) % len(ALPHABET)]
    
    return plain



def random_sequence(text):
    random = []

    for _ in range(len(text)):
        random.append(randint(0,len(ALPHABET)-1))

    return random 

def frequency_analysis(text):
    text = text.upper()
    # We use letter dictionary to store letter 
    letter_frequencies ={}
    for letter in ALPHABET:
        letter_frequencies[letter]=0
    for letter in text:
        if letter in ALPHABET:
            letter_frequencies[letter] += 1
    return letter_frequencies

def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


if __name__ == '__main__':
    message ='This is a very long text The text does not contain special characters and other symbols This is just alphabet letters Only for demo purpose to understand the frequency anlysis cracking mechanism'
    seq = random_sequence(message)
    print("Original message : %s" % message.upper())
    cipher = encrypt(message,seq)
    print("Encrypted message: %s" % cipher)
    decypted_text = decrypt(cipher,seq)
    print("Decrypted message: %s" % decypted_text)
    plot_distribution(frequency_analysis(cipher))


 
