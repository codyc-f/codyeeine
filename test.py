# Cody Choo-Foo, 2030183
# R. Vincent, instructor
# Advanced Programming, section 1
# Final project

import pygame
import random


pygame.init() #needed at beginning of program to run anything pygame related

#window
screen_width = 900 #size in pixels
screen_height = 900
screen = pygame.display.set_mode([screen_width,screen_height]) #creates window
pygame.display.set_caption('Snake Game') #sets title of window
font = pygame.font.Font(None,45) #needed to write on screen

#colors
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
LIGHTBLUE = (204,255,255)
YELLOW = (255,255,51)
BEIGE = (245,245,220)

clock = pygame.time.Clock() #intializes clock to run at 60 fps

def screentext(msg, color, x, y):
    ''''function to easily display text on screen'''
    text = font.render(msg, True, color)
    screen.blit(text, [x, y]) #puts the text on the screen

def plot_snake(screen, color, body, snake_size):
    '''function that draws snake on screen'''
    for x,y in body:
        pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])

def startscreen():
    '''initialization of the first screen when program is running'''
    image = pygame.image.load('how to.jpg') #opens image
    exitgame = False
    while not exitgame:
        screen.fill(LIGHTBLUE) #fills background
        screen.blit(image, [screen_width/7,screen_height/2]) #adds image on the screen
        screentext("Welcome! Press 'Enter' to play!", BLACK, 200,200)
        for event in pygame.event.get(): #iterates through all inputs
            if event.type == pygame.QUIT: #checks if user clicks on the x on the window
                exitgame = True
            elif event.type == pygame.KEYDOWN: #checks if keyboard input
                if event.key == pygame.K_ESCAPE: #checks if escape key it spressed
                    exitgame = True
                elif event.key == pygame.K_RETURN: #checks if return keyis pressed
                    game()

        pygame.display.flip() #needed to update screen
        clock.tick(60) #sets 60 fps on screen

def game():
    '''main game'''
    # game variables
    counter = 0 #score counter
    snake_x = screen_width / 2 #initial position of snake in x coord
    snake_y = screen_height / 2 #initial position of snake in y coord
    gameover = False
    exitgame = False
    speedx = 0 #initial speed of snake in x coord
    speedy = 0 #initial speed of snake in y coord
    initspeed = 4 #sets the movement of speed throughout whole game
    body = [] #list containing list of x,y coordinates of pieces of body
    snk_length = 1 #inital length of snake
    foody = random.randint(0, screen_height) #random coordinate in y for food
    foodx = random.randint(0, screen_width) #random coordinate in x for food
    fps = 60 #variable for fps
    start = open("hs.txt")
    highscore = start.read() #stores high score value from txt file
    while not exitgame:
        if gameover: #loads losing screen
            background = pygame.image.load('sadface.png')
            screen.blit(background, [0,200])
            screentext("Game over, Press 'ESC' to exit or Press 'Enter' to play again", BLACK, 0, 100)
            screentext("Your score is: " + str(counter), BLACK, 600,500)
            screentext("Your HighScore was: " + str(highscore), YELLOW, 400, 800)
            if counter > int(highscore): #checks new score vs high score
                writing = open("hs.txt", "w")
                writing.write(str(counter)) #changes old high score to new high score
                writing.close()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #user clicks "x" on the window
                    exitgame = True
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: #user presses escape key
                        exitgame = True
                        exit()
                    elif event.key == pygame.K_RETURN:
                        game()
                        exit() #closes original window
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        speedy = -initspeed #changes speed in y
                        speedx = 0
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        speedy = initspeed
                        speedx = 0
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        speedx = -initspeed #changes speed in x
                        speedy = 0
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        speedx = initspeed
                        speedy = 0
                    elif event.key == pygame.K_ESCAPE:
                        exit()
            snake_x += speedx #new value of x coord of snake
            snake_y += speedy #new value of y coord of snake

            if abs(snake_x - foodx)<20 and abs(snake_y - foody)<20: #checks if the snake pixel is on the food pixel
                counter += 1 #adds to score
                foodx = random.randint(0, screen_width) #another x coord for food is randomly generated
                foody = random.randint(0, screen_height) #another y coord for food is randomly generated
                snk_length += 10 #adds snake length
                
            screen.fill(BEIGE)
            pygame.draw.rect(screen, GREEN, [foodx, foody, 20, 20]) #draws food
            screentext("Score: " + str(counter), BLACK, 0,0) #puts text on screen
            screentext("HighScore: " + str(highscore), YELLOW, screen_width*2/3, 0)

            head = [] #list of x and y coord of head of snake
            head.append(snake_x)
            head.append(snake_y)
            body.append(head) #adds head list to body

            if len(body)>snk_length: #
                del body[0]

            if head in body[:-1]: #checks if snake runs into itself
                gameover = True
            if snake_x > screen_width or snake_x < 0 or snake_y < 0 or snake_y > screen_height: #checks if snake runs into border of screen
                gameover = True
            plot_snake(screen, BLACK, body, 20)
        pygame.display.flip()
        clock.tick(fps)



startscreen()



