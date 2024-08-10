def print_board(board):
    print("*********************")
    #make for loops to print the rows not manually
    print("*   {}  | {} | {}   *".format(board[0][0],board[0][1],board[0][2]))
    #line 2 breakline row%2==0
    print("*   {}  | {} | {}   *".format(board[1][0],board[1][1],board[1][2]))
    #line 4 breakline
    print("*   {}  | {} | {}   *".format(board[2][0],board[2][1],board[2][2]))
    print("*********************")
#add check win function
#add make turn function(board,row,col,player)
def main():
    board = [[' ','O','X'],['X','O','X'],['X','O','X']]
    print_board(board)
    while True:
        print("Enter the row and column to place the mark:")
        row,col=map(int,input().split())
        #add here the logic to check if the row and column are valid
        #add to check whos turn it is
        #add check for tie (after 9 plays)
        board[row][col]='X'
        print_board(board)






