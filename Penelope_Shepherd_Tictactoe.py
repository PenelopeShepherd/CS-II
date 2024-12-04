import time
import random
mistakes = 0
if mistakes < 3: # Unfinished feature to allow the user to only make a certain number of mistakes, not fully implemented and defective. Does not interfere with the function of the code
    game = True
while game == True:
    print("Welcome to Tic Tac Toe!")
    box = [                    # Create the box using arrays
        [' ',' A',' B',' C'],
        ['A','AA','BA','CA'],
        ['B','AB','BB','CB'],
        ['C', 'AC','BC','CC'] 
        ]
    def make_box(mark,player): 
        '''
        Play tic tac toe and check through the box to place the X's and O's
        Args: 
        mark (str): The current mark that is going to be placed onto the board
        player (str): The current player who is taking a turn

        returns:
        mark (str): The original mark
        box: Prints the box with the tic tac toe mark in it
        '''
        choice = str((input(player+" "+"Please choose a spot to place your pawn" + '. (format: (ColumnLetter)(RowLetter). Ex: "AA"')).upper()) # Asks the player where they want to place thier mark
        if choice == 'AA' or choice == 'BA' or choice == 'CA' or choice == 'AB' or choice == 'BB' or choice == 'CB' or choice == 'AC' or choice == 'BC'or choice == 'CC': # Check that the user input a valid input
            for i in range(len(box)): # For the amount of lists in the list of lists, print a new line
                if i != 0: # I do not want the dashed line before the first row is printed, this prevents that
                    print('\n'+'     -------------------') # Decorative line to seperate the rows
                else:
                    print('\n') # Again, I do not want the dashed line before the first row is printed, so this prints a blank line there

                for j in range(len(box[i])): # For the amount of lists in box, print the box and its corresponding number, then continue on
                    if box[i][j] == choice: # If the number that I am printing is equal to choice of the current player
                        if mark == "X":
                            box[i][j] = ' X' # Change this item of the list into the mark
                            print(box[i][j], end='     ')
                        elif mark == "O": # If the number that I am printing is equal to choice of the current player
                            box[i][j]= " O" # Change this item of the list into the mark
                            print(box[i][j], end='     ') 
                    elif box[i][j] == 'X' or box[i][j] == 'O': # If the spot is already taken by a mark
                        if mark == 'X': # Prevent the later code from switching around the marks and player because we need to repeat this function again for this player
                             mark = 'O'
                        elif mark == 'O':
                            mark = 'X'
                        if player == 'player one':
                            player = 'player two'
                        elif player == 'player two':
                            player = 'player one'
                        return mark # Leave the function so it can repeat and ask the user again
                    else:
                        print(box[i][j], end='     ') # Print the the number and then a space
                print()
            for j in range(len(box)): # If an entire row is equal to a mark, then that mark—and its corresponding player—has won the game
                if str.strip(box[j][1]) == mark and str.strip(box[j][2]) == mark and str.strip(box[j][3]) == mark: # Check through each row to see if they are equal to the mark
                    print(player+" has won")
                    time.sleep(5)
                    exit()
            for i in range(len(box)): # If an entire column is equal to a mark, then that mark—and its corresponding player—has won the game
                if str.strip(box[1][i]) == mark and str.strip(box[2][i]) == mark and str.strip(box[3][i]) == mark:  # Check through each column to see if they are equal to the mark
                    print(player+" has won")
                    time.sleep(5)
                    exit()
            if str.strip(box[1][1]) == mark and str.strip(box[2][2]) == mark and str.strip(box[3][3]) == mark: # If the first diagonal is equal to the mark the coressponding player has won
                print(player+" has won. The game will now close.")
                time.sleep(5)
                exit()
            elif str.strip(box[1][3]) == mark and str.strip(box[2][2]) == mark and str.strip(box[3][1]) == mark:  # If the second diagonal is equal to the mark the coressponding player has won
                print(player+" has won. The game will now close.")
                time.sleep(5)
                exit()
            elif str.strip(box[1][3])
        else:
            if mark == 'X':  # Prevent the later code from switching around the marks and player because we need to repeat this function again for this player
                mark = 'O'
            elif mark == 'O':
                mark = 'X'
            if player == 'player one':
                player = 'player two'
            elif player == 'player two':
                player = 'player one'
            return mark
    player='user1'
    def determine_player(mistakes):
        '''
        Play tic tac toe and check through the box to place the X's and O's

        args:
        mistakes (int): Again a remenant of this non-imported feature
        
        returns:
        player: "The name of the selected player
        '''
        while True:
            coin_flip_choice = input("Type 1 to pick 1st player with a coin flip, type 2 to choose yourself")
            if coin_flip_choice == '1' or coin_flip_choice == '2':
                False
                if coin_flip_choice == '1':
                    print("User of this machine, would you like to be heads or tails?")
                    it_doesnt_actually_matter = input("type heads or tails") # I left this part, it does not actually matter what you type because the integer will always pick the winner. This gives the illusion of choice
                        player = 'user1'
                        return player,mistakes
                    elif z == 2:
                        print("Other person(User2), you won! You will go first")
                        player = "user2"
                        return player,mistakes
                elif coin_flip_choice == '2':
                    print("Now pass the computer to player 1") # Ask player 1 to pick X or O
                    player = 'user1'
                    return player,mistakes
            else:
                mistakes += 1
                print('Type 1 OR 2. ex: "1"')
                if mistakes == 3:
                    print("You have made 3 mistakes. You don't get any re-try's anymore. Try harder to follow instuctions next time :)")
                    time.sleep(2) # Wait for 5 seconds
                    print("This program will now cease")
                    time.sleep(2) # Wait for 5 seconds
                    exit() # Quit the program
    
    determine_player(mistakes)
    while True:
        mark = str((input(player +" "+ "would you like to be X or O?")).upper())
        if mark == "X" or mark == "O": 
            print("Player 1 has selcted" + " " +mark)
            if mark == "X":
                print("Player 2, you will be 'O'")
                mark = "X"
                break
            elif mark == "O":
                mark = "O"
                print("Player 2, you will be 'X'")
                break
        else:
            print("Please type X or O")
            mistakes += 1
            if mistakes == 3:
                print("You have made 3 mistakes. You don't get any re-try's anymore. Try harder to follow instuctions next time :)")
                time.sleep(2) # Wait for 5 seconds
                print("This program will now cease")
                time.sleep(2) # Wait for 5 seconds
                exit() # Quit the program   
                break
    for i in range(len(box)):
        if i != 0:
            print('\n'+'     -------------------')
        else:
            print('\n')

        for j in range(len(box[i])):
                print(box[i][j], end='     ') # Print the the number and then a space
        print()
    while True:
        player = "player one"
        make_box(mark,player)
        if mark == 'X':
            mark = 'O'
        elif mark == 'O':
            mark = 'X'
        if player == 'player one':
            player = 'player two'
        elif player == 'player two':
            player = 'player one'


