import random

r = random.randint(0,2) 

word_list = ["ardvark","baboon","camel"]

#chosen_word = random.choice(word_list)


chosen_word = word_list[r]
guess = input("Guess a letter: ").lower()
print(chosen_word, guess)
outputs = []
for n in chosen_word:
    outputs.append("_")

print(outputs)


for p in range(len(chosen_word)):
    if chosen_word[p] == guess:
      
        outputs[p]=guess
    # else: 
      
    #     outputs[p]= '_'
# for index, letter in enumerate(chosen_word):
#     if letter == guess:
#         print(f"Yes {letter} {guess}")
#         outputs[index]=guess
#     else:
#         print (f"No {letter} {guess}")
#         outputs[index]= '_'

print(outputs)
# if guess in chosen_word:
#     print(f"Yes {guess} is in the word {chosen_word}")

# else:
#     print(f"No {guess} is not the word {chosen_word}")





