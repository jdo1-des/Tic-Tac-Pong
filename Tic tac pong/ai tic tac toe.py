# import and initailse pygame library
import pygame
pygame.init()

# import tkinter for message boxes
import tkinter as tk
from tkinter import messagebox

import random as rand
import sys
import subprocess as sp
import os
import pickle # import pickel for sending board across files
import time

# link to pong.py file
BASE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(BASE, "ai pong.py")

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
    round_winner = "Player"
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
            if board[row][col] == "Computer":
                draw_X(row,col)
            elif board[row][col] == "Player":
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

# computer mind
LINES = [
    [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], # rows
    [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)], # columns
    [(0,0), (1,1), (2,2)], [(0,2),(1,1), (2,0)], # diagonals
]
# function that looks for a line with 2 of players markers and 1 empty space
def find_winning_move(player):
    for line in LINES:
        values = [board[r][c] for r,c in line]
        if values.count(player) == 2 and values. count(0) == 1:  # if a lien has two spaces filled by the player and one empty
            return line[values.index(0)]
    return None

# function that chooses where the computer places its marker
def computer_move():
        move = find_winning_move("Computer") # if computer can win it plays that
        if move:
            return move
        move = find_winning_move("Player") # if player can win computer blocks it
        if move:
            return move
        if board[1][1] == 0: # if center is open computer plays there
            return (1,1)
        #  otherwise computer randomly choses a space to play
        # check board for empty spots
        for r in range(3): 
            for c in range(3):
                if board[r][c] == 0:
                    empty = [(r,c)]
                    return rand.choice(empty)

# function for Player or computer to place marker
def place_mark(chosen_row,chosen_col):
    global grand_winner, round_over
    board[chosen_row][chosen_col] = p
    if p == "Computer":
        draw_X(chosen_row,chosen_col)
    else: 
        draw_O(chosen_row,chosen_col)
    grand_winner = check_win(board, chosen_row, chosen_col, p)
    round_over = True


# set text for round counter
round_counter = FONT.render("Round " + str(round), True, WHITE, BLACK)

carryOn = True # as long as this variable is true game will continue to run
round_over = False # when this becomes true go back to pong game

start_time = pygame.time.get_ticks() # get start time of game

while carryOn: 

    for event in pygame.event.get(): 
        # if user clicks the close button, the game stops running
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.MOUSEBUTTONDOWN and 50 <+event.pos[1] < SIZE[1]:
            # record where screen is clicked
            mouseX = event.pos[0]
            mouseY = event.pos[1] - 50
            # convert click cords to and row and colum
            chosen_row = int(mouseY // SPACE_SIZE)
            chosen_col = int(mouseX // SPACE_SIZE)
            # mark the chosen space
            if board[chosen_row][chosen_col] == 0 and p == "Player": # checks chosen space is empty and its the players turn
                place_mark(chosen_row,chosen_col)

    # if its computers turn it places a marker after a small wait
    if p == "Computer" and not round_over and pygame.time.get_ticks() - start_time > 700:
        row, col = computer_move()
        place_mark(row,col)

    # draws the previous rounds board  
    draw_round_board()

    SCREEN.blit(round_counter, round_counter.get_rect(midtop=(SIZE[0]//2, 10))) # draw round counter on screen

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
        time.sleep(1)
        messagebox.showinfo("Game Over","The Tic Tac Pong grand winner is " + grand_winner + "!")
        carryOn = False
    elif round_over == True and grand_winner == 0 and round == 9:
        messagebox.showinfo("Tie","The game is a tie!")
        carryOn = False
    elif round_over == True:
        messagebox.showinfo("Round Over","Starting next round.")
        board_bytes = pickle.dumps(board)
        # open pong file and send board over
        round += 1
        process = sp.Popen([sys.executable, SCRIPT, str(round)], stdin=sp.PIPE, cwd=BASE)
        process.stdin.write(board_bytes)
        process.stdin.close()
        sys.exit()
        carryOn = False

pygame.quit()


