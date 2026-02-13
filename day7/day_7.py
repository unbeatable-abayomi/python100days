import random

r = random.randint(0,2) 

word_list = ["ardvark","baboon","camel"]

#chosen_word = random.choice(word_list)


chosen_word = word_list[r]

# print(chosen_word, guess)
outputs = []
for n in chosen_word:
    #outputs.append("_")
    outputs += "_"

print(outputs)
# while rr > 0: 
#      guess = input("Guess a letter: ").lower()
#      print(f'{rr} hello' )
#      for p in range(len(chosen_word)):
#          if chosen_word[p] == guess:
#              outputs[p]=guess
             
#      print(outputs)
#      rr -= 1
print(chosen_word)
is_game_end = False
while not is_game_end:
    guess = input("Guess a letter: ").lower()
    for p in range(len(chosen_word)):     
            if chosen_word[p] == guess:
                outputs[p]=guess
    print(outputs)
    if "_" not in outputs:
         is_game_end = True
print("You win")
# for p in range(len(chosen_word)):
#     if chosen_word[p] == guess:
      
#         outputs[p]=guess
    # else: 
      
    #     outputs[p]= '_'
# for index, letter in enumerate(chosen_word):
#     if letter == guess:
#         print(f"Yes {letter} {guess}")
#         outputs[index]=guess
#     else:
#         print (f"No {letter} {guess}")
#         outputs[index]= '_'
# if guess in chosen_word:
#     print(f"Yes {guess} is in the word {chosen_word}")

# else:
#     print(f"No {guess} is not the word {chosen_word}")





