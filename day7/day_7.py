import random

r = random.randint(0,2) 

word_list = ["ardvark","baboon","camel"]

#chosen_word = random.choice(word_list)


chosen_word = word_list[r]
guess = input("Guess a letter: ").lower()
print(chosen_word, guess)

for letter in chosen_word:
    if letter == guess:
        print(f"Yes {letter} {guess}")
    else:
        print (f"No {letter} {guess}")

if guess in chosen_word:
    print(f"Yes {guess} is in the word {chosen_word}")

else:
    print(f"No {guess} is not the word {chosen_word}")


