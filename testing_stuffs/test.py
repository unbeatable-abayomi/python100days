#prime checker

alpheat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def function_chip(dd,ss,ww):
     end_text = ''
     if dd == "decode":
          ss *= -1
     for char in ww:
          if char in alpheat:
             position = alpheat.index(char)
             new_postion = position + ss
             end_text += alpheat[new_postion]
          else:
               end_text += char

lestkeepthelop = True
while lestkeepthelop:
    dirc = input("decode or encode")
    shift_nm = int(input("What is the shift number"))
    word_to = input("What word")

    shift_nm = shift_nm % 26

    function_chip(dirc,shift_nm,word_to)

    based_on = input("Do we continue. yes or no")
    if based_on == "no":
         lestkeepthelop = False
         print("Byyyyyyyyeeeee")



# def prime_checker(number):
#    is_prime = True
#    for num in range(2,number):
#       if number % num == 0:
#          is_prime = False

#    if is_prime:
#       print(f"This number {number} is a prime")
#    else:

#       print(f"This number {number} is not a prime")




# check_num = int(input("input your number"))

# prime_checker(check_num)

def chiper_check(direction,shift_num,word):
    all_text = ""
    if direction == "decode":
         shift_num *= -1

    for char in word:
        if char in alpheat:
            posistion = alpheat.index(char)
            new_posistion = posistion + shift_num
            all_text += alpheat[new_posistion]
        else:
            all_text += char

    print(f"The {direction}d text is {all_text}")

should_continue = True
while should_continue:
      sh = int(input("What is the shift amount: "))
      dr = input("Which directtion: ")
      wd = input("Which word: ")      
      shh = sh % 26
      chiper_check(dr,shh,wd)

      result = input("COntinue Yes or NO")

      if result.lower() == "no":
           should_continue = False
           print("ByeBye")
   


