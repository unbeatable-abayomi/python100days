#Randomization and Python Lists
import random
my_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

r = random.randint(0,1) 
if r == 1:
  print("Heads")
else:
  print("Tails")

print(r, my_states.__len__(), len(my_states)-1)
family_name = ["yomi", "tolu", "deji", "bayo", "simi"]

print(family_name)
family_name[len(family_name):] = "ola"
# family_name.append("ola")
print(family_name)





names = input("give me names of your friends: ")

print(names.split(","))

splitted_name = names.split(",")


my_randon_num = random.randint(0,len(splitted_name)-1)

# random.choice(splitted_name)
print(my_randon_num)

print(f"{splitted_name[my_randon_num]} is going to pay for the dinner")


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = fruits + vegetables

dirty_dozen_2 = [*fruits, *vegetables]
# dirty_dozen_2 = [fruits, vegetables]
print(dirty_dozen_2)
print(dirty_dozen_2[0][0])




row1 = ["*","*","*"]
row2 = ["*","*","*"]
row3 = ["*","*","*"]

all_roget = [row1, row2, row3]

print(f'{row1}\n{row2}\n{row3}')

postion_want = input("Enter postion: ")
lastnumber = int(postion_want[1])
firstnumber = int(postion_want[0])

all_roget[lastnumber-1][firstnumber-1] = "X"


print(f'{row1}\n{row2}\n{row3}')

choice_number = int(input("Input your Chioce"))

computer_chioce = random.randint(0,2)

rock = 0
paper = 1  
scissors = 2

if choice_number == 0:
    if computer_chioce == 2:
        print(f"You won Your choice {choice_number} Computer Choice {computer_chioce} ")
    elif computer_chioce == 1:
        print(f"You Lose Your choice {choice_number} Computer Choice {computer_chioce}")
    elif computer_chioce == 0:
        print(f"You Draw Your choice {choice_number} Computer Choice {computer_chioce}")
elif choice_number == 1:
    if computer_chioce == 0:
        print(f"You won Your choice {choice_number} Computer Choice {computer_chioce}")
    elif computer_chioce == 2:
        print(f"You Lose Your choice {choice_number} Computer Choice {computer_chioce}")
    elif computer_chioce == 1:
        print(f"You Draw Your choice {choice_number} Computer Choice {computer_chioce}")
elif choice_number == 2:
    if computer_chioce == 1:
        print(f"You won Your choice {choice_number} Computer Choice {computer_chioce}")
    elif computer_chioce == 0:
        print(f"You Lose Your choice {choice_number} Computer Choice {computer_chioce}")
    elif computer_chioce == 2:
        print(f"You Draw Your choice {choice_number} Computer Choice {computer_chioce}")
else:
    print("Invalid Input, You Lose")

# Make sure too write an alternative to above code

# if you want to use the emoji in your code
# https://www.webfx.com/tools/emoji-cheat-sheet/