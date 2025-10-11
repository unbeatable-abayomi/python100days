#Randomization and Python Lists
["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

print("Welcome to Treasure Island Your Mission is to find the treasure")
stand_1 = input("Where would you like to go L or R")
stand_2 = ""
stand_3 = ""
# stand_4 = ""
if stand_1 == "L":
   stand_2 = input("Good, Go ahead, What is your next move S or W, swim or wait")
   if stand_2 == "W":
       stand_3 = input("Good, Go ahead, What is your next move which color Red,Yellow,or Blue, R ,Y or,B")
       if stand_3 == "Y":
           print("You Win")
       elif stand_3 == "R" or stand_3 == "B":
           print("Game Over")
   else:
       print("It's game over")
       
   
else:
   print("It's game over")
