# Control flow and logical operators

# age_max = int(input("What is your age? :"))

# if age_max >= 18:
#     print("You are old enough to drink alcohol")
# else:
#     print("You are not old enough to drink alcohol")

# num = int(input("Enter your number : "))

# if num % 2 == 0:
#   print(f"{num} is a an even number")
# else:
#  print(f"{num} is a an odd number")

height = int(input("Enter your height: " ))



if height >= 120:
   age = int(input("Enter your age:"))
   if age < 12:
      print(f"You will pay discount price")
   elif age >= 12 and age <= 18:
      print(f"You will pay half price")
   else:
      print(f"You have no discount price")
else:
 print("Not eligible to ride")