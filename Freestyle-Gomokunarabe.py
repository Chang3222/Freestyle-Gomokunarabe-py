import pygame as game
import random

#colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
brown = (150, 75, 0)

screen_width = 900
screen_height = 900

game.init()

screen = game.display.set_mode((screen_width, screen_height))

game.display.set_caption('Freestyle-Gomokunarabe')

game.display.update()

clock = game.time.clock()

font = game.font.Font('freesansbold', 22)
big_font = game.font.Font('freesansbold', 50)

fps = 60



game.quit()