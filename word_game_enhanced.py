#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

# Generate a list of 100 words
candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDED', 'YONDER']

attempts = [5, 4, 3]

while True:
    
    # ask the user to choose a level
    level = input("Choose a level (1 - Easy, 2 - Medium, or 3 - Hard): ")
    
    # select a random word from the chosen level
    if level == '1':
        word = random.choice(candidateWords)
        attempts = attempts[0]
    elif level == '2':
        word = random.choice(candidateWords)
        attempts = attempts[1]
    elif level == '3':
        word = random.choice(candidateWords)
        attempts = attempts[2]
    else:
        print("Invalid choice. Please choose a level between 1 and 3.")
        continue

    # Randomly select 8 words from the list
    password_list = random.sample(candidateWords, 8)

    # Randomly select one of the 8 passwords as the correct answer
    answer = random.choice(password_list)

    # Welcome the user to the game
    print("Welcome to the Word Game! You must identify a randomly selected password from a list of 8 words.")

    # Print the list of passwords for the user to see
    print("Here are the 8 passwords:")
    for index, item in enumerate(password_list):
        print(f"{index+1}: {item}")


    # Loop through each attempt
    for i in range(attempts):

        guess = input("Enter your guess: ")

        if guess == answer:
            print("You Won!")
            break
        else:
            matching_chars =  sum([1 for i in range(len(answer)) if answer[i] == guess[i]])

    # Loop for adding the matched characters
            for index, item in enumerate(password_list):
                if guess in item:
                    df = f"{index+1}: {item} [" + str(matching_chars) + "/6] correct"
                    print(df)
                else:
                    print(f"{index+1}: {item}")

            attempts = attempts - 1
            print("\n" + str(attempts) + " attempts remaining")

