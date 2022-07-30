#Snake game 
#The player controls a snake which roams around on a bordered plane, picking up food,
#The object of the game is to eat food to grow longer while avoiding hitting its own tail or wall

import pygame, sys, random




#def game_over(self):
   #check if the snake if outside of the screen

   #check if snake hits itself 





#initialize the pygame library
pygame.init()

#Create a title for the game
pygame.display.set_caption('Snake game by EC')
#Set up the screen display
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,600))
test_surface = pygame.Surface((50,100))
test_surface.fill((0,125,255))

#Set the initial position of the snake
x1 = 20
y1 = 100

x1_change = 0
y1_change = 0

#create game loop 
while True:
    
    for event in pygame.event.get():
        #To get user input from keyboard to move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10 
            if event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0

        #Check if the user clicked the window close button
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit
            
        x1 += x1_change
        y1 += y1_change

    #Fill the background with Green
    screen.fill((0,128,0))
    screen.blit(test_surface,(150,200))
    pygame.draw.rect(screen,pygame.Color('blue'),pygame.Rect(x1,y1,30,30))
    pygame.display.update()
    clock.tick(60)











