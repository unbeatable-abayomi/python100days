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
      print(f"Your final bill is ${bill}")
   #    print(f"Your final bill is ${bill}")
   # else:
   print(f"Your final bill is ${bill}")

 
else:
 print("Not eligible to ride")

lets_in = input("Enter your the year: ")

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
    
     # second way of solving the problem  

if int(lets_in) % 4 == 0:
    if int(lets_in) % 100 == 0:
     if int(lets_in) % 400 == 0:
        print(f"{lets_in} is a leap year 2")
     else:
        print(f"{lets_in} is not a leap year 2")
    else:
     print(f"{lets_in} is a leap year 2")
else:
   print(f"{lets_in} is not a leap year 2")



pizza_size = input("Select Pizza S,M and L")
pay = 0
extra = ""
extrachees = ""
if pizza_size == "S":
     pay += 15
     extra = input(" Prepperoin Y and N")
     if extra == "Y":
      pay += 2
     extrachees = input("Extra chess Y and N")
     if extrachees == "Y":
      pay += 1
if pizza_size == "M":
    pay += 20
    extra = input(" Prepperoin Y and N")
    if extra == "Y":
      pay += 3
    extrachees = input(f"Y and N")
    if extrachees == "Y":
      pay += 1 
if pizza_size == "L":
    pay += 25
    extra = input(" Prepperoin Y and N")
    if extra == "Y":
      pay += 3
    extrachees = input(f"Y and N")
    if extrachees == "Y":
      pay += 1
      
      
      
print(f"final pay id {pay}")
    