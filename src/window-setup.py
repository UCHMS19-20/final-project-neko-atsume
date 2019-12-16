import sys
import pygame

#initialize pygame
pygame.init()

#create a display
screen = pygame.display.set_mode( (700, 500) )
print(pygame.QUIT)

#create a background
background = pygame.image.load("img/magnet-exterior.png")
#fill window with color
screen.fill( (255, 255, 255) )
#fill screen with background
screen.blit(background)
#update screen with changes
pygame.display.flip()

# Main loop for game
while True:
    for event in pygame.event.get():
        #check if current event is a quit event
        if event.type == pygame.QUIT:
            #quit program if the event is quit
            sys.exit()