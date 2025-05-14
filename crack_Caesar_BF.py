"""
We need the alphabet because we convert letters into numerical values to be 
able to use mathematical opeartions (Note we encrypt the space as well)
"""
alphabet  = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def crack_caeser(cipher_text):

    for key in range(len(alphabet)):
        plain_text = ''

        for c in cipher_text:
            index = alphabet.find(c)
            index = (index - key) % len(alphabet)
            plain_text =plain_text + alphabet[index]

        print(f'With key {key}, the result is : {plain_text}')


if  __name__ == '__main__':
    encrypted = 'VDKBNLDZSNZSGDZBNLOTSDQZ MCZBXADQZRDBTQHSX hZBNTQRD'
    crack_caeser(encrypted)
    