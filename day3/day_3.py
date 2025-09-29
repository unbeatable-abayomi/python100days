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

age = int(input("Enter your age:"))

if height >= 120:
   if age >= 19:
      print(f"You will pay normal price")
   else:
      print(f"You will pay have a discount price")
else:
 print("Not eligible to ride")