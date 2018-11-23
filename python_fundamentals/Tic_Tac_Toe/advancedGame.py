class TicTacToe(object):
    def __init__(self):
        self.board = [1,2,3,4,5,6,7,8,9]
        self.guessed_nums = []
        self.player1 = None
        self.player2 = None
        self.turn = 1
