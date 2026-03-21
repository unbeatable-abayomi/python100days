import math
#Functions

def greet():
    print("Hoday")
    print("Hope everything")
    print("Going Smooth")
    
greet()

def greet_with_name(name):
    print(f'Hello {name}')
    print(f'Hope everthing is fine {name}')
    print(f"All going smooth {name}")

name = 'abayomi'
greet_with_name(name)

#Functions with more the one parameter

def greet_with(name,location):
    print(f'Hi {name} where your current location')
    print(f"Hi i'm currently in {location}")

greet_with(name,'poland')


#Keyword Functions

def greet_with_postions(name="abayomi",location="poland",surname="igwubor"):
    print(f'Hi yomi this is your surname {surname}')
    print(f'So {name} is your firstname')
    print(f'You are located in {location}')


greet_with_postions('abayomi','abuja','igwubor')

width = int(input("Pls input width: "))

height = int(input("Pls input height: "))

coverage = int(input("Pls input coverage: "))

def print_cal (w=width,h=height,c=coverage):
        return (h/w)*c

restules = print_cal(width,height,coverage)


print(math.ceil(restules))

check_number = int(input("Input the number to check: "))

def prime_checker(number=check_number):
     is_prime = True
     for i in range(2,number):
          print(f'This is the number {i}')
          if number % i == 0:
            is_prime = False
     if is_prime :
          print(f"{number} is a prime number")
     else:
           print(f"{number} is not a prime number")


prime_checker(check_number)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' or 'decode' to do either: ").lower()

text = input("Type the text that you want to either encode or decode: ").lower()

shift_n = int(input("input shift: "))


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caser(word,shfit_count,direction):
    end_text = ""
    if direction == 'decode':
       shfit_count *= -1
    for letter in word:
        if letter in alphabet:
           position=alphabet.index(letter)
           new_posistion = position + shfit_count
           end_text += alphabet[new_posistion]
        else:
           end_text += letter
    print(f'Your {direction} text of {word} is now {end_text}')
    
should_contiue = True
while should_contiue:
    directions = input("Input either 'encode' or 'decode' :")
    words=input("Input word: ")
    shfit_counts  = int(input('input the amount: '))
    shfit_counts = shfit_counts % 26
    caser(word=words,shfit_count=shfit_counts,direction=directions)
    result = input('Type Yes or No to continue')
    if result == 'no':
        should_contiue = False
        print("Goodbye")

# def encrypt(words,shfit_number):
#     decrty_word = ''
#     for letter in words:
#         position=alphabet.index(letter)
#         shifted_posistion = position + shfit_number
#         decrty_word += alphabet[shifted_posistion]
#     print(f'This is the new word {decrty_word}')
# def decrypt(words,shfit_number):
#     decrty_word = ''
#     for letter in word:
#         position = alphabet.index(letter)
#         new_posistion = position - shfit_number
#         decrty_word += alphabet[new_posistion]
#     print(f'This is the new word {decrty_word}')
# decrypt(words=word,shfit_number=shfit_count)
# encrypt(words=word,shfit_number=shfit_count)
#number_to_check = int(input('Input number'))
# def prime_check(number):
#     is_prime = False
#     for i in range (2,number):
#         if number % i == 0:
#           is_prime = True
#     if is_prime:
#         print(f'{number} is not prime number')
#     else:
#         print(f'{number} is a prime number')
        
# prime_check(number=number_to_check)



# def encrpty (plain_text, shift_amount):
#      cipher_text = ''
#      for letter in plain_text:
#         if letter not in alphabet:
#             cipher_text += letter
#         else:
#             position=alphabet.index(letter)
#             shift_position = position + shift_amount
#             print(f'shift post {shift_position} posistion {position} and lenfgt {len(alphabet)}')
#             if shift_position >= len(alphabet):
#                 new_shift_position = shift_position - len(alphabet)
#                 new_letter = alphabet[new_shift_position+1]
#                 cipher_text += new_letter
#             else:
#              new_letter = alphabet[shift_position] 
#              cipher_text += new_letter
#      print(f'The is the encrptyed text {cipher_text}')


# def decrpty (plain_text, shift_amount):
#      cipher_text = ''
#      for letter in plain_text:
#         position=alphabet.index(letter)
#         shift_position = position - shift_amount
#         print(f'shift post {shift_position} posistion {position} and lenfgt {len(alphabet)}')
#         if shift_position == 0:
#             print(f' Shift {shift_position}')
#             new_shift_position = len(alphabet) - len(alphabet) 
#             print(f' new Shift {new_shift_position}')
#             new_letter = alphabet[new_shift_position]
#         elif shift_position < 0:
#             print(f' Shift {shift_position}')
#             new_shift_position = len(alphabet) + shift_position
#             print(f' new Shift {new_shift_position}')
#             new_letter = alphabet[new_shift_position]
#         else:
#           new_letter = alphabet[shift_position]
#         cipher_text += new_letter
#      print(f'The is the encrptyed text {cipher_text}')

# if direction == 'decode':
#    decrpty(plain_text=text,shift_amount=shift_n)

# if direction == 'encode':
#    encrpty(plain_text=text,shift_amount=shift_n)



