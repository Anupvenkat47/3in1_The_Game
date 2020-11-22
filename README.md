# 3in1_The_Game
_This is developed by **Anup Venkat** and **Anirudh Preeth** for Python Mini project at Dayananda Sagar University, Kudlu Gate_

**Introduction**:
  Imagine if you where bored to the core while doing a work you hate to do, or doing that assignment that has to be submitted in 12 hours and you feel like taking a break, well you came to the right place to destroy your boredom.
  This game has 3 games in it:
  1) Hangman
  2) Rock,Paper,Scissors
  3) Tic,Tac,Toe
And these games can be accesed by using the main menu built by me that execute them as and when it is called
 This entire program is created in python and you can download this and play it if you want and give me suggestions for improvement :).

**Working**:
  1)_**Introduction function (aka the_3in1_game() function)**_:
    This function is used only once in order to introduce the game and the people who are hosting the game in order to make the user familiarize with the simple UI that we have created, This will have each games function which will work without the command from the main_menu() so as to run any game without having to force the user to one game at the beginning of program every time it starts.

    ```
    def the_3in1_game():
      #This part of the program is done by Anup venkat(ENG19CS0037)
      #This part of the program starts the interface and the main menu
      print("Hello and welcome to 3in1:The game, well you came to this game because you where bored to core while doing you work or assignment or that very long project that you have to do in 2 days\n Whatever the case maybe you came to the right game to pass your time ;)\n You will be playing with our simple AI named Briann\n")
      print("Oh, I just realised that me and my friend have not introdued to you, My name is Anup venkat and where as this good friend of mine is called Anirudh Preeth.\n")
      name=input(print("Well this is awkward, we forgot to ask you name\n What's your name? "))
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
    ```
    ![](https://github.com/Anupvenkat47/3in1_The_Game/blob/main/Intro()%20function.jpg?raw=true)

  2)_**main_menu() function**_:
    This function is used the most after the Introduction function, After the user wins or loses a game, The user decides if he/she wants to play the game again and if they select no or 'n' then this function is executed with the user name to get more personal with the user, It gives the user with options that lists all the games and an option to close the game (in order for the user to close the program safely and not cause any error when the program is reexecuted for any reasons)

    ```
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
    ```

    ![](https://github.com/Anupvenkat47/3in1_The_Game/blob/main/Going%20in%20to%20main%20menu%20after%20a%20game.jpg?raw=true)
    ![](https://github.com/Anupvenkat47/3in1_The_Game/blob/main/TTT%20ending%20of%20the%20game.jpg?raw=true)

  3)_**hangman function**_:This function is executed/runned when the user requests this function in order to play a game of Hangman.
      This function runs first by asking the user to confirm if they want to play, if they want to play this game the function will be taking the name of the user given at the start of the program and display the message that wishes the best for the user and then randomly takes a word from the list of words givin in the list called 'words' and then waits for the user input, if the given letter(s) is correct the guess counter is not decremented and the right letter(s) are placed in the blanks else it will decrement the guess count value (which is fixed at 12) and inform the user of there error.
      Once the user is guess the right word or when the user's guess count reaches the game, the function will display the right word and according asks the user if they want to play again or play another game, in case if they have chosen the latter it will run the main_menu() function.
      The function is same for both Introduction and main_menu() functions.

      ```
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
      ```
      ![](https://github.com/Anupvenkat47/3in1_The_Game/blob/main/Hangman_function_win.jpg?raw=true)

  4)_**rockpaperscissors() function**_:This function is executed/runned when the user requests this function in order to play a game of Rock,Paper,Scissors.
      This function runs first by asking the user to confirm if they want to play, if they want to play this game the function will be taking the name of the user given at the start of the program and display the message that wishes the best for the user.
      The function then randomly selects a option and waits for the user input where the user will input the option they want to use, then the function will compare between the choice taken by the AI and user and accordingly calls the user if he won the round or not and the score of the AI or user is incremented accordingly
      when the user chooses to look at there score the function will display the scores and asks the user if they want to play a game again, if they choose to exit the game the function will check if the AI has scored more, less or the same as the user did and according will give a message to the User.
      The function remains the same for both Introduction and main_menu() functions.

      ```
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
      ```
      ![](https://github.com/Anupvenkat47/3in1_The_Game/blob/main/RPS%20input.jpg?raw=true)
      ![](https://github.com/Anupvenkat47/3in1_The_Game/blob/main/RPS%20score%20and%20message%20after%20exiting%20to%20main%20menu.jpg?raw=true)

  5)_**tictactoe() function**_:This function is executed/runned when the user requests this function in order to play a game of Rock,Paper,Scissors.
      This function runs first by asking the user to confirm if they want to play, if they want to play this game the function will be taking the name of the user given at the start of the program and display the message that wishes the best for the user.
      Since this function is a 2 player game, this function will ask the name of the other player and will accordingly tell who gets the 'x' piece and 'O' piece. The function will take the input from the keyboard and will place the piece at that array location, after 5 moves the function will check for every move after that, so as to find if any of the player got a winning position, if it has found one it will stop the game and inform who won the game for that round else it will keep on checking, if the board is filled the function will declare that game as draw/tie.
      The function is same for both Introduction and main_menu() functions

    ```
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
      ```
      ![](https://github.com/Anupvenkat47/3in1_The_Game/blob/main/TTT%20input%20and%20output.jpg?raw=true)
      ![](https://github.com/Anupvenkat47/3in1_The_Game/blob/main/TTT%20ending%20of%20the%20game.jpg?raw=true)
