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
cactusImg0 = pygame.image.load('cactus_0.png')
cactusImg1 = pygame.image.load('cactus_1.png')
cactusImg2 = pygame.image.load('cactus_2.png')
cactusImg3 = pygame.image.load('cactus_3.png')
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

#def rocks(rockx, rocky, rockw, rockh):
#    gameDisplay.blit((

def cactus0(cactus0x, cactus0y, cactus0w, cactus0h, color):
    gameDisplay.blit((cactusImg0),[cactus0x, cactus0y, cactus0w, cactus0h])

def cactus1(cactus1x, cactus1y, cactus1w, cactus1h, color):
    gameDisplay.blit((cactusImg1),[cactus1x, cactus1y, cactus1w, cactus1h])

def cactus2(cactus2x, cactus2y, cactus2w, cactus2h, color):
    gameDisplay.blit((cactusImg2),[cactus2x, cactus2y, cactus2w, cactus2h])

def cactus3(cactus3x, cactus3y, cactus3w, cactus3h, color):
    gameDisplay.blit((cactusImg3),[cactus3x, cactus3y, cactus3w, cactus3h])

#cactus obstacle

def road0(roadx,roady):
    gameDisplay.blit(roadImg_0,(roadx,roady))

def road1(roadx,roady):
    gameDisplay.blit(roadImg_1,(roadx,roady))

def isfloat(num):
    #print(num)
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

    time.sleep(1)

    game_loop()
    
def crash():
    message_display('CRASH')
    
def game_loop():
    carx = (display_width * 0.45)
    cary = (display_height * 0.8)\

    groundx = 0
    groundy = 0

    roadx = 0
    roady = 0

   # timinge = 0
    
    carx_change = 0

    thing_startx = random.randrange(175, 625)
    thing_starty = -1000
    thing_speed = 10
    thing_width = 64
    thing_height = 64

    cactus0_startx = random.randrange(0, 175)
    cactus0_starty = -570
    cactus0_speed = 10
    cactus0_width = 78
    cactus0_height = 78

    cactus2_startx = random.randrange(0, 175)
    cactus2_starty = -500
    cactus2_speed = 10
    cactus2_width = 78
    cactus2_height = 78

    cactus3_startx = random.randrange(0, 175)
    cactus3_starty = -658
    cactus3_speed = 10
    cactus3_width = 78
    cactus3_height = 78

    cactus1_startx = random.randrange(0, 175)
    cactus1_starty = -712
    cactus1_speed = 10
    cactus1_width = 78
    cactus1_height = 78

    thingCount = 2

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

        #time.sleep(5)

     #   if (clock.tick % 2)==0:
       #     road0(roadx,roady)
       # else:
       #     road1(roadx,roady)
        
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        cactus0(cactus0_startx, cactus0_starty, cactus0_width, cactus0_height, black)
        cactus1(cactus1_startx, cactus1_starty, cactus1_width, cactus1_height, black)
        cactus2(cactus2_startx, cactus2_starty, cactus2_width, cactus2_height, black)
        cactus3(cactus3_startx, cactus3_starty, cactus3_width, cactus3_height, black)
        
        cactus0_starty += cactus0_speed
        cactus1_starty += cactus1_speed
        cactus2_starty += cactus2_speed
        cactus3_starty += cactus3_speed
        
        car(carx,cary)

     #   timinge += 0.5

       #if isfloat(timinge) == False:
          #  road0(roadx,roady)
            
      #  if isfloat(timinge) == True:
          #  road1(roadx,roady)
        
        things_dodged(dodged)
        
        if carx > display_width - car_width or carx < 0:
            crash()
            
        if cactus0_starty > display_height:
            cactus0_starty = 0 - cactus0_height
            cactus0_startx = random.randrange(0, 150)
            cactus0_speed += 1

        if cactus1_starty > display_height:
            cactus1_starty = 0 - cactus1_height
            cactus1_startx = random.randrange(0, 150)
            cactus1_speed += 1

        if cactus2_starty > display_height:
            cactus2_starty = 0 - cactus2_height
            cactus2_startx = random.randrange(675,800)
            cactus2_speed += 1

        if cactus3_starty > display_height:
            cactus3_starty = 0 - cactus3_height
            cactus3_startx = random.randrange(675,800)
            cactus3_speed += 1

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(175,600)
            dodged += 1
            thing_speed += 1
        #
        if cary < thing_starty+thing_height:
            #print('y crossover')

            if carx > thing_startx and carx < thing_startx + thing_width or carx+car_width > thing_startx and carx + car_width < thing_startx+thing_width:
              #  print('x crossover')
                crash()
        ####
            if carx > cactus0_startx and carx < cactus0_startx + cactus0_width or carx+car_width > cactus0_startx and carx + car_width < cactus0_startx + cactus0_width:
                crash()

            if carx > cactus1_startx and carx < cactus1_startx + cactus1_width or carx+car_width > cactus1_startx and carx + car_width < cactus1_startx + cactus1_width:
                crash()

            if carx > cactus2_startx and carx < cactus2_startx + cactus2_width or carx+car_width > cactus2_startx and carx + car_width < cactus2_startx + cactus2_width:
                crash()

            if carx > cactus3_startx and carx < cactus3_startx + cactus3_width or carx+car_width > cactus3_startx and carx + car_width < cactus3_startx + cactus3_width:
                crash()
        
        pygame.display.update()
        clock.tick(30)
        #print(isfloat(clock.tick))
        #print(clock.tick)


game_loop()
pygame.quit()
quit()
