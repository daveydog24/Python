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