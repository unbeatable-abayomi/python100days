import platform
import os
def clear_screen():
    # Detect the operating system
    if platform.system() == "Windows":
        os.system('cls')
    else:
        # This covers Linux (like your Ubuntu laptop) and macOS
        os.system('clear')

# Call the function to clear the screen
#clear_screen()

#prime checker day -- 8
# chiper day--8
# bidder game --day 9

alpheat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def chiper_check(direction,shift_amount,word):
#     end_text = ''
#     if direction == "decode":
#         shift_amount *= -1
#     for char in word:
#         if char in alpheat:
#             posistion = alpheat.index(char)
#             newposition = posistion + shift_amount
#             end_text += alpheat[newposition]
#         else:
#             end_text += char
#     print(f"The {direction}d text is {end_text}")

# to_keep_going = True

# while to_keep_going:

#      what_direction = input(f"Please what direction are you going encode or decode: ")
#      what_shift_amount = int(input("Please input the shift amount: "))
#      what_word = input("What is the word, to encode or decode: ")
#      what_shift_amount = what_shift_amount % 26
#      chiper_check(what_direction,what_shift_amount,what_word)

#      to_continue = input("Do you still want to continue")

#      if to_continue == "no":
#          to_continue = False
#          print("Byeeeeeeeeeeeee")



# new_number_to_check = int(input("What number do we check, Pls enter:"))

# def prime_checker(number_to_check):
#     is_prime = True
#     for num in range(2,number_to_check):
#         if number_to_check % num == 0:
#             is_prime = False

#     if is_prime:
#         print(f"The number {number_to_check} is a prime number")
#     else:
        
#         print(f"The number {number_to_check} is not a prime number")

# prime_checker(new_number_to_check)      

allbider ={}
def form_bidders_dictonary(name,bidamount):
    allbider[name] = bidamount
   
def get_higehest_bidder(bidders):
    highest_bidder = 0
    winner = ''
    for bid in bidders:
        bidammount = bidders[bid]

        if bidammount > highest_bidder:
            highest_bidder = bidammount
            winner = bid
    print(f"The winner is {winner} with the bid ${highest_bidder}, Byyyeeeee")

to_keep_bidding = True

while to_keep_bidding:
    bidders_name = input("Pls input bidders name: ")
    bidders_amount = int(input("Pls input the amount to bid $: "))
    form_bidders_dictonary(bidders_name,bidders_amount)
    to_keep_adding = input("Would you still like to add bidders, yes or no: ")
    if to_keep_adding == "no":
        to_keep_bidding = False
        get_higehest_bidder(allbider)

    elif to_keep_adding == "yes":
        clear_screen()    
# def chiper_check (direction,shift_am,word):
#      endtext = ""
#      if direction == "decode":
#           shift_am *= -1
     
#      for char in word:
#           if char in alpheat:
#                position = alpheat.index(char)
#                new_posi = position + shift_am
#                endtext += alpheat[new_posi]
#           else:
#                endtext += char

#      print(f"The {direction}d text is {endtext}")

# allways = True

# while allways:
#      dm = input("Input direation")
#      shif = int(input("Input Shift amount"))
#      wordss= input("word")
#      shif = shif % 26
#      chiper_check(dm,shif,wordss)

#      cn = input("How yow want continw")
#      if cn == "no":
#           allways = False
#           print("Byyyyyyyy")









# def function_chip(dd,ss,ww):
#      end_text = ''
#      if dd == "decode":
#           ss *= -1
#      for char in ww:
#           if char in alpheat:
#              position = alpheat.index(char)
#              new_postion = position + ss
#              end_text += alpheat[new_postion]
#           else:
#                end_text += char

# lestkeepthelop = True
# while lestkeepthelop:
#     dirc = input("decode or encode")
#     shift_nm = int(input("What is the shift number"))
#     word_to = input("What word")

#     shift_nm = shift_nm % 26

#     function_chip(dirc,shift_nm,word_to)

#     based_on = input("Do we continue. yes or no")
#     if based_on == "no":
#          lestkeepthelop = False
#          print("Byyyyyyyyeeeee")




# def chiper_check(direction,shift_num,word):
#     all_text = ""
#     if direction == "decode":
#          shift_num *= -1

#     for char in word:
#         if char in alpheat:
#             posistion = alpheat.index(char)
#             new_posistion = posistion + shift_num
#             all_text += alpheat[new_posistion]
#         else:
#             all_text += char

#     print(f"The {direction}d text is {all_text}")

# should_continue = True
# while should_continue:
#       sh = int(input("What is the shift amount: "))
#       dr = input("Which directtion: ")
#       wd = input("Which word: ")      
#       shh = sh % 26
#       chiper_check(dr,shh,wd)

#       result = input("COntinue Yes or NO")

#       if result.lower() == "no":
#            should_continue = False
#            print("ByeBye")
   


