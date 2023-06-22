import pygame as game
import random

# pygame setup

screen_width = 1280
screen_height = 720
board_size = round(screen_height  / 20)
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

black_stock = 181
white_stock = 180

turn = 0
remove_list = []

board_pieces = [[empty for j in range(21)] for i in range(21)]

for i in range(21): # board borders are invalid, only exist to make searches easier
    board_pieces[0][i] = invalid
    board_pieces[20][i] = invalid
    board_pieces[i][0] = invalid
    board_pieces[i][20] = invalid


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
    
    if board_pieces[x][y] == empty or board_pieces[x][y] == removed:
        return 1
        
    if board_pieces[x][y] != piece_color:
        return 0
    
    
    free = 0
    
    board_pieces[x][y] = removing_black if piece_color == black else removing_white
    
    free += freedom(x + 1, y, piece_color)
    free += freedom(x - 1, y, piece_color)
    free += freedom(x, y + 1, piece_color)
    free += freedom(x, y - 1, piece_color)
    
    board_pieces[x][y] = piece_color
    
    return free
    
    # DONE???


def valid_move(x, y):
    
    if x < 1 or y < 1 or x > 19 or y > 19:
        return False
    if board_pieces[x][y] != empty:
        return False
    
    board_pieces[x][y] = black if turn % 2 == 0 else white
    opposite = black if turn % 2 == 1 else white
    
    if freedom(x, y, board_pieces[x][y]) == 0:
        if board_pieces[x + 1][y] == opposite and freedom(x + 1, y, opposite) == 0:
            board_pieces[x][y] = empty
            return True
        if board_pieces[x - 1][y] == opposite and freedom(x - 1, y, opposite) == 0:
            board_pieces[x][y] = empty
            return True
        if board_pieces[x][y + 1] == opposite and freedom(x, y + 1, opposite) == 0:
            board_pieces[x][y] = empty
            return True
        if board_pieces[x][y - 1] == opposite and freedom(x, y - 1, opposite) == 0:
            board_pieces[x][y] = empty
            return True
        
        board_pieces[x][y] = empty
        return False
        
    else:
        board_pieces[x][y] = empty
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
    
    board_pieces[x][y] = piece_color
    board_pieces[x][y] = empty if freedom(x, y, black if turn % 2 == 1 else white) > 0 else removed
    if board_pieces[x][y] == removed:
        remove_list.append((turn, x, y))
    
    # DONE???
    
def is_winning_move(x, y, piece_color):
    x_win = 1
    y_win = 1
    xy_win = 1
    yx_win = 1
    
    i = 1
    
    while board_pieces[x + i][y] == piece_color:
        x_win += 1
        i += 1
    i = 1
    while board_pieces[x - i][y] == piece_color:
        x_win += 1
        i += 1
    i = 1  
    while board_pieces[x][y + i] == piece_color:
        y_win += 1
        i += 1
    i = 1
    while board_pieces[x][y - i] == piece_color:
        y_win += 1
        i += 1
    i = 1    
    while board_pieces[x + i][y + i] == piece_color:
        xy_win += 1
        i += 1
    i = 1
    while board_pieces[x - i][y - i] == piece_color:
        xy_win += 1
        i += 1
    i = 1    
    while board_pieces[x + i][y - i] == piece_color:
        yx_win += 1
        i += 1
    i = 1
    while board_pieces[x - i][y + i] == piece_color:
        yx_win += 1
        i += 1
        
    return x_win >= 5 or y_win >= 5 or xy_win >= 5 or yx_win >= 5
    
    

def try_move(x, y):
    
    global turn
        
    if not valid_move(x, y):    
        return
    
    board_pieces[x][y] = black if turn % 2 == 0 else white
    opposite = black if turn % 2 == 1 else white
    
    if board_pieces[x + 1][y] == opposite and freedom(x + 1, y, opposite) == 0:
        remove_pieces(x + 1, y, opposite)
        
    if board_pieces[x - 1][y] == opposite and freedom(x - 1, y, opposite) == 0:
        remove_pieces(x - 1, y, opposite)
        
    if board_pieces[x][y + 1] == opposite and freedom(x, y + 1, opposite) == 0:
        remove_pieces(x, y + 1, opposite)
        
    if board_pieces[x][y - 1] == opposite and freedom(x, y - 1, opposite) == 0:
        remove_pieces(x, y - 1, opposite)
        
    # TODO
    
    if is_winning_move(x, y, black if turn % 2 == 0 else white):
        print(f'{black if turn % 2 == 0 else white} wins')
        
    turn += 1
    
    while len(remove_list) > 0 and remove_list[0][0] == turn - 2 and board_pieces[remove_list[0][1]][remove_list[0][2]] == removed:
            
        board_pieces[remove_list[0][1]][remove_list[0][2]] = empty
        remove_list.pop(0)
    
    
    
    

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
            
            cursor_x = x_coord
            cursor_y = y_coord
                
            
        if event.type == game.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = round(event.pos[0] / board_size)
            y_coord = round(event.pos[1] / board_size)
            
            try_move(x_coord, y_coord)
            
            # TODO
    if valid_move(cursor_x, cursor_y):
        if turn % 2 == 0:
            game.draw.circle(screen, 'black', (cursor_x * board_size, cursor_y * board_size), board_size / 2 - 1, 5)
        else:
            game.draw.circle(screen, 'white', (cursor_x * board_size, cursor_y * board_size), board_size / 2 - 1, 5)
            
    game.display.flip()

game.quit()