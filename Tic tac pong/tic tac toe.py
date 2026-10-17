# import and initailse pygame library
import pygame
pygame.init()

# import tkinter for message boxes
import tkinter as tk
from tkinter import messagebox

# import the system and subprocesses libraries
import sys
import subprocess as sp
# import pickel for sending board across files
import pickle

clock = pygame.time.Clock()

# define colors as constants for later
Black = (0,0,0)
White = (255,255,255)

# open game screen
size = (600,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("tic tac toe")
screen.fill(Black)

# set parameters for the lines on the board
line_spacing = size[0] / 3
line_size = 5
Board_cols = 3
Board_rows = 3
Space_size = size[0] / Board_cols

# Set start of game board state

if len(sys.argv) > 1:
    round_winner = sys.argv[1] 
    board_bytes = sys.stdin.buffer.read()
    board = pickle.loads(board_bytes)
else:
    round_winner = "Player A"
    board = [[0] *Board_cols for _ in range(Board_rows)]
p = round_winner  # winner of the Pong round choses the spot
grand_winner = 0

def draw_X(row,col):
    start_pos_1 = (col * Space_size, row * Space_size)
    end_pos_1 = ((col + 1) * Space_size, (row +1) * Space_size)
    pygame.draw.line(screen, White, start_pos_1, end_pos_1, line_size)
    start_pos_2 = ((col + 1) * Space_size, row * Space_size)
    end_pos_2 = (col * Space_size, (row+1) * Space_size)
    pygame.draw.line(screen,White,start_pos_2,end_pos_2,line_size)

def draw_O(row,col):
    center = (int(col*Space_size + Space_size // 2), int(row*Space_size + Space_size // 2))
    pygame.draw.circle(screen, White, center, Space_size // 2, line_size, )

# a function to redraw the baord at the start of each round
def draw_round_board():
    for row in range(Board_rows):
        for col in range(Board_cols):
            if board[row][col] == "Player A":
                draw_X(row,col)
            elif board[row][col] == "Player B":
                draw_O(row,col)

def check_win(board, chosen_row, chosen_col,p):    
    # check if there is 3 in a row
    if board[chosen_row][0] == board[chosen_row][1] == board[chosen_row][2] and board[chosen_row][0] != 0:
        grand_winner = p
    # check if there is 3 in a column
    elif board[0][chosen_col] == board[1][chosen_col] == board[2][chosen_col] and board[0][chosen_col] != 0:
        grand_winner = p
    # check for top left to bottom right diagonal
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        grand_winner = p
        # check for bottom left to top right diagonal
    elif board[2][0] == board[1][1] == board[0][2] and board [2][0] != 0:
        grand_winner = p
    else:
        grand_winner = 0  
    return grand_winner 

carryOn = True # as long as this variable is true game will continue to run
round_over = False # when this becomes true go back to pong game

while carryOn: 

    for event in pygame.event.get(): 
        # if user clicks the close button, the game stops running
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # record where screen is clicked
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            # convert click cords to and row and colum
            chosen_row = int(mouseY // Space_size)
            chosen_col = int(mouseX // Space_size)
            # mark the chosen space
            if board[chosen_row][chosen_col] == 0:
                board[chosen_row][chosen_col] = p
                if board[chosen_row][chosen_col] == "Player A":
                    draw_X(chosen_row,chosen_col)
                    grand_winner = check_win(board, chosen_row, chosen_col,"Player A")
                elif board[chosen_row][chosen_col] == "Player B":
                    draw_O(chosen_row,chosen_col)
                    grand_winner = check_win(board,chosen_row, chosen_col, "Player B")
                round_over = True

    # draws the previous rounds board  
    draw_round_board()

    # draw the grid lines
    # draw vertical lines
    pygame.draw.line(screen, White, (line_spacing, 0), (line_spacing, size[1]), line_size)
    pygame.draw.line(screen, White, (line_spacing*2, 0), (line_spacing*2, size[1]), line_size)
    # draw horizontal lines
    pygame.draw.line(screen, White, (0, line_spacing), (size[0], line_spacing), line_size)
    pygame.draw.line(screen, White, (0, line_spacing*2), (size[0], line_spacing*2), line_size)

    pygame.display.flip()

    clock.tick(60) # limit the game to 60 frames per second

    if grand_winner != 0:
        messagebox.showinfo("The Tic Tac Pong grand winner is " + grand_winner + "!")
        carryOn = False
    elif round_over == True:
        messagebox.showinfo("Starting next round.")
        board_bytes = pickle.dumps(board)
        # open pong file and send board over
        process = sp.Popen([sys.executable, "pong.py", round_winner], stdin=sp.PIPE, stdout = sp.PIPE, stderr=sp.PIPE)
        process.stdin.write(board_bytes)
        process.stdin.close()
        sys.exit()
        carryOn = False

pygame.quit()


