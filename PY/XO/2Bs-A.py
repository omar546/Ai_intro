#initialising counters and valribales for game results
tie = lose = win = 0
computer = player = ' '
exit = False

#to calculate n of empty positions and return it
def nEmpty(board):
    count = 0
    for i in range(1, 10):
        if board[i] == ' ':
            count += 1
    return count

#to insert a letter at desired position
def inserting(letter, position):
    if board[position] == ' ':
        board[position] = letter
    elif position < 1 or position > 9:#to avoid wrong inputs
        position = int(input("please choose from 1 to 9:\n"))
        inserting(letter, position)
    else:#in case of it is a used position
        position = int(input("This place was chosen, choose another one:\n"))
        inserting(letter, position)

#to check for occurrence of possible winning ways
def checkForWin():
    #to check the diagonals
    if board[1] == board[5] and board[5] == board[9] and board[9] != ' ':
        return True
    if board[3] == board[5] and board[5] == board[7] and board[7] != ' ':
        return True
    #to check the raws
    for i in range(1, 8, 3):
        if board[i] == board[i + 1] and board[i + 1] == board[i + 2] and board[i + 2] != ' ':
            return True
    #to check the colomn
    for i in range(1, 4):
        if board[i] == board[i + 3] and board[i + 3] == board[i + 6] and board[i + 6] != ' ':
            return True

#to flag the case of draw
def isTie():
    #if board is full with no win or lose
    counter = 0
    # when the number of empty none empty is 9 then it retuns True
    # in the while loop we will use isWinner before it to avoid if it's full and win
    for i in range(1, 10):
        if board[i] != ' ':
            counter += 1
    return counter == 9

#to determine which letter is winning and it's the same as checkForWin function
def isWinner(letter):
    if board[1] == board[5] and board[5] == board[9] and board[9] == letter:
        return True
    if board[3] == board[5] and board[5] == board[7] and board[7] == letter:
        return True
    for i in range(1, 8, 3):
        if board[i] == board[i + 1] and board[i + 1] == board[i + 2] and board[i + 2] == letter:
            return True
    for i in range(1, 4):
        if board[i] == board[i + 3] and board[i + 3] == board[i + 6] and board[i + 6] == letter:
            return True

#to draw the game grid
def printBoard(board):
    print(' ' + board[1] + " | " + board[2] + " | " + board[3])
    print("---|---|---")
    print(' ' + board[4] + " | " + board[5] + " | " + board[6])
    print("---|---|---")
    print(' ' + board[7] + " | " + board[8] + " | " + board[9])

#this to see the bestScore ever to the current state and return it
def minimax(board, isMaxminzing):
    if isWinner(computer):
        return 100 * (nEmpty(board) + 1)
    elif isWinner(player):
        return -100 * (nEmpty(board) + 1)
    elif isTie():
        return 0
    if isMaxminzing:
        #to the Max step for AI
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                #recursively calling the minimax function
                score = minimax(board, False)
                board[key] = ' '
                bestScore = max(bestScore, score)
        return bestScore

    else:
        #to the Mini step from player
        lowScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                # recursively calling the minimax function
                score = minimax(board, True)
                board[key] = ' '
                lowScore = min(lowScore, score)
        return lowScore

#to start the computer's ("Ai") turn
def computerMove():
    bestScore = -100
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
                #passing the letter and chosen position of computer
    inserting(computer, bestMove)

#to start the human player's turn
def playerMove():
    position = int(input("Place your mark:\n"))
        #passing the letter and chosen position of player
    inserting(player, position)

#to start a new game with a cleared board
def playAgain():
    for i in range(1, 10):
        board[i] = ' '
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 " + "\n")

#creating the board
board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
#human have to choose his letter
player = input("Choose your mark (X/O): \nNote: X palys first\n")
#The guide to choose indexes
print("\nHere is the guide of indexes\n")
print(" 1 | 2 | 3 ")
print("---|---|---")
print(" 4 | 5 | 6 ")
print("---|---|---")
print(" 7 | 8 | 9 " + "\n")
#a loop to keep the game going till user choose to exit
while not exit:
    #the player plays first if he  chosed to be X
    if player == 'x' or player == 'X':
        computer = 'O'
        player = 'X'
        playerMove()
        if isWinner(player):
            print("Winner Winner!")
            #incrementing the winning counter
            win += 1
            #prompt user to continue or exit
            play = int(input("1- Play Again\n2- Exit\n"))
            if play == 2:
                exit = True
                break
            else:
                playAgain()
                continue
                #check for tie
        elif isTie():
            print("Tie!")
            # incrementing the ties counter
            tie += 1
            play = int(input("1- Play Again\n2- Exit\n"))
            if play == 2:
                exit = True
                break
            else:
                playAgain()
                continue
        computerMove()
        printBoard(board)
        if isWinner(computer):
            print("Loser!")
            # incrementing the losing counter
            lose += 1
            play = int(input("1- Play Again\n2- Exit\n"))
            if play == 2:
                exit = True
                break
            else:
                playAgain()
                continue
        elif isTie():
            print("Tie!")
            tie += 1
            play = int(input("1- Play Again\n2- Exit\n"))
            if play == 2:
                exit = True
                break
            else:
                playAgain()
                continue
    #the AI plays first
    else:
        player = 'O'
        computer = 'X'
        computerMove()
        printBoard(board)
        if isWinner(computer):
            print("Loser!")
            lose += 1
            play = int(input("1- Play Again\n2- Exit\n"))
            if play == 2:
                exit = True
                break
            else:
                playAgain()
                continue
        elif isTie():
            print("Tie!")
            tie += 1
            play = int(input("1- Play Again\n2- Exit\n"))
            if play == 2:
                exit = True
                break
            else:
                playAgain()
                continue
        playerMove()
        if isWinner(player):
            print("Winner Winner!")
            win += 1
            play = int(input("1- Play Again\n2- Exit\n"))
            if play == 2:
                exit = True
                break
            else:
                playAgain()
                continue
        elif isTie():
            print("Tie!")
            tie += 1
            play = int(input("1- Play Again\n2- Exit\n"))
            if play == 2:
                exit = True
                break
            else:
                playAgain()
                continue
#showing the statistics for the games played
print(str(win) + " Wins\n" + str(tie) + " Ties\n" + str(lose) + " loses")
#this code is writen by -omar_mekkawy -karim_h_radwan -omar_a_el'aissy -karim_maged -abd el'rahman_salem