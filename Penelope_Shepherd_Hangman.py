import random

head=' ' #Although these variables do not have importance within the game itself, they allow the programmer to see where each body part is contained on the list
left = ' '
body = ' '
right= ' '

hangman = [                    # Create the box using arrays to form a picture of the hangman
        ['____________'],
        [' ','| ','       ','|'],
        [' ', head,'        ','|'],
        [left,body, right, '       ','|'],
        [' ',right,"",left ,'       ','|']
        ]

def hangman_printer(): # Creates a fuction that prints the variable hangman
    for i in range(len(hangman)):
        print('')
        for j in range(len(hangman[i])): # For the amount of lists in box, print the box and its corresponding number, then continue on
            print(hangman[i][j], end='')

hangman_printer() # print the hangman so the user can see what they are writing

def main():
    guessedletters=[] #Create a list to store the letters that the user has guessed
    word_list = ['banana','computer','keyboard','poster','jacket','tree','window'] #Creates a list of words for the computer to choose from
    word = random.choice(word_list) # Makes a random selection from the list of words
    wordguesser = list(word) # Turns the randomly selected word into a list, where each item is a letter of the word
    dashes = [] #Creates a list for dashes
    for char in wordguesser: # For every letter in the word, add a dash so that for each letter there is a dash
        dashes.append('—')
    dashes="".join(dashes)
    print('\n'+'\n'+dashes) 
    dashes= dashes.strip() #Strip the extra space out of dashes
    dashes = list(dashes) #Turn dashes back into a list
    counter = 0 #Set the counter to 0

    while True:
        round = 'lost' #Start the round as lost

        if '—' not in dashes: #Check if the player has won the game, if there is no more to be revealed then the game is won
            print("Congrats! You have won!")
            exit()

        guess=str.lower(input("Please type your letter guess.   ")) #Ask for a letter guess
        if len(guess) >= 2: #If the length of the guess is bigger then just one letter, ask the player to retype it
            print("Please only guess one letter.")
            round = 'bad' #Set the round as  bad so the loop will repeat without changing anything
        elif guess in guessedletters: #If the player has already guessed a certain letter, ask the player to type a new letter
            print("You have already guessed this letter.")
            round = 'bad' # Again, set the round as bad so the loop can repeat
        else:
            guessedletters.append(guess) # If the guess is a good guess, add it to our list of guessed letters
            for pos in range(len(wordguesser)): #Iterate through each letter in our word
                if guessedletters[counter] == wordguesser[pos]: #If the most recent guessed letter is equal to the letter then change the dashes to the guessed letter at that position
                    dashes[pos] = guessedletters[counter] 
                    round = 'won' #Set the round as 'won' so we do not add a part to the hangman
            print(dashes)
            
        if round == 'won': # If the round has been won, reapeat the loop and ask for a additional guess
            print("Nice guess!")
        elif round == 'bad':
            print("Please try again.")
            counter = counter - 1  # Because we add 1 to the counter every time we perform the hangman_printer, we remove one from the counter to compensate and prevent anything from changing as we iterate through the loop again
        else: #Inefficent way to see which parts are missing and if that part is missing, then add a part to it when the round was lost
            if hangman[2][1] != 'O': 
                hangman[2][1] = 'O'
            elif hangman[3][0] != '\\':
                hangman[3][0] = '\\'
            elif hangman[3][2] != '/':
                hangman[3][2] = '/'
            elif hangman[3][1] != '|':
                hangman[3][1] = '|'
            elif hangman[4][0] != '/':
                hangman[4][0] = '/'
            elif hangman[4][2] != '\\':
                hangman[4][2] = '\\'
                print("You have lost.") #If the last part has been added the game is lost
                hangman_printer() # Print the completed hangman one last time
                exit()

        hangman_printer() #Print the hangman so the player can see what it looks like
        print('\n') # Without this, the game will not go to the next line when its asks for the next input
        counter = counter + 1 #Add one to the counter so we can be at the most recent gussed letter

main()
                


