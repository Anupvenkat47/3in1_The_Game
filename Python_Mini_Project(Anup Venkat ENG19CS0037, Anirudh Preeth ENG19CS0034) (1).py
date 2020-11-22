#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from random import randint
            
def the_3in1_game():
    #This part of the program is done by Anup venkat(ENG19CS0037)
    #This part of the program starts the interface and the main menu
    print("Hello and welcome to 3in1:The game, well you came to this game because you where bored to core while doing you work or assignment or that very long project that you have to do in 2 days\n Whatever the case maybe you came to the right game to pass your time ;)\n You will be playing with our simple AI named Briann\n")
    print("Oh, I just realised that me and my friend have not introdued to you, My name is Anup venkat who has created this program and where as this good friend of mine is called Anirudh Preeth who helped me with some code formatting and spelling.\n")
    name=input(print("Well this is awkward, we forgot to ask your name\n What's your name? "))
    game=input(print("Now then let's select a game you what to play:\n 1.Hangman\n 2.Rock,Paper,Scissors\n 3.TIC-TAC-TOE\n 4.Exit :(\n What's your choose? (1-4)"))
    #Here depending on the user input, the game function is defined and is excuted                 
    if game=='1':
        def hangman(name):
            #This part of the program is done by Anup venkat(ENG19CS0037)
            import random
            user=0
            mode = input("You are about to play Hangman:\n Play\n exit:\n(Type your option)")
            #Asking the user for input to start the game
            if (mode=="exit"):
                main_menu(name)
            else:
                print("Good Luck ! ", name)
            words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'roads', 'movies']
            word = random.choice(words)
            print("Guess the characters")
            guesses = ''
            turns = 12
            #conditions are checked in order to count the number of wrong letters (if any) or right one and accordingly trigger the remaining guesses function
            while turns > 0:
                failed = 0
                for char in word:
                    if char in guesses: 
                        print(char)
                    else:
                        print("_")
                        failed += 1
                if failed == 0:
                    print("You Win")
                    print("The word is: ", word)
                    replay=input(print("That was a good game, want to try that again:\n (y/n)\n"))
                    #Asking user if they want to play again after winning the game
                    if replay == 'y':
                        hangman(name)
                    else:
                        main_menu(name)
                        quit()
                        break
                guess = input("guess a character:") 
                guesses += guess
                if guess not in word:
                    turns -= 1
                    print("Wrong")
                    print("You have", + turns, 'more guesses')
                    if turns == 0:
                        print("You Loose")
                        print("The word is: ", word)
                        replay=input(print("I belive you can win this game, want to try that again:\n (y/n)\n"))
                        #Asking user if they want to play again after lossing the game
                        if replay == 'y':
                            hangman(name)
                        else:
                            main_menu(name)
                    
        hangman(name)
    elif game=='2':
        def rockpaperscissors(name):
            #This part of the program is done by Anup venkat(ENG19CS0037)
            t = ["Rock", "Paper", "Scissors"]
            computer = t[randint(0,2)]
            player = False
            user=0
            AI=0
            print("WARNING: THE INPUT IS CASE-SENSITIVE SO INPUT YOU CHOICE CAREFULLY!!")
            print("All the best, ", name)
            while player == False:
                player = input("Enter the Option:\nRock, Paper, Scissors?\nTo exit the program type 'exit'\nTo see your Score type 'Score'\n")
                #Asking user to input there operation for the function to decide what to do.
                        #The following if-else condition checkes for the user input and determines the if the user or the computer has won the game and accordingly increase there score respectively.
                if player == computer:
                    print("Tie!")
                elif player == "Rock":
                    if computer == "Paper":
                        print("You lose!", computer, "covers", player)
                        AI=AI+1
                    else:
                        print("You win!", player, "smashes", computer)
                        user=user+1
                elif player == "Paper":
                    if computer == "Scissors":
                        print("You lose!", computer, "cut", player)
                        AI=AI+1
                    else:
                        print("You win!", player, "covers", computer)
                        user=user+1
                elif player == "Scissors":
                    if computer == "Rock":
                        print("You lose...", computer, "smashes", player)
                        AI=AI+1
                    else:
                        print("You win!", player, "cut", computer)
                        user=user+1
                elif player == "exit":
                    #This elif condition checkes if the the score of the user is higher than computer or AI accordingly gives a response to the user
                        if user>AI :
                            print("Well, you defeted our AI, Brian, Good Job")
                            main_menu(name)
                        elif user<AI :
                            print("Well that sucks, our AI, Brian, just made you lose in this game")
                            main_menu(name)
                        else:
                            print("You have the same luck as a robot, we do not know if this is supossed to be a compliment or not ._.")
                            main_menu(name)
                            break
                elif player == "Score":
                    #This funtion is used for retrive score obtained by the user and AI
                        print("Your Score is ", user,"\nBrian(AI) Score is ", AI)
                else:
                    print("That's not a valid option. Check your spelling!")
                player = False
                
                computer = t[randint(0,2)]
                #the computer or AI chooses the next move before hand.
        rockpaperscissors(name)
        
    elif game=='3':
        def tictactoe(name):
            #This part of the program is done by Anirudh Preeth(ENG19CS0034)
            #this is for the Program to understand where the game piece are needed to be placed when the input is given
            theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                        '4': ' ' , '5': ' ' , '6': ' ' ,
                        '1': ' ' , '2': ' ' , '3': ' ' }

            board_keys = []

            for key in theBoard:
                board_keys.append(key)

            # This function is used to create the tic-tac-toe board
            def printBoard(board):
                print(board['7'] + '|' + board['8'] + '|' + board['9'])
                print('-+-+-')
                print(board['4'] + '|' + board['5'] + '|' + board['6'])
                print('-+-+-')
                print(board['1'] + '|' + board['2'] + '|' + board['3'])

            # Main function called game() which has all the gameplay functionality.
            def game():

                turn = 'X'
                count = 0

                play=input(print("You are about to play Tic-Tac_toe:\n 1.Play\n 2.Exit: (Enter option 1 or 2)"))
                if play == '1':
                    print("You need 2 players to play this game")
                    name1=input(print("Enter the second player name:"))
                    print("So,",name,"is X and ",name1,"is O")
                    print("Also the game uses your number pad as the grid")
                elif play == '2':
                    main_menu(name)
                else:
                    print("Invalid number, try again")
                    game()

                for i in range(10):
                    printBoard(theBoard)
                    print("It's your turn," + turn + ".Move to which place?")

                    move = input()        

                    if theBoard[move] == ' ':
                        theBoard[move] = turn
                        count += 1
                    else:
                        print("That place is already filled.\nMove to which place?")
                        continue

                    # Now we will check if player X or O has won,for every move after 5 moves. 
                    if count >= 5:
                        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                            printBoard(theBoard)
                            print("\nGame Over.\n")                
                            print(" **** " +turn + " won. ****")                
                            break
                        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                            printBoard(theBoard)
                            print("\nGame Over.\n")                
                            print(" **** " +turn + " won. ****")
                            break
                        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                            printBoard(theBoard)
                            print("\nGame Over.\n")                
                            print(" **** " +turn + " won. ****")
                            break
                        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                            printBoard(theBoard)
                            print("\nGame Over.\n")                
                            print(" **** " +turn + " won. ****")
                            break
                        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                            printBoard(theBoard)
                            print("\nGame Over.\n")                
                            print(" **** " +turn + " won. ****")
                            break
                        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                            printBoard(theBoard)
                            print("\nGame Over.\n")                
                            print(" **** " +turn + " won. ****")
                            break 
                        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                            printBoard(theBoard)
                            print("\nGame Over.\n")                
                            print(" **** " +turn + " won. ****")
                            break
                        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                            printBoard(theBoard)
                            print("\nGame Over.\n")                
                            print(" **** " +turn + " won. ****")
                            break 

                    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
                    if count == 9:
                        print("\nGame Over.\n")                
                        print("It's a Tie!!")

                    #To change the player after every move.
                    if turn =='X':
                        turn = 'O'
                    else:
                        turn = 'X'        

                # If player wants to restart the game or not after either player wins or loses or has a tie.
                restart = input("Do want to play Again?(y/n)")
                if restart == "y" or restart == "Y":  
                    for key in board_keys:
                        theBoard[key] = " "
                    game()
                else:
                    main_menu(name)

            if __name__ == "__main__":
                game()
                
        tictactoe(name)
    elif game=='4':
        sys.exit()
    else:
        print("Invalid input")

