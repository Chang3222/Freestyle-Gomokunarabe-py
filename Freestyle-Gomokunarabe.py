import pygame as game
import random

# colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
brown = (150, 75, 0)


# pygame setup
screen_width = 1000
screen_height = 1000

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

# TODO: use pygame built in circle instead of images
#black_piece = game.image.load('assets/images/black_piece.png')
#black_piece = game.transform.scale(black_piece, (80, 80))
#white_piece = game.image.load('assets/images/white_piece.png')
#white_piece = game.transform.scale(white_piece, (80, 80))


def draw_board(size): # OBS: mapear as posições para colocar as peças (ou encontrar solução semelhante)
    
    line_width = 3
    
    for i in range(size, 19 * size + 1, size):
        game.draw.line(screen, 'grey50', (i, size), (i, 19 * size), width = line_width)
        
    for i in range(size, 19 * size + 1, size):
        game.draw.line(screen, 'grey50', (size, i), (19 * size, i), width = line_width)

# def draw_pieces():
    # TODO

# main game loop
run = True
while run:
    clock.tick(fps)
    screen.fill('darkgoldenrod3') # mano, que desgraça de cor que eu escolhi
    
    draw_board(50)
    
    #event handling
    for event in game.event.get():
        
        if event.type == game.QUIT:
            run = False
            
        if event.type == game.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            # TODO
            
    game.display.flip()

game.quit()