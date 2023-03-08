alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
choice1 = "encode"
choice2 = "decode"


def caesar(text, shift, direction):
    if direction == choice1:
        alphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        plain_text = text
        text_lenght = len(plain_text)
        drowedoc = ""
    
    
        for position in range(text_lenght):
            for letter in plain_text[position]:
                alphabetposition = alphabet2.index(letter)
                cipherpos = alphabetposition + shift
                codeword = alphabet2[cipherpos]
                for letter in codeword:
                    drowedoc += str(letter)
                    if len(drowedoc) == len(plain_text):
                        print(drowedoc)
                        
    if direction == choice2:
        plain_text = text
        text_lenght = len(plain_text)
        decmessage = ""
    
    
        for position in range(text_lenght):
            for letter in plain_text[position]:
                alphabetposition = alphabet.index(letter)
                cipherpos = alphabetposition - shift
                codeword = alphabet[cipherpos]
                for letter in codeword:
                    decmessage += str(letter)
                    if len(decmessage) == len(plain_text):
                        print(decmessage)


caesar(text, shift, direction)   

