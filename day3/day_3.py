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
      bill += five_dollar_bill
      print(f"You will pay ${bill} ")
      
   elif age <= 18 :
      bill += seven_dollar_bill
      print(f"You will pay ${bill} ")
   
   elif age >= 45 and age <= 55 :
      print(f"You will pay ${bill}, it is free for you")

   else:
      bill += tewelve_dollar_bill
      print(f"You will pay ${bill} ")
      
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

my_man_name = input("Enter 1st name: ")
my_female_name = input("Enter 2nd name: ")
t_count = "t"
r_count = "r"
u_count = "u"
e_count = "e"
l_count = "l"
o_count = "o"
v_count = "v"
# e_count = "e"
fullname = my_man_name.lower() + my_female_name.lower()
t_occurs = fullname.count(t_count)
r_occurs = fullname.count(r_count)
u_occurs = fullname.count(u_count)
e_occurs = fullname.count(e_count)

l_occurs = fullname.count(l_count)
o_occurs = fullname.count(o_count)
v_occurs = fullname.count(v_count)
# e_occurs_2 = e_occurs


print(f"The character '{t_count}' appears {t_occurs}")
print(f"The character '{r_count}' appears {r_occurs}")
print(f"The character '{u_count}' appears {u_occurs}")
print(f"The character '{e_count}' appears {e_occurs}")

print(f"The character '{l_count}' appears {l_occurs}")
print(f"The character '{o_count}' appears {o_occurs}")
print(f"The character '{v_count}' appears {v_occurs}")
print(f"The character '{e_count}' appears {e_occurs}")

print(f"{t_occurs+r_occurs+u_occurs+e_occurs}{l_occurs+o_occurs+v_occurs+e_occurs} %")

love_score = int(f"{t_occurs+r_occurs+u_occurs+e_occurs}{l_occurs+o_occurs+v_occurs+e_occurs}")
if (love_score < 10) or (love_score > 90):
        print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
        print(f"Your score is {love_score}, you are alright together.")
else:
        print(f"Your score is {love_score}.")



# Rolacoster challange


print("Welcome to Treasure Island Your Mission is to find the treasure")
stand_1 = input("Where would you like to go L or R")
# stand_2 = ""
# stand_3 = ""
# stand_4 = ""
if stand_1.upper() == "L":
   stand_2 = input("Good, Go ahead, What is your next move S or W, swim or wait")
   if stand_2.upper() == "W":
       stand_3 = input("Good, Go ahead, What is your next move which color Red,Yellow,or Blue, R ,Y or,B")
       if stand_3.upper() == "Y":
           print("You Win")
       elif stand_3.upper() == "R" or stand_3.upper() == "B":
           print("Game Over")
   else:
       print("It's game over")
       
   
else:
   print("It's game over")