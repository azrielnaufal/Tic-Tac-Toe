# MODULES
import pygame, sys
import numpy as np

# initializes pygame
pygame.init()

# ---------
# CONSTANTS
# ---------
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15 # tebal garis
WIN_LINE_WIDTH = 15 # tebal coretan garis yg menang
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200 # ukuran masing2 kotak -> square_size^2
CIRCLE_RADIUS = 60 # radius lingkaran
CIRCLE_WIDTH = 30 # tebal garis lingkaran
CROSS_WIDTH = 25 # tebal garis silang
SPACE = 30 #
bot = 2
player = 1
# we assign rgb value (red green blue) 
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BG_COLOR = (145, 121, 250) #ganti warna background
LINE_COLOR = (94, 23, 235) #ganti warna garis pada background
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)


# ------
# SCREEN
# ------
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Backtracking Tic Tac Toe')
screen.fill( BG_COLOR )
mainClock = pygame.time.Clock()

# -------------
# CONSOLE BOARD
# -------------
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

# ---------
# FUNCTIONS
# ---------
def draw_lines(): # untuk gambar garis2 kotak
	# 1 horizontal
	pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
	# 2 horizontal
	pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )
	# 1 vertical
	pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	# 2 vertical
	pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )

def draw_figures(): # untuk gambar simbol player dan bot ( O DAN X )
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			elif board[row][col] == 2:
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )	
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )
	print(board)

def mark_square(row, col, player): # assign 1 kotak, terisi oleh player yang mana (1 , 2 ,...)
	if available_square(row,col):
		board[row][col] = player

def available_square(row, col): # -> if kotaknya available maka -> return True
	return board[row][col] == 0

def is_board_full(): # cek apakah semua kotak penuh ato gaa, kalo penuh -> return True
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 0:
				return False

	return True

def check_win(player): # nge cek udh ada yang menang belum
	# vertical win check
	for col in range(BOARD_COLS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			return True

	# horizontal win check
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			return True

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		return True

	# desc diagonal win chek
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		return True

	return False

#bikin coretan garis kalo berhasil menang
def draw_vertical_winning_line(col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

def draw_horizontal_winning_line(row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )

def winning_Line(player):
		# vertical win check
	for col in range(BOARD_COLS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)

	# horizontal win check
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal(player)

	# desc diagonal win chek
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)

	return

def restart():
	screen.fill( BG_COLOR )
	draw_lines()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0

def checkDraw():
	for row in range(0,BOARD_ROWS):
		for col in range(0,BOARD_COLS):
			if (board[row][col] == 0):
				return False
	return True

def compMove_X():
	bestScore = -800
	bestMove_row = -1
	bestMove_col = -1
	for i in range(0,BOARD_ROWS):
		for y in range(0,BOARD_COLS):
			if (board[i][y] == 0):
				board[i][y] = bot
				score = minimax(bot,board, 0, False)
				board[i][y] = 0
				if (score > bestScore):
					bestScore = score
					bestMove_row = i
					bestMove_col = y

	mark_square(bestMove_row,bestMove_col,bot)
	return 

def compMove_O():
	bestScore = -800
	bestMove_row = -1
	bestMove_col = -1
	for i in range(0,BOARD_ROWS):
		for y in range(0,BOARD_COLS):
			if (board[i][y] == 0):
				board[i][y] = player
				score = minimax(player,board, 0, False)
				board[i][y] = 0
				if (score > bestScore):
					bestScore = score
					bestMove_row = i
					bestMove_col = y

	mark_square(bestMove_row,bestMove_col,player)
	return 

def minimax(user, board, depth, isMaximizing):
	if user == player:
		minVal = bot
	elif user == bot:
		minVal = player

	if (check_win(user)):
		return 1
	elif (check_win(minVal)):
		return -1
	elif (checkDraw()):
		return 0

	if (isMaximizing):
		bestScore = -800
		for i in range(0,BOARD_ROWS):
			for y in range(0,BOARD_COLS):
				if (board[i][y] == 0):
					board[i][y] = user
					score = minimax(user,board, depth + 1, False)
					board[i][y] = 0
					if (score > bestScore):
						bestScore = score
		return bestScore

	else:
		bestScore = 0
		for i in range(0,BOARD_ROWS):
			for y in range(0,BOARD_COLS):
				if (board[i][y] == 0):
					board[i][y] = minVal
					score = minimax(user,board, depth + 1, True)
					board[i][y] = 0
					if (score < bestScore):
						bestScore = score
		return bestScore

def main_2Bot():
	
	draw_lines()
	game_over = False
	running = False
	while not running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					restart()
					main_2Bot()
				if event.key == pygame.K_s:
					if not game_over:
						compMove_O()
						if check_win(1):
							game_over = True
							winning_Line(1)
						compMove_X()
						if check_win(2):
							game_over = True
							winning_Line(2)
						draw_figures()
				if event.key == pygame.K_ESCAPE:
					running = True

		pygame.display.update()
		mainClock.tick(60)

if __name__ == "__main__":
	main_2Bot()


