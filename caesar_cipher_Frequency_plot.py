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

if  __name__ == '__main__':
    plain_text = "This is a very long text The text does not contain special characters and other symbols This is just alphabet letters Only for demo purpose to understand the frequency anlysis cracking mechanism"
    freq = frequency_analysis(plain_text)
    plot_distribution(freq)