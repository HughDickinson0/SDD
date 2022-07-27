import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 55

gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('race_test')
clock = pygame.time.Clock()
	
bg_img = pygame.image.load('ground.png')
bg_img = pygame.transform.scale(bg_img,(display_width,display_height))

oil = pygame.image.load('oil_1.png')

rock = pygame.image.load('rock_0.png')

cactus = 0

vehicle = pygame.image.load('car_0.png')

def car(x,y):
    gamedisplay.blit(vehicle, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gamedisplay.blit(TextSurf, TextRect)

    pygame.display.update()


    time.sleep(2)

    game_loop()

def crash():
    message_display('daquavious bingleton')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameexit = False
    
    while not gameexit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -8
                if event.key == pygame.K_d:
                    x_change = 8
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        x += x_change

        gamedisplay.fill(white)
        car(x,y)
    
        if x > display_width - car_width or x < 0:
            crash()
        
        pygame.display.update()
        clock.tick(30)

game_loop()
pygame.quit()
quit()
