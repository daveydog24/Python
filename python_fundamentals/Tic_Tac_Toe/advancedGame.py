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

    # fuction to hand users guess
    def users_choice(self):
        number = input("Please select a number to mark your square: ")
        check_num = self.validate_input(number)
        if check_num == True:
            number = int(number)
            return number
        else:
            return False

    # function to check for valid entries and display proper error responses 
    def validate_input(self, user_input):
        try:
            number = int(user_input)
        except ValueError:
            return False
        if len(user_input) == 1:
            if int(user_input) in self.guessed_nums:
                    print(f"The #{user_input} has already been guessed!")
                    return False
            else:
                return True
        else:
            print("Please enter a valid number Corey")
            return False

    # function to print the gameboard 
    def print_game(self):
        print("\n" * 7)
        print("                               ", self.board[0],"|", self.board[1],"|", self.board[2])
        print("                               ", self.board[3],"|", self.board[4],"|", self.board[5])
        print("                               ", self.board[6],"|", self.board[7],"|", self.board[8])
        print("\n" * 7)
    
    # where we change the game board pieces
    def change_square(self, index):
        if self.turn % 2 == 1:
            self.board[index - 1] = "X"
        else:
            self.board[index - 1] = "O"

    # goes through one game of tic tac toe for a win/loss/draw
    def one_game(self):
        while self.turn < 10:
            self.print_game()
            number = self.users_choice()
            if number == False:
                self.turn -= 1
            else:
                self.guessed_nums.append(number)
                self.change_square(number)
                winner = self.check_winner()
                if winner == True:
                    self.print_game()
                    if self.turn % 2 == 1:
                        print(f"{self.player1} is the winner!!!!")
                    else:
                        print(f"{self.player2} is the winner!!!!")
                    break
            self.turn += 1
        if self.turn == 10:
            print("TIE GAME!!!")
        else: 
            self.board = [1,2,3,4,5,6,7,8,9]
            self.guessed_nums = []
            self.turn = 1