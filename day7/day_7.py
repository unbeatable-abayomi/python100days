import random
HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
      |
      |
      |
      |
=========''']
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
end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
          lives -= 1
          print(HANGMANPICS[lives])
          print(f"You only have {lives} left")
    else:
        for p in range(len(chosen_word)):     
                if chosen_word[p] == guess:
                    outputs[p]=guess
    if lives == 0:
        end_of_game = True 
        print("You Lose")     
                
    print(outputs)
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
# if guess in chosen_word:
#     print(f"Yes {guess} is in the word {chosen_word}")

# else:
#     print(f"No {guess} is not the word {chosen_word}")





