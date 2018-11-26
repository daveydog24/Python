board = [1,2,3,4,5,6,7,8,9]

def change_square(index, turn):
    if turn % 2 == 1:
        board[index - 1] = "X"
    else:
        board[index - 1] = "O"
        
def print_square(board):
    print(board[0],"|", board[1],"|", board[2])
    print(board[3],"|", board[4],"|", board[5])
    print(board[6],"|", board[7],"|", board[8])

turn = 1
while turn < 10:
    print_square(board)
    number = input("Please select a number to mark your square: ")
    number = int(number)
    print("You entered:", number)
    change_square(number, turn)
    turn += 1

