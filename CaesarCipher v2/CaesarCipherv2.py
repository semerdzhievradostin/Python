from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '$', '{', '}', '(', ')', '[', ']', '.', ',', ':', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '$', '{', '}', '(', ')', '[', ']', '.', ',', ':', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
def caesar(start_text, shift_amount, cipher_direction):
  shift_amount = shift % len(alphabet)
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

restart = True
while restart == True:
  question = input("Do you want to restart the cipher ? Type yes or no...\n ")
  if question == "no":
    restart = False
  else:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)



