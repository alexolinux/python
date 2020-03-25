from random import randint

# Declarando um Tabuleiro (Lista Vazia).
board = []

# Populando o Tabuleiro (Lista de 5 x 5).
for x in range(5):
  board.append(["O"] * 5)

# Formatando o Tabuleiro (eliminando caracteres).
def print_board(board):
  for row in board:
    print(" ".join(row))

# Printando o Tabuleiro Formatado para jogadas.
print_board(board)

# Funcao Randomica para fazer a localizacao do alvo em pos(x,y).
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

# Variaveis que recebem o posicionamento da Funcao Randomica.
ship_row = random_row(board)
ship_col = random_col(board)

# Print da localizacao do Alvo (DEBUGGING).
##print ship_row
##print ship_col

# Everything from here on should go in your for loop!
# Looping (iterando 04 tentativas).
for turn in range(4):

# Validacao de Entrada de Dados.
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
    break

  else:
    if turn == 3:
      board[guess_row][guess_col] = "X"
      print("Game Over.")

    else:
      if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print("Oops, that's not even in the ocean.")
        reason = "Out of Map!"
      elif(board[guess_row][guess_col] == "X"):
        print("You guessed that one already.")
        reason = "Repeated Guesses!"
      else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
  
# Print (turn + 1) here!
  print("Turn", turn + 1)
  print_board(board)
