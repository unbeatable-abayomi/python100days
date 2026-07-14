#prime checker


# def prime_checker(number):
#    is_prime = True
#    for num in range(2,number):
#       if number % num == 0:
#          is_prime = False

#    if is_prime:
#       print(f"This number {number} is a prime")
#    else:

#       print(f"This number {number} is not a prime")

alpheat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


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
   