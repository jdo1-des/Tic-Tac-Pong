# import and initailse pygame library
import pygame
pygame.init()

# import tkinter for message boxes
import tkinter as tk
from tkinter import messagebox

import sys
import subprocess as sp
import os
import pickle # import pickel for sending board across files
import time

# link to pong.py file
BASE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(BASE, "pong.py")

clock = pygame.time.Clock()

# define colors as constants for later
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

# open game screen
SIZE = (600,650)
BOARD_SIZE = 600
FONT = pygame.font.Font(None, 42)
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("tic tac toe")
SCREEN.fill(BLACK)

# set parameters for the lines on the board
LINE_SPACING = SIZE[0] / 3
LINE_SIZE = 5
BOARD_COLS = 3
BOARD_ROWS = 3
SPACE_SIZE = SIZE[0] / BOARD_COLS

# Set start of game board state

if len(sys.argv) > 1:
    round_winner = sys.argv[1]
    round = int(sys.argv[2])
    board_bytes = sys.stdin.buffer.read()
    board = pickle.loads(board_bytes)
else:
    round = 1
    round_winner = "Player A"
    board = [[0] *BOARD_COLS for _ in range(BOARD_ROWS)]
p = round_winner  # winner of the Pong round choses the spot
grand_winner = 0

def draw_X(row,col):
    start_pos_1 = (col * SPACE_SIZE, row * SPACE_SIZE + 50)
    end_pos_1 = ((col + 1) * SPACE_SIZE, (row +1) * SPACE_SIZE + 50)
    pygame.draw.line(SCREEN, BLUE, start_pos_1, end_pos_1, LINE_SIZE)
    start_pos_2 = ((col + 1) * SPACE_SIZE, row * SPACE_SIZE + 50)
    end_pos_2 = (col * SPACE_SIZE, (row+1) * SPACE_SIZE + 50)
    pygame.draw.line(SCREEN ,BLUE ,start_pos_2,end_pos_2, LINE_SIZE)

def draw_O(row,col):
    center = (int(col*SPACE_SIZE + SPACE_SIZE // 2), int(row*SPACE_SIZE + SPACE_SIZE // 2) + 50)
    pygame.draw.circle(SCREEN, RED, center, SPACE_SIZE // 2 - 10, LINE_SIZE, )

# a function to redraw the baord at the start of each round
def draw_round_board():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "Player A":
                draw_X(row,col)
            elif board[row][col] == "Player B":
                draw_O(row,col)

def check_win(board, chosen_row, chosen_col,p):    
    # check if there is 3 in a row
    if board[chosen_row][0] == board[chosen_row][1] == board[chosen_row][2] and board[chosen_row][0] != 0:
        y = chosen_row * SPACE_SIZE + SPACE_SIZE // 2 + 50
        pygame.draw.line(SCREEN, GREEN, (0,y), (600,y), LINE_SIZE*3)
        grand_winner = p
    # check if there is 3 in a column
    elif board[0][chosen_col] == board[1][chosen_col] == board[2][chosen_col] and board[0][chosen_col] != 0:
        x = chosen_col * SPACE_SIZE + SPACE_SIZE //2
        pygame.draw.line(SCREEN, GREEN, (x,50), (x, 650), LINE_SIZE*3)
        grand_winner = p
    # check for top left to bottom right diagonal
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        pygame.draw.line(SCREEN, GREEN, (0,50), (600,650), LINE_SIZE*3)
        grand_winner = p
    # check for bottom left to top right diagonal
    elif board[2][0] == board[1][1] == board[0][2] and board [2][0] != 0:
        pygame.draw.line(SCREEN, GREEN, (0,650), (600,50), LINE_SIZE*3)
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
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] < BOARD_SIZE:
            # record where screen is clicked
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            # convert click cords to and row and colum
            chosen_row = int(mouseY // SPACE_SIZE)
            chosen_col = int(mouseX // SPACE_SIZE)
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

    # display the current round on the screen
    round_counter = FONT.render("Round " + str(round), True, WHITE, BLACK)
    SCREEN.blit(round_counter, round_counter.get_rect(midtop=(SIZE[0]//2, 10)))

    # draw the grid lines
    # draw vertical lines
    pygame.draw.line(SCREEN, WHITE, (LINE_SPACING, 50), (LINE_SPACING, SIZE[1]), LINE_SIZE)
    pygame.draw.line(SCREEN, WHITE, (LINE_SPACING*2, 50), (LINE_SPACING*2, SIZE[1]), LINE_SIZE)
    # draw horizontal lines
    pygame.draw.line(SCREEN, WHITE, (0, LINE_SPACING + 50), (SIZE[0], LINE_SPACING + 50), LINE_SIZE)
    pygame.draw.line(SCREEN, WHITE, (0, LINE_SPACING*2 + 50), (SIZE[0], LINE_SPACING*2 + 50), LINE_SIZE)

    pygame.display.flip()

    clock.tick(60) # limit the game to 60 frames per second

    if grand_winner != 0:
        time.sleep(2)
        messagebox.showinfo("Game Over","The Tic Tac Pong grand winner is " + grand_winner + "!")
        carryOn = False
    elif round_over == True and grand_winner == 0 and round == 9:
        messagebox.showinfo("Tie","The game is a tie!")
        carryOn = False
    elif round_over == True:
        messagebox.showinfo("Round Over","Starting next round.")
        board_bytes = pickle.dumps(board)
        # open pong file and send board over
        round = round + 1
        process = sp.Popen([sys.executable, SCRIPT, str(round)], stdin=sp.PIPE, cwd=BASE)
        process.stdin.write(board_bytes)
        process.stdin.close()
        sys.exit()
        carryOn = False

pygame.quit()


