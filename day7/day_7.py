
import random,ascii

print(ascii.hangman)
chosen_word =random.choice(ascii.words_list)


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
end_of_game = False
lives = 6
trackguess = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in trackguess:
      print(f"You have already Chosen {guess}")
    elif guess not in chosen_word and guess not in outputs:
          lives -= 1
          print(ascii.HANGMANPICS[lives])
          print(f"You only have {lives} left")
          if guess not in chosen_word :
               print(f"Your {guess} guess is not in {chosen_word}")
    elif guess in outputs:
         print(f"You have already Chosen {guess}")
    else:
        for p in range(len(chosen_word)):     
                if chosen_word[p] == guess:
                    outputs[p]=guess
    trackguess += guess
    if lives == 0:
        end_of_game = True 
        print("You Lose")     
                
    print(outputs,"hell")

    if "_" not in outputs:
         end_of_game = True
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






