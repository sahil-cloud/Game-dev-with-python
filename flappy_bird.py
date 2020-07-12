import pygame
import random
import sys

pygame.init()
pygame.mixer.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
#screen specs
screen_width = 600
screen_height = 600
#backgroung img

GameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("FLAPPY BIRD")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

exit_game=False
game_over=False

