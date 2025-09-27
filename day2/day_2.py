# day 2 

import sys

print(sys.version.split()[0])

age = 20
print("Hello"[0])

print(f"I am {age} years old."[1])
print(type(123_456_789))

number = input("Type a two digit number:\n")
print(int(number[0]) + int(number[1]))

# PEMDASLR
# Parentheses ()
# Exponents **
# Multiplication * Division /
# Addition + Subtraction -


print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)


height = input("What is your height in m? :")

weight = input("What is your weight in kg? :")
  
# result  = ( int(weight) /(float(height) * float(height)))
bmi_as_float = ( int(weight) /(float(height) ** 2))
print(int(bmi_as_float),type(bmi_as_float),bmi_as_float)