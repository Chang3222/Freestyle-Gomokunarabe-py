import pygame as game
import random

# pygame setup

screen_width = 700
screen_height = 700
board_size = 35
board_color = 'black'
board_pieces = [[0 for j in range(21)] for i in range(21)] # -1 = invalid, 0 = empty, 1 = black, 2 = white

for i in range(21): # invalid positions
    board_pieces[0][i] = -1
    board_pieces[20][i] = -1
    board_pieces[i][0] = -1
    board_pieces[i][20] = -1


game.init()
screen = game.display.set_mode((screen_width, screen_height))
game.display.set_caption('Freestyle-Gomokunarabe')
game.display.update()
font = game.font.Font('freesansbold.ttf', 22)
big_font = game.font.Font('freesansbold.ttf', 50)
clock = game.time.Clock()
fps = 60


# game setting

black_stock = 181
white_stock = 180

turn = 0


def draw_board(size):
    
    line_width = 3
    j = 0
    for i in range(size, 19 * size + 1, size):
        game.draw.line(screen, board_color, (i, size), (i, 19 * size), width = line_width)            
        
    for i in range(size, 19 * size + 1, size):
        game.draw.line(screen, board_color, (size, i), (19 * size, i), width = line_width)
        
    for i in range(size + 3 * size, 3 * 6 * size + 3 * size + 1, 6 * size):
        for j in range(size + 3 * size, 3 * 6 * size + 3 * size + 1, 6 * size):
            game.draw.circle(screen, board_color, (i, j), 6)

def draw_pieces(size):

    for i in range(20):
        for j in range(20):
            if(board_pieces[i][j] == 1):
                game.draw.circle(screen, 'black', (i * size, j * size), size / 2 - 1)
            if(board_pieces[i][j] == 2):
                game.draw.circle(screen, 'white', (i * size, j * size), size / 2 - 1)
    

def valid_move(x, y):
    
    # TODO (or not, idk)
    if board_pieces[x][y] != 0:    
        return
    
    return True

def try_move(x, y):
    
    if board_pieces[x][y] != 0:    
        return
        
    
    
    

# main game loop
running = True
game_over = False
while running:
    clock.tick(fps)
    screen.fill('darkgoldenrod3') # mano, que desgraça de cor que eu escolhi
    
    draw_board(board_size)
    draw_pieces(board_size)
    
    #event handling
    for event in game.event.get():
        
        if event.type == game.QUIT:
            running = False
            
        if event.type == game.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = round(event.pos[0] / board_size)
            y_coord = round(event.pos[1] / board_size)
            click_coords = (x_coord, y_coord)
            
            if valid_move(x_coord, y_coord):
                board_pieces[x_coord][y_coord] = 1 if turn % 2 == 0 else 2
                turn += 1
            
            # TODO

        
            
    game.display.flip()

game.quit()