def main_menu(name):
        #This part of the program is done by Anup venkat(ENG19CS0037)
        #This function acts as a main menu when you get out a game
            game=input(print("Now then",name,"let's select the next game you what to play:\n 1.Hangman\n 2.Rock,Paper,Scissors\n 3.TIC-TAC-TOE\n 4.Exit\n What's your choose? (1-4):"))
            #Here depending on the user input the game function is defined and excuted
            if game=='1':
                def hangman(name):
                    #This part of the program is done by Anup venkat(ENG19CS0037)
                    import random
                    user=0
                    mode = input("You are about to play Hangman:\n Play\n exit:\n(Type your option)")
                    #Asking the user for input to start the game
                    if (mode=="exit"):
                        main_menu(name)
                    else:
                        print("Good Luck ! ", name)
                    words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'roads', 'movies']
                    word = random.choice(words)
                    print("Guess the characters")
                    guesses = ''
                    turns = 12
                    #conditions are checked in order to count the number of wrong letters(if any) or right one and accordingly trigger the remaining guesses function
                    while turns > 0:
                        failed = 0
                        for char in word:
                            if char in guesses: 
                                print(char)
                            else:
                                print("_")
                                failed += 1
                        if failed == 0:
                            print("You Win")
                            print("The word is: ", word)
                            replay=input(print("That was a good game, want to try that again:\n (y/n)\n"))
                            #Asking user if they want to play again after winning the game
                            if replay == 'y':
                                hangman(name)
                            else:
                                main_menu(name)
                                quit()
                                break
                        guess = input("guess a character:") 
                        guesses += guess
                        if guess not in word:
                            turns -= 1
                            print("Wrong")
                            print("You have", + turns, 'more guesses')
                            if turns == 0:
                                print("You Loose")
                                print("The word is: ", word)
                                replay=input(print("I belive you can win this game, want to try that again:\n (y/n)\n"))
                                #Asking user if they want to play again after lossing the game
                                if replay == 'y':
                                    hangman(name)
                                else:
                                    main_menu(name)
                hangman(name)
            elif game=='2':
                def rockpaperscissors(name):
                    #This part of the program is done by Anup venkat(ENG19CS0037)
                    t = ["Rock", "Paper", "Scissors"]
                    computer = t[randint(0,2)]
                    player = False
                    user=0
                    AI=0
                    print("WARNING: THE INPUT IS CASE-SENSITIVE SO INPUT YOU CHOICE CAREFULLY!!")
                    print("All the best, ", name)
                    while player == False:
                        player = input("Enter the Option:\nRock, Paper, Scissors?\nTo exit the program type 'exit'\nTo see your Score type 'Score'\n")
                        #Asking user to input there operation for the function to decide what to do.
                        #The following if-else condition checkes for the user input and determines the if the user or the computer has won the game and accordingly increase there score respectively. 
                        if player == computer:
                            print("Tie!")
                        elif player == "Rock":
                            if computer == "Paper":
                                print("You lose!", computer, "covers", player)
                                AI=AI+1
                            else:
                                print("You win!", player, "smashes", computer)
                                user=user+1
                        elif player == "Paper":
                            if computer == "Scissors":
                                print("You lose!", computer, "cut", player)
                                AI=AI+1
                            else:
                                print("You win!", player, "covers", computer)
                                user=user+1
                        elif player == "Scissors":
                            if computer == "Rock":
                                print("You lose...", computer, "smashes", player)
                                AI=AI+1
                            else:
                                print("You win!", player, "cut", computer)
                                user=user+1
                        elif player == "exit":
                            #This elif condition checkes if the the score of the user is higher than computer or AI accordingly gives a response to the user 
                                if user>AI :
                                    print("Well, you defeted our AI, Brian, Good Job")
                                    main_menu(name)
                                elif user<AI :
                                    print("Well that sucks, our AI, Brian, just made you lose in this game")
                                    main_menu(name)
                                else:
                                    print("You have the same luck as a robot, we do not know if this is supossed to be a compliment or not ._.")
                                    main_menu(name)
                                    break
                        elif player == "Score":
                            #This funtion is used for retrive score obtained by the user and AI
                                print("Your Score is ", user,"\nBrian(AI) Score is ", AI)
                        else:
                            print("That's not a valid option. Check your spelling!")
                        player = False
                        #the computer or AI chooses the next move before hand.
                        computer = t[randint(0,2)]
                        
                rockpaperscissors(name)
            elif game=='3':
                def tictactoe(name):
                    #This part of the program is done by Anirudh Preeth(ENG19CS0034)
                    #this is for the Program to understand where the game piece are needed to be placed when the input is given
                    theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                                '4': ' ' , '5': ' ' , '6': ' ' ,
                                '1': ' ' , '2': ' ' , '3': ' ' }

                    board_keys = []

                    for key in theBoard:
                        board_keys.append(key)

                    # This function is used to create the tic-tac-toe board
                    def printBoard(board):
                        print(board['7'] + '|' + board['8'] + '|' + board['9'])
                        print('-+-+-')
                        print(board['4'] + '|' + board['5'] + '|' + board['6'])
                        print('-+-+-')
                        print(board['1'] + '|' + board['2'] + '|' + board['3'])

                    # Main function called game() which has all the gameplay functionality.
                    def game():

                        turn = 'X'
                        count = 0

                        play=input(print("You are about to play Tic-Tac_toe:\n 1.Play\n 2.Exit: (Enter option 1 or 2)"))
                        if play == '1':
                            print("You need 2 players to play this game")
                            name1=input(print("Enter the second player name:"))
                            print("So,",name,"is X and ",name1,"is O")
                            print("Also the game uses your number pad as the grid")
                        elif play == '2':
                            main_menu(name)
                        else:
                            print("Invalid number, try again")
                            game()

                        for i in range(10):
                            printBoard(theBoard)
                            print("It's your turn," + turn + ".Move to which place?")

                            move = input()        

                            if theBoard[move] == ' ':
                                theBoard[move] = turn
                                count += 1
                            else:
                                print("That place is already filled.\nMove to which place?")
                                continue

                            # Now we will check if player X or O has won,for every move after 5 moves. 
                            if count >= 5:
                                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                                    printBoard(theBoard)
                                    print("\nGame Over.\n")                
                                    print(" **** " +turn + " won. ****")                
                                    break
                                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                                    printBoard(theBoard)
                                    print("\nGame Over.\n")                
                                    print(" **** " +turn + " won. ****")
                                    break
                                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                                    printBoard(theBoard)
                                    print("\nGame Over.\n")                
                                    print(" **** " +turn + " won. ****")
                                    break
                                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                                    printBoard(theBoard)
                                    print("\nGame Over.\n")                
                                    print(" **** " +turn + " won. ****")
                                    break
                                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                                    printBoard(theBoard)
                                    print("\nGame Over.\n")                
                                    print(" **** " +turn + " won. ****")
                                    break
                                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                                    printBoard(theBoard)
                                    print("\nGame Over.\n")                
                                    print(" **** " +turn + " won. ****")
                                    break 
                                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                                    printBoard(theBoard)
                                    print("\nGame Over.\n")                
                                    print(" **** " +turn + " won. ****")
                                    break
                                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                                    printBoard(theBoard)
                                    print("\nGame Over.\n")                
                                    print(" **** " +turn + " won. ****")
                                    break 

                            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
                            if count == 9:
                                print("\nGame Over.\n")                
                                print("It's a Tie!!")

                            #To change the player after every move.
                            if turn =='X':
                                turn = 'O'
                            else:
                                turn = 'X'        

                        # If player wants to restart the game or not after either player wins or loses or has a tie.
                        restart = input("Do want to play Again?(y/n)")
                        if restart == "y" or restart == "Y":  
                            for key in board_keys:
                                theBoard[key] = " "
                            game()
                        else:
                            main_menu(name)

                    if __name__ == "__main__":
                        game()
                        
                tictactoe(name)
            elif game=='4':
                sys.exit()
            else:
                print("Invalid input")
                main_menu(name)


the_3in1_game()


# In[ ]:




