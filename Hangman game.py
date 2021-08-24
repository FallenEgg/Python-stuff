import random
from collections import Counter

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon 
coconut watermelon cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
#randomly choose a secret word from our "someWords" LIST
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        #For printing the empty spaces for letters of the word
        print('_', end = ' ')
    print()

    playing = True
    #list for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0 ) and flag == 0: #update flag
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            #If letter is guessed correctly
            if guess in word:
                k = word.count(guess) #k stores the number of times the guessed letter occurs in the word
                for _ in range(k):
                    letterGuessed += guess #the guess letter is added as many times as it occurs
            
            #Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end = ' ')
                    correct += 1
                
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", end = ' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!!!')
                    break
                    break
                else: 
                    print('_', end = ' ')

        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
