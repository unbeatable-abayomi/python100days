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

