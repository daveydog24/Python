class TicTacToe(object):
    def __init__(self):
        self.board = [1,2,3,4,5,6,7,8,9]
        self.guessed_nums = []
        self.player1 = None
        self.player2 = None
        self.turn = 1

    # handles the start of every game
    def start(self):
        want_to_play = False
        play_a_game = input("Want to play a game of Tic Tac Toe? ")
        yes = ["YES", "Yes", "y", "Y", "yes"]
        if play_a_game in yes:
            return True
        else:
            return False

    # function to define players
    def get_players(self):
        self.player1 = input("Enter your name Player 1: ")
        self.player2 = input("Enter your name Player 2: ")
