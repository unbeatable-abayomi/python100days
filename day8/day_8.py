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
          if number % i == 0:
            is_prime = False
     if is_prime :
          print(f"{number} is a prime number")
     else:
           print(f"{number} is not a prime number")


prime_checker(check_number)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# direction = input("Type 'encode' or 'decode' to do either").lower()

text = input("Type the text that you want to either encode or decode: ").lower()

shift_n = int(input("input shift: "))

def encrpty (plain_text, shift_amount):
     cipher_text = ''
     for letter in plain_text:
        position=alphabet.index(letter)
        shift_position = position + shift_amount
        print(f'shift post {shift_position} and lenfgt {len(alphabet)}')
        if shift_position >= len(alphabet):
            new_shift_position = shift_position - len(alphabet)
            new_letter = alphabet[new_shift_position]
        else:
          new_letter = alphabet[shift_position]
        cipher_text += new_letter
     print(f'The is the encrptyed text {cipher_text}')



encrpty(plain_text=text,shift_amount=shift_n)