import sys
import pygame

#initialize pygame
pygame.init()

#create a display
screen = pygame.display.set_mode( (700, 500) )
print(pygame.QUIT)

#create a background
background = pygame.image.load("src/img/magnet-exterior.png")
#define image size and location
backrect = background.get_rect()
#load image onto screen
screen.blit(background, backrect)
#update screen with changes
pygame.display.flip()

# Main loop for game
while True:
    for event in pygame.event.get():
        #check if current event is a quit event
        if event.type == pygame.QUIT:
            #quit program if the event is quit
            sys.exit()