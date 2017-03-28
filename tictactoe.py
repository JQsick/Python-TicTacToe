#Initialize
import random
import IPython.display

#globals
turn = True
cat_tracker = 0
winner = False
player1_name = ''
player2_name = ''
player_piece = {}
player_move = ''
gp = {"A1": ' ', 'A2': ' ', 'A3': ' ', 'B1': ' ', 'B2': ' ', 'B3': ' ', 'C1': ' ', 'C2': ' ', 'C3': ' '}

def main_game():
    
    #************ 
    global turn 
    global cat_tracker
    global winner
    global player1_name
    global player2_name
    global player_piece
    global player_move
    global gp
    #************
    
    #Initialize defaulted values ---
    turn = True
    cat_tracker = 0
    winner = False
    player1_name = ''
    player2_name = ''
    player_piece = {}
    player_move = ''
    gp = {"A1": ' ', 'A2': ' ', 'A3': ' ', 'B1': ' ', 'B2': ' ', 'B3': ' ', 'C1': ' ', 'C2': ' ', 'C3': ' '} 
    #-------------------------------

    
    #!!!*** Start of Functions ***!!!
    def print_grid():
        print('    A   B   C ')
        print('            ')
        print('1   {} | {} | {}  '.format(gp["A1"],gp["B1"],gp["C1"]))
        print('   ---|---|---')
        print('2   {} | {} | {}  '.format(gp["A2"],gp["B2"],gp["C2"]))
        print('   ---|---|---')
        print('3   {} | {} | {}  '.format(gp["A3"],gp["B3"],gp["C3"]))

    #Clears in Jupyter
    def clr_scr():
        IPython.display.clear_output()

    def assign_name():
        global turn
        global player1_name
        global player2_name
        global player_piece

        player1_name = input('Welcome to Text Based Tic Tac Toe!\n\nPlayer 1 what is your name? ')
        clr_scr()
        player2_name = input('Player 1 name: ' + player1_name + '\n\nPlayer 2 what is your name? ')
        clr_scr()
        print('Player 1 name: ' + player1_name + '\n\nPlayer 2 name: ' + player2_name )

        #assigns a player to X randomly who always goes first
        if random.randint(0,1) == 0:
            player_piece['player1'] = 'X'
            player_piece['player2'] = 'O'
            print('\n' + player1_name + ', you have randomly been assigned to X and will go first!')
        else:
            player_piece['player1'] = 'O'
            player_piece['player2'] = 'X'
            print('\n' + player2_name + ', you have randomly been assigned to X and will go first!')
            turn = False

    def directions():
        directions_input = input("\nDirections: Type letter and number and press enter to place your piece. Example: A2\n\nDo you understand? Type 'ok' and hit enter ")
        if directions_input.lower() == 'ok':
            clr_scr()
            pass
        else: 
            clr_scr()
            print('You CLEARLY do not understand.')
            
            #re-do directions with emphasis
            directions()

    def player_turn():
        global turn

        #player 1 plays on turn = True
        #returns player input for grid position
        if turn:
            player_input = input(player1_name + ", pick your '" + player_piece['player1'] + "' position! ")
            turn = False
            return player_input  
        else:
            player_input = input(player2_name + ", pick your '" + player_piece['player2'] + "' position! ")
            turn = True
            return player_input

    def winner_check():
        global cat_tracker
        cat_tracker +=1

        #all possible winning combinations
        gp_winners = [
             gp['A1'] == gp['A2'] == gp['A3'] == gp[player_move], 
             gp['B1'] == gp['B2'] == gp['B3'] == gp[player_move], 
             gp['C1'] == gp['C2'] == gp['C3'] == gp[player_move],
             gp['A1'] == gp['B1'] == gp['C1'] == gp[player_move], 
             gp['A2'] == gp['B2'] == gp['C2'] == gp[player_move],
             gp['A3'] == gp['B3'] == gp['C3'] == gp[player_move],
             gp['A1'] == gp['B2'] == gp['C3'] == gp[player_move], 
             gp['C1'] == gp['B2'] == gp['A3'] == gp[player_move]
             ]

        #first check for winners
        for i in range(0, len(gp_winners)):
            if gp_winners[i]:
                print_grid()
                #looks for last move made to decide who won
                if turn: 
                    print('Congrats ' + player2_name + '! You Win!')
                    return True
                else:
                    print('Congrats ' + player1_name + '! You Win!')
                    return True

        #cats game after 9 moves and no winners
        if cat_tracker == 9: 
            print_grid()
            print("It's a CATS game!!!")
            return True

        #then return false to continue playing
        return False

    def game_loop():
        global winner
        global player_move
        global turn
        global player_piece

        #loops until winner_check returns True
        while winner == False: 
            #goes to player_turn()

            print_grid()
            player_move = player_turn()
            player_move = player_move.upper()
            clr_scr()
            
            #checks for correct input
            if player_move in gp.keys():

                #start again if spot is taken, keeps track of the turn
                if gp[player_move] != ' ':
                    print('That spot is already taken, enter an open spot.')
                    if turn:
                        turn = False
                    else: 
                        turn = True

                else:
                    #stores player piece X or O into the grid location they choose
                    #player2 turn is True after player_turn()
                    #sends to see if the move is a winning move
                    if turn:
                        gp[player_move] = player_piece['player2']
                        winner = winner_check()
                    else:
                        gp[player_move] = player_piece['player1']  
                        winner = winner_check()

            #redo if they input something weird, keeps track of turn
            else: 
                print('Please enter letter+number! Example: A2')
                if turn:
                    turn = False
                else: 
                    turn = True
                    
    #!!!*** End of Functions ***!!!

    
    #plays through game
    assign_name()
    directions() 
    game_loop()
    
    #play again?
    play_again = input('Play again? type: yes')
    if play_again.upper() == 'YES':
        clr_scr()
        main_game()
        
    clr_scr()

main_game()