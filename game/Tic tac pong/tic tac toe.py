# import and initailse pygame library
import pygame
pygame.init()

import sys

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
board = [[0] *Board_cols for _ in range(Board_rows)]

if len(sys.argv) > 1:
    round_winner = sys.argv[1]  
else:
    round_winner = "Player A"
p = round_winner  # winner of the Pong round choses the spot

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

carryOn = True # as long as this variable is true game will continue to run

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
                elif board[chosen_row][chosen_col] == "Player B":
                    draw_O(chosen_row,chosen_col)

    # draw the grid lines
    # draw vertical lines
    pygame.draw.line(screen, White, (line_spacing, 0), (line_spacing, size[1]), line_size)
    pygame.draw.line(screen, White, (line_spacing*2, 0), (line_spacing*2, size[1]), line_size)
    # draw horizontal lines
    pygame.draw.line(screen, White, (0, line_spacing), (size[0], line_spacing), line_size)
    pygame.draw.line(screen, White, (0, line_spacing*2), (size[0], line_spacing*2), line_size)



    pygame.display.flip()

    clock.tick(60) # limit the game to 60 frames per second


pygame.quit()


