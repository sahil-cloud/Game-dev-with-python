import pygame
import random
import os

pygame.init()

pygame.mixer.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
#screen specs
screen_width=600
screen_height=600
#backgroung img

GameWindow=pygame.display.set_mode((screen_width,screen_height))
bgimg = pygame.image.load("SSS.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height))

pygame.display.set_caption("SNAKES")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

def plot_snake(GameWindow,color,snk_list,snake_size): #ploting sanke 
    for x,y in snk_list:
        pygame.draw.rect(GameWindow, black, [
                     x, y, snake_size, snake_size])

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    GameWindow.blit(screen_text,[x,y]) #plotting score on screen

def welcome(): #welcome msg
    exit_game=False
    while not exit_game:
        GameWindow.fill(white)
        
        text_screen("welcome to snakes",black,165,250)    
        text_screen("press space to play",red,165,300)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play()
                    Gameloop()
        pygame.display.update()
        clock.tick(60)        

def Gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    velocity_x = 0
    velocity_y = 0  # giving velocity
    food_x = random.randint(100, screen_width-100)  # genrates random variable
    food_y = random.randint(100, screen_height-100)
    score = 0
    fps = 40  # frames per second
    with open("his.txt","r") as f:
        hiscore=f.read()

    snk_list = []  # creating snake list
    snk_length = 1  # snake length
#creating a game loop
    while not exit_game:
        #event handling
        if game_over:
            with open("his.txt", "w") as f:
                f.write(str(hiscore))

            GameWindow.fill(white)
            text_screen("Game over :Tap a key to continue",red,100,250)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    welcome()
                if event.type == pygame.QUIT:
                    exit_game = True
        else:           
            for event in pygame.event.get():
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=5
                        velocity_y = 0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = -5
                        velocity_y = 0
                    
                    if event.key == pygame.K_DOWN:
                        velocity_y = 5
                        velocity_x = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -5
                        velocity_x = 0
                    if event.key == pygame.K_q: #cheat code
                        score=score+10
                       # snk_length +=5

                if event.type == pygame.QUIT:
                    exit_game=True 

            snake_x=velocity_x+snake_x
            snake_y=velocity_y+snake_y
            
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score += 10
                food_x = random.randint(100, screen_width-100)
                food_y = random.randint(100, screen_height-100)
                snk_length +=5 #increesing length
                if score>int(hiscore):
                    hiscore=score
            GameWindow.fill(white)
            GameWindow.blit(bgimg, (0, 0))
            text_screen("score:"+str(score) + "  hiscore:" + str(hiscore),red,5,5)
            #creating head of snake
            pygame.draw.rect(GameWindow,red,[food_x,food_y,snake_size,snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head) #passing initial coordinates to the list

            if len(snk_list)>snk_length:
                del snk_list[0]

            if snake_y<0 or snake_y >screen_height or snake_x<0 or snake_x>screen_width:
                game_over=True
            if head in snk_list[:-1]:
                game_over=True
            #pygame.draw.rect(GameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(GameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()  # quit function
    quit()

welcome()
