import time
import random
mistakes = 0
if mistakes < 3:
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
        choice = str((input(player+" "+"Please choose a spot to place your pawn" + '. (format: (ColumnLetter)(RowLetter). Ex: "AA"')).upper())
        if choice == 'AA' or choice == 'BA' or choice == 'CA' or choice == 'AB' or choice == 'BB' or choice == 'CB' or choice == 'AC' or choice == 'BC'or choice == 'CC':
            for i in range(len(box)):
                if i != 0:
                    print('\n'+'     -------------------')
                else:
                    print('\n')

                for j in range(len(box[i])): # For the amount of lists in box, print the box and its corresponding number, then continue on
                    if box[i][j] == choice:
                        if mark == "X":
                            box[i][j] = ' X'
                            print(box[i][j], end='     ')
                        elif mark == "O":
                            box[i][j]= " O"
                            print(box[i][j], end='     ')
                    elif box[i][j] == 'X' or box[i][j] == 'O':
                        if mark == 'X':
                             mark = 'O'
                        elif mark == 'O':
                            mark = 'X'
                        if player == 'player one':
                            player = 'player two'
                        elif player == 'player two':
                            player = 'player one'
                        return mark
                    else:
                        print(box[i][j], end='     ') # Print the the number and then a space
                print()
            for j in range(len(box)):
                    if str.strip(box[j][1]) == mark and str.strip(box[j][2]) == mark and str.strip(box[j][3]) == mark:
                        print(player+" has won")
                        time.sleep(5)
                        exit()
            if str.strip(box[1][1]) == mark and str.strip(box[2][2]) == mark and str.strip(box[3][3]) == mark:
                print(player+" has won. The game will now close.")
                time.sleep(5)
                exit()
            elif str.strip(box[1][3]) == mark and str.strip(box[2][2]) == mark and str.strip(box[3][1]) == mark:
                print(player+" has won. The game will now close.")
                time.sleep(5)
                exit()
        else:
            if mark == 'X':
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
        while True:
            coin_flip_choice = input("Type 1 to pick 1st player with a coin flip, type 2 to choose yourself")
            if coin_flip_choice == '1' or coin_flip_choice == '2':
                False
                if coin_flip_choice == '1':
                    print("User of this machine, would you like to be heads or tails?")
                    it_doesnt_actually_matter = input("type heads or tails.")
                    z = random.randint(1,2)
                    if z == 1:
                        print("User(User1), you won! You will go first.")
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


