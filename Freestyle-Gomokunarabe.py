import pygame as game
import random

# pygame setup

screen_width = 1280
screen_height = 720
board_size = round(screen_height  / 20)
print(board_size)
board_color = 'black'

game.init()
screen = game.display.set_mode((screen_width, screen_height))
game.display.set_caption('Freestyle-Gomokunarabe')
game.display.update()
font = game.font.Font('freesansbold.ttf', 22)
big_font = game.font.Font('freesansbold.ttf', 50)
clock = game.time.Clock()
fps = 60


# game setting

invalid = -1
empty = 0
black = 1
white = 2
removing_black = 3
removing_white = 4
removed = 5

board_pieces = [[empty for j in range(21)] for i in range(21)]

for i in range(21): # board borders are invalid, only exist to make searches easier
    board_pieces[0][i] = -1
    board_pieces[20][i] = -1
    board_pieces[i][0] = -1
    board_pieces[i][20] = -1

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
            if(board_pieces[i][j] == black):
                game.draw.circle(screen, 'black', (i * size, j * size), size / 2 - 1)
            if(board_pieces[i][j] == white):
                game.draw.circle(screen, 'white', (i * size, j * size), size / 2 - 1)
    
    
def freedom(x, y, piece_color): # checks for "freedom" rule by using dfs (for a given group of connected pieces of the same color to be in the board, at least 1 of them must have a free space adjacent to it)
    
    if board_pieces[x][y] == empty:
        return 1
        
    if board_pieces[x][y] != piece_color:
        return 0
    
    
    free = 0
    
    board_pieces[x][y] = removing_black if piece_color == black else removing_white
    
    if board_pieces[x + 1][y] != board_pieces[x][y]: free += freedom(x + 1, y, piece_color)
    if board_pieces[x - 1][y] != board_pieces[x][y]: free += freedom(x - 1, y, piece_color)
    if board_pieces[x][y + 1] != board_pieces[x][y]: free += freedom(x, y + 1, piece_color)
    if board_pieces[x][y - 1] != board_pieces[x][y]: free += freedom(x, y - 1, piece_color)
    
    board_pieces[x][y] = piece_color
    
    return free
    
    # DONE???


def valid_move(x, y):
    
    if x < 1 or y < 1 or x > 19 or y > 19:
        return False
    if board_pieces[x][y] != empty:
        return False
    
    board_pieces[x][y] = black if turn % 2 == 0 else white
    if freedom(x, y, board_pieces[x][y]) == 0:
        if board_pieces[x + 1][y] != board_pieces[x][y] and board_pieces[x + 1][y] != invalid and freedom(x + 1, y, black if turn % 2 == 1 else white) == 0:
            board_pieces[x][y] = 0
            return True
        if board_pieces[x - 1][y] != board_pieces[x][y] and board_pieces[x - 1][y] != invalid and freedom(x - 1, y, black if turn % 2 == 1 else white) == 0:
            board_pieces[x][y] = 0
            return True
        if board_pieces[x][y + 1] != board_pieces[x][y] and board_pieces[x][y + 1] != invalid and freedom(x, y + 1, black if turn % 2 == 1 else white) == 0:
            board_pieces[x][y] = 0
            return True
        if board_pieces[x][y - 1] != board_pieces[x][y] and board_pieces[x][y - 1] != invalid and freedom(x, y - 1, black if turn % 2 == 1 else white) == 0:
            board_pieces[x][y] = 0
            return True
        
        board_pieces[x][y] = 0
        return False
        
    else:
        board_pieces[x][y] = 0
        return True
    # DONE???

    return True

def remove_pieces(x, y, piece_color):
    
    if board_pieces[x][y] != piece_color: return
    
    board_pieces[x][y] = empty
    
    remove_pieces(x + 1, y, piece_color)
    remove_pieces(x - 1, y, piece_color)
    remove_pieces(x, y + 1, piece_color)
    remove_pieces(x, y - 1, piece_color)
    
    board_pieces[x][y] = empty if freedom(x, y, black if turn % 2 == 0 else white) > 0 else removed
    
    #TODO

def try_move(x, y):
    
    if not valid_move(x, y):    
        return
    
    board_pieces[x][y] = black if turn % 2 == 0 else white
    
    # TODO
    
    turn += 1
    
    
    

# main game loop
running = True
game_over = False
cursor_x = 0
cursor_y = 0
while running:
    clock.tick(fps)
    screen.fill('darkgoldenrod3') # mano, que desgraça de cor que eu escolhi
    
    draw_board(board_size)
    draw_pieces(board_size)
    
    #event handling
    for event in game.event.get():
        
        if event.type == game.QUIT:
            running = False
            
        if event.type == game.MOUSEMOTION and not game_over:
            x_coord = round(event.pos[0] / board_size)
            y_coord = round(event.pos[1] / board_size)
            click_coords = (x_coord, y_coord)
            print((x_coord, y_coord))
            
            cursor_x = x_coord
            cursor_y = y_coord
                
            
        if event.type == game.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = round(event.pos[0] / board_size)
            y_coord = round(event.pos[1] / board_size)
            click_coords = (x_coord, y_coord)
            print((x_coord, y_coord))
            
            if valid_move(x_coord, y_coord):
                board_pieces[x_coord][y_coord] = 1 if turn % 2 == 0 else 2
                turn += 1
            
            # TODO
    if valid_move(cursor_x, cursor_y):
        if turn % 2 == 0:
            game.draw.circle(screen, 'black', (cursor_x * board_size, cursor_y * board_size), board_size / 2 - 1, 5)
        else:
            game.draw.circle(screen, 'white', (cursor_x * board_size, cursor_y * board_size), board_size / 2 - 1, 5)
            
    game.display.flip()

game.quit()