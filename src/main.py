import sys
import pygame


#initialize pygame
pygame.init()

#create a display
screen = pygame.display.set_mode( (1150, 500) )
print(pygame.QUIT)

#create a background
background = pygame.image.load("src/img/magnet-exterior.png")
#define image size and location
backrect = background.get_rect()
#load image onto screen
screen.blit(background, backrect)
#update screen with changes
pygame.display.flip()


# Create colors for text
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
magenta = pygame.Color(250, 72, 233)
# Create font object
font = pygame.font.SysFont("Arial", 20)

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
    Teachers('Ms. Valley', 'Deadlift', 200, 'Common'),
    Teachers('Ms. Pinto', '35 Notecards', 200, 'Common'),
    Teachers('Mrs. Kipp', 'AutoCAD Certificate', 8000, 'ULTRA RARE'),
    Teachers('Mr. Moskowitz', 'Open Position', 600, 'Common')
]

def welcome():
    """Welcomes te player to the game and explains some commands"""
    #creates a text object for the welcome message
    welcome_message = font.render('Welcome to Sensei Atsume: Teacher Collector!', True, white)
    #Draws the text
    screen.blit(welcome_message, (730, 30))
    #creates a text object for commands list
    commands = font.render('To open the shop: RIGHT ARROW KEY', True, white)
    #draws the commands text
    screen.blit(commands, (730, 80))
    # Creates a text object for continuation
    cont = font.render('To start the game, press space', True, white)
    #draws the continuation text
    screen.blit(cont, (730, 150))
    #updates the screen
    pygame.display.flip()
    return

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
    'Deadlift': 30,
    '35 Notecards': 30,
    'AutoCAD Certificate': 500,
    'Open Position': 80
}


def open_shop():
    """Opens the shop and lists the items and the prices of the items available for purchase."""
    # Create text object
    shop_prompt = font.render('What would you like to purchase?', True, white)
    #Draw text
    screen.blit(shop_prompt, (710,50))
    #Update screen
    pygame.display.flip()

    #defines the y value of the shop text for the following for loop.
    y= 80
    # Create text object for shop
    for key, value in shop.items():
        shop_list = font.render(f'{key}: {value}', True, white)
        #Draw text
        screen.blit(shop_list, (730, y))
        # Update screen
        pygame.display.flip()
        # Spaces out the shop items so they don't overlap
        y += 25
    return
#dictionary for the dimensions of a rectangle that clears the sidebar.
sidebar = {
    "x": 700,
    "y": 0,
    "height": 500,
    "width": 450
}
#START OF GAME CODE

# Main loop for game
while True:
    for event in pygame.event.get():
        #check if current event is a quit event
        if event.type == pygame.QUIT:
            #quit program if the event is quit
            sys.exit()
    #Defines a variable relating to retrieving information about which keys are being pressed.
    keys = pygame.key.get_pressed()
    #draws over the sidebar if space button is clicked
    if keys[pygame.K_SPACE]:
        pygame.draw.rect(screen, black, (sidebar["x"], sidebar["y"], sidebar["width"], sidebar["height"]))
    #Welcomes the player to the game and explains some commands.
    welcome()
    #if right arrow key is clicked, the shop opens.
    if keys[pygame.K_RIGHT]:
        open_shop()