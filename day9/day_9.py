import os
import platform

def clear_screen():
    # Detect the operating system
    if platform.system() == "Windows":
        os.system('cls')
    else:
        # This covers Linux (like your Ubuntu laptop) and macOS
        os.system('clear')

# Call the function to clear the screen
clear_screen()


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    123:12345
}


#Retrieving items from dictionary
print(programming_dictionary["Bug"],programming_dictionary[123])

#Adding new items to dictionary
programming_dictionary["error"] = "Syntax Error"


#Create an empty dictionary
empty_dictionary = {}
print(programming_dictionary["error"])
#Editing items in dictionary
programming_dictionary["error"] = "Runtime Error"
print(programming_dictionary["error"])
print(programming_dictionary)

#Wipe an existing  dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_results = {}
for score in student_scores:
   if student_scores[score] > 90 or student_scores[score] == 100:
       student_results[score]="Outstanding"
   elif student_scores[score] > 80 and student_scores[score] < 91:
       student_results[score]="Exceeds Expectations"
   elif student_scores[score] > 70 and student_scores[score] < 81:
    student_results[score]="Acceptable"
   elif student_scores[score] < 70:
       student_results[score]="Fail"

print(student_results)
student_grades = {}
for student in student_scores:
   score = student_scores[student]
   if score > 90:
      student_grades[student] = "Outstanding"
   elif score > 80:
      student_grades[student] = "Exceeds Expectations"
   elif score > 70: 
       student_grades[student] = "Acceptable"
   else:
      student_grades[student] = "Fail"

print(student_grades)


#Nesting dictionary inside of a dictionary
travel_log = {
   "France" : {"cities_visited":["Paris","Lille","Dijion"],"total_visits":12},
   "Germany" : {"cities_visited": ["Berlin","Hamburg","Stuggart"],"total_visits":5},
  # "Nigeria": {"LAGOS":200,"ABUJA":300,"JOS":400}

}


#Nesting dictionary inside of a list
travel_log2 = [
   {
      "country":"France",
      "cities_visited":["Paris","Lille","Dijion"],
      "total_visits":12
   },
   {
      "country":"Germany",
      "cities_visited": ["Berlin","Hamburg","Stuggart"],
      "total_visits":5
   },
]

def add_new_country(country2,lists_of_cities,visits):
#    travel_log2.append({'country':country2,"cities_visited":lists_of_cities,"total_visits":visits})
   # or
   new_country = {}
   new_country["country"] = country2
   new_country["cities_visited"] = lists_of_cities
   new_country["total_visits"] = visits
   travel_log2.append(new_country)

add_new_country("Brazil",['Sao Paulo','Rio de Janerio'],5)

print(f"I've been to {travel_log2[2]['country']} {travel_log2[2]['total_visits']} times...")

print(f"My favorite city was {travel_log2[2]['cities_visited'][0]}")

yes_keepbiding = True
allbiders ={}
def input_biders(name,bid):
    allbiders[name] = bid 

def do_bidder(allbiders):
   higest_bid = 0
   winner_name = ''
   for key,value in allbiders.items():
       #bid_amount = allbiders[bidder]
       if value > higest_bid:
          higest_bid = value
          winner_name = key
   print(f"The winner is {winner_name} and with the bid of ${higest_bid}")

      

while yes_keepbiding:
   name = input("Hi what is your name: ")
   bid_amount = int(input("Input bid amount $"))
   input_biders(name,bid_amount)

   tokeepbiding = input("Is there still any more bid: Yes or No")
   # if tokeepbiding == "yes":
   #  clear_screen()
   if tokeepbiding == "no":
      yes_keepbiding = False
      print("I will tell you a winner now")
      do_bidder(allbiders)
   elif tokeepbiding == "yes":
      clear_screen()
      

      
         

            
      






   

