import random

def takePlayerInput():
    player = "blank"   #default value
    while not(player.lower() == 'r' or player.lower() == 'p' or player.lower() == 's'):
        player = input ("Please enter your choice from R | P | S = ")
    return player.lower()


def getComputerInput():
    lst = ['r', 's', 'p']
    bot_choice = random.choice(lst)
    print("Bot Chooses =", bot_choice)
    return bot_choice


def checkWinner (player,bot):
    if (player == 'r' and bot == 'r') or (player == 's' and bot == 's') or (player == 'p' and bot == 'p'):
        return 'Draw'
    elif (player == 'r' and bot == 's') or (player == 's' and bot == 'p') or (player == 'p' and bot == 'r'):
        return 'player'
    elif (player == 'r' and bot == 'p') or (player == 's' and bot == 'r') or (player == 'p' and bot == 's'):
        return 'bot'

def rockPaperScissor():
    endTheGame = 'n'
    player_score = 0
    bot_score = 0
    while endTheGame.lower() != 'y':
        ply = takePlayerInput()
        bt = getComputerInput()
        winner = checkWinner(player = ply,bot = bt)
        if winner == 'player':
            player_score += 2
        elif winner == 'bot':
            bot_score += 2
        else:
            player_score += 1
            bot_score += 1

        print("=================== Score Board ===================")
        print("================== Player =================",player_score)
        print("================== Bot =================",bot_score)
        print(' ')
        endTheGame = input("End The game ? Y/N - ")




rockPaperScissor()


