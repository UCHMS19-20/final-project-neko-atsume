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

class Teachers:
    """class of all collectable teachers"""
    def __init__(self, name, goodie, cost, rarity):
        """constructor for Teachers"""
        self.name = name
        self.goodie = goodie
        self.cost = cost
        self.rarity = rarity

#all the teachers available to collect. Cost is based on year that they teach, and rarity is based on if they're still teaching here or not.
teachers = [
    Teachers('Mrs. Gerstein', 'Robot', 300, 'Common'),
    Teachers('Mr. Sanservino', 'Pop Quiz', 2000, 'RARE'),
    Teachers('Dr. Fang', 'Free-Body Diagram', 300, 'Common'),
    Teachers('Mr. Weisser', 'Drum Set', 300, 'Common'),
    Teachers('Mr. Stanko', 'AED', 300, 'Common'),
    Teachers('Mr. Raite', 'Pure Oxygen', 300, 'Common'),
    Teachers('Mr. Nowakoski', 'Fancy Knife', 8000, 'ULTRA RARE'),
    Teachers('Mr. McMenamin', 'Patrick Star Shorts', 7000, 'ULTRA RARE'),
    Teachers('Dr. Jidarian', "GA's", 400, 'Common'),
    Teachers('Ms. Valley', 'Deadlift', 200, 'Common'),
    Teachers('Ms. Pinto', '35 Notecards', 200, 'Common'),
    Teachers('Mrs. Kipp', 'AutoCAD Certificate', 8000, 'ULTRA RARE'),
    Teachers('Mr. Moskowitz', 'Open Position', 600, 'Common')
]

# Sets base (initial) money value at 500. Currency is tears.
tears = 0
# Establishes the shop as a dictionary. Lists name of item and cost.
shop = {
    'Robot': 15,
    'Pop Quiz': 200,
    'Free-Body Diagram': 50,
    'Drum Set': 20,
    'AED': 15,
    'Pure Oxygen': 70,
    'Fancy Knife': 400,
    'Patrick Star Shorts': 400,
    "GA's": 50,
    'Deadlift': 30,
    '35 Notecards': 30,
    'AutoCAD Certificate': 500,
    'Open Position': 80
}

# Create colors for text
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
# Create font object
font = pygame.font.SysFont("Arial", 30)
# Create text object
#shop_prompt = font.render('What would you like to purchase?', True, black)
#Draw text
#screen.blit(shop_prompt, (50,50))
# Creat text object for shop
shop_list = font.render(shop, True, black)
#Draw text
screen.blit(shop_list, (50, 40))
# Update screen
pygame.display.flip()

# Main loop for game
while True:
    for event in pygame.event.get():
        #check if current event is a quit event
        if event.type == pygame.QUIT:
            #quit program if the event is quit
            sys.exit()
   