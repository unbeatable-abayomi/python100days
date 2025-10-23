# /bin/python3

# Loops
import random

mynumber = input("give me numbers you want in an array ")

print(mynumber.split(","))

splitted_mynumber = mynumber.split(",")

print(splitted_mynumber)

for n in range(0, len(splitted_mynumber)):
    splitted_mynumber[n] = int(splitted_mynumber[n])
    
print(splitted_mynumber , "after converting to int", type(splitted_mynumber[0]))

all_splitted_mynumber = 0
number_of_elements = 0
sum_of_elements = 0
container_var = 0
highest_value = splitted_mynumber[0]

print(number_of_elements, "first")
print(highest_value, "firstdd")

for x in splitted_mynumber:
    print(f"{x} is in the array")
    number_of_elements += 1
    sum_of_elements += x
    # container_var = x
    if x > highest_value:
      highest_value = x



print(f"{highest_value} is the highest")
print(number_of_elements, "second")
print(round(sum_of_elements/number_of_elements), "second method")

for n in range(0, len(splitted_mynumber)):
    all_splitted_mynumber += int(splitted_mynumber[n])
    
print(all_splitted_mynumber,len(splitted_mynumber))
print(all_splitted_mynumber/len(splitted_mynumber))
print(round(all_splitted_mynumber/len(splitted_mynumber)))


alleven = 0

for i in range(0,101):
    if i % 2 == 0:
      print(i,"first")
      alleven += i
print(alleven)

alleven2 = 0
for i in range(0,101,2):
      print(i,"second")
      alleven2 += i
print(alleven2)

# Fizzbuzz problem
for num in range (1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizzbuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
      print(num) 



print("My password Gen")

allalphas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
 "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
allspecial = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?"]

allnumber = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# passwordLenght = int(input("How many character do you want in your password"))
countOfLetter = int(input("How many letters do you want in your password : "))
countOfSpecial = int(input("How many Special character do you want in your password : "))
countOfnumbers = int(input("How many Numbers do you want in your password : "))

passwordGenerated = '' #Change to array/list
for pl in range(1, countOfLetter+1):
    # Instead try random.choice(allalphas) here it's a one liner with the append function
    selectedLetter = random.randint(0,len(allalphas)-1)
    passwordGenerated += allalphas[selectedLetter]
for pl in range(1, countOfSpecial+1):
    selectedSpecial = random.randint(0,len(allspecial)-1)
    passwordGenerated += allspecial[selectedSpecial]
for pl in range(1, countOfnumbers+1):
    selectedNumber = random.randint(0,len(allnumber)-1)
    passwordGenerated += allnumber[selectedNumber]
    
print(f" Here is your password {passwordGenerated}")

randomizedPassword = ''.join(random.sample(passwordGenerated, len(passwordGenerated)))