#Snake game 
#The player controls a snake which roams around on a bordered plane, picking up food,
#The object of the game is to eat food to grow longer while avoiding hitting its own tail or wall

import pygame, sys, random




#def game_over(self) :
   #check if the snake if outside of the screen

   #check if snake hits itself 



snake_speed = 15

#Set screen size
screen_width = 600
screen_length = 720 

#initialize the pygame library
pygame.init()

#Create a title for the game
pygame.display.set_caption('Snake game by YC')
#Set up the screen display
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_length))


#Set the initial position and length of the snake
snake_positionX = 20
snake_positionY = 100
snake_size = 5
snake_length = 1
snake_blocks = []

x1_change = 0
y1_change = 0



#Set the initial position of the fruit
fruit_positionX = random.randrange(1, (screen_width//10)) * 10
fruit_positionY = random.randrange(1, (screen_length//10)) * 10
fruit_spawn = True

#Set initial score
score = 0

game_over = False

#create game loop 
while True:
  
  for event in pygame.event.get():
        #To get user input from keyboard to move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -5 
            if event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 5
            if event.key == pygame.K_LEFT:
                x1_change = -5
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = 5
                y1_change = 0

        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit   
     
   
  if not game_over: 
    
    #Set the position of the snake head
    snake_head = []
    snake_head.append(snake_positionX)
    snake_head.append(snake_positionY)
    snake_blocks.append(snake_head)
    
    #Check if any block except last one is touching the snake head
    for x in snake_blocks[:-1]:
      if x == snake_head:
        game_over = True

        
    if snake_positionX == fruit_positionX and snake_positionY == fruit_positionY:
      fruit_positionX = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
      fruit_positionY = round(random.randrange(0, screen_length - snake_size) / 10.0) * 10.0
      snake_length += 1
         
      fruit_spawn = True
    
   #Update the speed of the snake 
    snake_positionX += x1_change
    snake_positionY += y1_change

        #Check if the user clicked the window close button
    

  #Fill the background with Green
  screen.fill((0,128,0))
  pygame.draw.rect(screen,pygame.Color('blue'),pygame.Rect(snake_positionX,snake_positionY,30,30))
  pygame.display.update()
  clock.tick(60)











