# First creating a list to store the contents of our game board
board=['-','-','-',
       '-','-','-',
       '-','-','-']

#  now creating a function to display our board
def show_board():
  print(board[0]+'|'+board[1]+'|'+board[2])
  print(board[3]+'|'+board[4]+'|'+board[5])
  print(board[6]+'|'+board[7]+'|'+board[8])

turn=0  # variable to keep track which player's turn it is
game_on=True

# making a list  of all the winning states
winning_states=[(0,3,6),(1,4,7),(2,5,8),(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6)]

def play_game():

  show_board()      # showing board 

  while(game_on):     # Loop until one of the player wins

    take_input()
    
    check_win()

    change_player()
      

# Funnction to take input from player
def take_input():

  if(turn==0):
      print('player 1:')
  else:
      print('Player 2:')
  pos = int(input("enter the position :")) - 1    # taking position 1 less than specified

  if(turn==0):
    board[pos] = 'X'
  else:
    board[pos] = 'O'
  show_board()

# Function to check if any winning state has been achived  
def check_win():
  global game_on   # defining game_on global so it can be modified
  for i in winning_states:
    # if condition to check winning state is achieved or not
    if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]] and board[i[0]] !='-':
      game_on=False
      if turn==0:
        print("Player 1 wins!!")
      else:
        print("Player 2 wins!!")
      print("Do you want to play again?(Y/N)")
      play_ag=input("Enter y or n:")
      if(play_ag=='y'):
        game_on=True
        reset()  #  calling reset  function to reset  all values
      
# Function to change the player after each turn
def change_player():
  global turn
  if(turn==0):
    turn=1
  else:
    turn=0
  return turn

# Function to reset values after game is over
def reset():
  global board
  turn=0
  board=['-','-','-',
       '-','-','-',
       '-','-','-']


play_game()
  