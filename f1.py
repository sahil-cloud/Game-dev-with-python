import pygame
pygame.init() #for pygame intialising

#for creating game window
GameWindow=pygame.display.set_mode((1000,500))

#for creating caption in window
pygame.display.set_caption("MY FIRST GAME")

#for creating game specific variables
exit_game=False
game_over=False

#creating a game loop
while not exit_game:
    #event handling
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           exit_game=True 

        #if event.type == pygame.KEYDOWN:
         #   if event.key == pygame.K_RIGHT:
          #      print("you have pressed right key")

pygame.quit() #quit function
quit()
"""