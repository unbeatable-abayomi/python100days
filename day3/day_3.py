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
print("Welcome to the rollercoaster!")
height = int(input("Enter your height: " ))

bill = 0
five_dollar_bill = 5
seven_dollar_bill = 7
tewelve_dollar_bill = 12
if height >= 120:
   age = int(input("Enter your age:"))
   if age < 12:
      print(f"You will pay ${five_dollar_bill} ")
      bill += five_dollar_bill
   elif age <= 18:
      print(f"You will pay ${seven_dollar_bill} ")
      bill += seven_dollar_bill
   else:
      print(f"You will pay ${tewelve_dollar_bill} ")
      bill += tewelve_dollar_bill
   response = input("Do you want a photo taken? Y or N: ")
   if response == "Y":
      print("You will pay an extra $3")
      bill += 3
   #    print(f"Your final bill is ${bill}")
   # else:
   print(f"Your final bill is ${bill}")

 
else:
 print("Not eligible to ride")

lets_in = input("Enter your name: ")

last_two_chars = lets_in[-2:]
print(last_two_chars, type(last_two_chars))
if last_two_chars == "00":
    if int(lets_in) % 4 == 0 and int(lets_in) % 400 == 0 :
       print(f"{lets_in} is a leap year")
    else:
         print(f"{lets_in} is not a leap year")
elif int(lets_in) % 4 == 0:
    print(f"{lets_in} is a leap year")
else:
    print(f"{lets_in} is not a leap year")
       
    