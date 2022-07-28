import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
#display dimensions

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
#colour variables

car_width = 53
road_width = 460

oil = pygame.image.load('oil_1.png')
groundImg = pygame.image.load('ground.png')
cactus = pygame.image.load('cactus_1.png')
roadImg_0 = pygame.image.load('road_0.png')
roadImg_1 = pygame.image.load('road_1.png')
#importing obstacle images and ground and road

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('daquavious juandale bingleton')
clock = pygame.time.Clock()

carImg = pygame.image.load('car_0.png')
carLeftImg = pygame.image.load('car_1.png')
carRightImg = pygame.image.load('car_2.png')
#importing car images

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    gameDisplay.blit((oil),[thingx, thingy, thingw, thingh])
#oil obstacle

def road0(roadx,roady):
    gameDisplay.blit(roadImg_0,(roadx,roady))

def road1(roadx,roady):
    gameDisplay.blit(roadImg_1,(roadx,roady))

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def ground(groundx,groundy):
    gameDisplay.blit(groundImg,(groundx,groundy))
#displaying ground

def car(carx,cary):
    gameDisplay.blit(carImg,(carx,cary))
#displaying car

def carLeft(carx,cary):
    gameDisplay.blit(carLeftImg,(carx -10,cary -10))
#displaying car turning left
def carRight(carx,cary):
    gameDisplay.blit(carRightImg,(carx,cary))
#displaying car turning right
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
def crash():
    message_display('CRASHED')
    
def game_loop():
    carx = (display_width * 0.45)
    cary = (display_height * 0.8)

    groundx = 0
    groundy = 0

    roadx = 0
    roady = 0

    
    
    carx_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -1200
    thing_speed = 10
    thing_width = 64
    thing_height = 64

    thingCount = 1

    #car(carx,cary)

    dodged = 0

    gameExit = False

    while not gameExit:

        car(carx,cary)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    carx_change = -10
                    carLeft(carx,cary)
                if event.key == pygame.K_d:
                    carx_change = 10
                    carRight(carx,cary)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    carx_change = 0
                    car(carx,cary)

        carx += carx_change

        ground(groundx,groundy)

     #   if (clock.tick % 2)==0:
       #     road0(roadx,roady)
       # else:
       #     road1(roadx,roady)
        
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        
        car(carx,cary)
        
        things_dodged(dodged)
        
        if carx > display_width - car_width or carx < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 0.5
        #
        if cary < thing_starty+thing_height:
            #print('y crossover')

            if carx > thing_startx and carx < thing_startx + thing_width or carx+car_width > thing_startx and carx + car_width < thing_startx+thing_width:
              #  print('x crossover')
                crash()
        ####
        
        pygame.display.update()
        clock.tick(30)
        print(isfloat(clock.tick))


game_loop()
pygame.quit()
quit()
