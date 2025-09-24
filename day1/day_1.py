print("Day 1 - Python Print Function" + "Abayomi")
print("The function is declared like this:")
print("print('what to print')")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
print("Hello \nworld")

name = input("What is your name ? ")
# print("Hello " + input("What is your name ? "))
newstring = name.strip()
print(len(newstring.replace(" ", "")))

# example
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in ?\n")
pet = input("What's your pet's name ?\n")
print("Your band name could be " + city  + " " + pet)
