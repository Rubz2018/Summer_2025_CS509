import matplotlib.pylab as plt
"""
We need the alphabet because we convert letters into numerical values to be 
able to use mathematical opeartions (Note we encrypt the space as well)
"""
LETTERS  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def frequency_analysis(text):
    text = text.upper()
    # We use letter dictionary to store letter 
    letter_frequencies ={}
    for letter in LETTERS:
        letter_frequencies[letter]=0
    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1
    return letter_frequencies

def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()

# def caser_crack(cipher_text):
#     freq = frequency_analysis(cipher_text)
#     print(freq)
#     plot_distribution(freq)
def caser_crack(cipher_text):
    freq= frequency_analysis(cipher_text)
    freq = sorted(freq.items(), key = lambda x:x[1], reverse=True)
    print("The possible key value: %s" % (LETTERS.find(freq[0][0]) - LETTERS.find('E')) )

        
if  __name__ == '__main__':
    plain_text = "Welcome to the cyber security course"
    plain_freq= frequency_analysis(plain_text)
    plain_freq_sorted = sorted(plain_freq.items(), key = lambda x:x[1], reverse=True)
    print(f"Plain text frequency distribution: {plain_freq_sorted}")
    #plot_distribution(freq)
    cipher_text = "ZHOFRPHCWRCWKHCFAEHUCVHFXULWACFRXUVH"
    cipher_freq=frequency_analysis(cipher_text)
    cipher_freq_sorted = sorted(cipher_freq.items(), key = lambda x:x[1], reverse=True)
    print(f"cipher text frequency distribution: {cipher_freq_sorted}")
    caser_crack(cipher_text)

    

    