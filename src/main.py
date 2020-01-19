import sys
import pygame
import time

#NEXT set up trivia and the teachers appearing.

#initialize pygame
pygame.init()

#create a display
screen = pygame.display.set_mode( (1150, 500) )
print(pygame.QUIT)


# Create colors for text
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

# Create font object
font = pygame.font.SysFont("Arial", 20)

def draw_back():
    """Draws a background for the game"""
    #create a background
    background = pygame.image.load("src/img/magnet-exterior.png")
    #define image size and location
    backrect = background.get_rect()
    #load image onto screen
    screen.blit(background, backrect)
    #draws over the sidebar
    pygame.draw.rect(screen, black, (sidebar["x"], sidebar["y"], sidebar["width"], sidebar["height"]))
    return


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

class Picker:
    """Draw and move the picker in the shop""" 
    
    def __init__(self, index=0):
        self.y = 80
        self.index = index

    # Draw the picker
    def draw_self(self):
        screen.blit(picker, (715, self.y))

    # move picker down one option if not on last option
    def next(self):
        if self.y< 355:
            self.y += 25
            self.index += 1

    # move picker up one option if not at top option
    def prev(self):
        if self.y>80:
            self.y -= 25
            self.index -= 1

commands = {'Open the shop': 'RIGHT ARROW', 'Clear screen': 'SPACE', 'Confirm selection/purchase': 'ENTER', 'Browse options': 'UP and DOWN ARROWS', 'Open Trivia': 'T'}

def welcome():
    """Welcomes the player to the game and explains some commands"""
    #creates a text object for the welcome message
    welcome_message = font.render('Welcome to Sensei Atsume: Teacher Collector!', True, white)
    #Draws the text
    screen.blit(welcome_message, (730, 30))
    # Set default height of commands list
    y_cmnd = 70
    for action, command in commands.items():
        command_list = font.render(f'{action}: {command}', True, white)
        screen.blit(command_list, (730, y_cmnd))
        # Space out the commands listed vertically
        y_cmnd += 25
    # Creates a text object for continuation
    cont = font.render('To start the game, press space', True, white)
    #draws the continuation text
    screen.blit(cont, (730, 300))
    #updates the screen
    pygame.display.flip()
    return


# Establishes the shop as a dictionary. Lists name of item and cost.
prices = {
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

#List of items for sale, in order
for_sale = ['Robot', 'Pop Quiz', 'Free-Body Diagram', 'Drum Set', 'AED', 'Pure Oxygen', 'Fancy Knife', 'Patrick Star Shorts', 'Deadlift', '35 Notecards', 'AutoCAD Certificate', 'Open Position']

def open_shop():
    """Opens the shop and lists the items and the prices of the items available for purchase."""
    # Ask player what they'd like to buy
    shop_prompt = font.render('What would you like to purchase?', True, white)
    #Draw text
    screen.blit(shop_prompt, (730,50))

    #defines the y value of the shop text for the following for loop.
    y= 80
    # Create text object for shop
    for key, value in prices.items():
        shop_list = font.render(f'{key}: {value}', True, white)
        #Draw text
        screen.blit(shop_list, (730, y))
        # Spaces out the shop items so they don't overlap
        y += 25
    #if you press the down arrow, the picker goes down one item
    if keys[pygame.K_DOWN]:
        #reduces click sensitivity by slowing the time between key input and movement
        pygame.time.wait(900)
        picker1.next()
    #if you press up arrow, picker goes up one item
    if keys[pygame.K_UP]:
        #reduces click sensitivity by slowing the time between key input and movement
        pygame.time.wait(900)
        picker1.prev()
    #draw picker
    picker1.draw_self()   
    return

#dictionary for the dimensions of a rectangle that clears the sidebar.
sidebar = {
    "x": 700,
    "y": 0,
    "height": 500,
    "width": 450
}

picker = font.render('>', True, white)

picker1=Picker()

# Sets base (initial) money value at 500. Currency is tears.
tears = 100

#blank list to keep track of purchased items
inventory = []


def purchase():
    """Allows the player to purchase items in the shop"""
    global tears
    global run1
    #defines the item the player picked to line up with the index (height) of the picker
    chosen_item = for_sale[picker1.index]
    #checks if chosen item has already been bought
    if chosen_item in inventory and run1 == True:
        already_have = font.render('You already have this item!', True, white)
        screen.blit(already_have, (750, 100))

    else:
        if tears < prices[chosen_item]:
            #calculates how much more money you need to buy the item
            difference = prices[chosen_item] - tears
            broke = font.render(f'Sorry, you are short {difference} tears.', True, white)
            screen.blit(broke, (750, 100))
            return
        elif tears >= prices[chosen_item]:
            if run1 == True:
                #update money 
                tears -= prices[chosen_item]
                #add bought item to your inventory
                inventory.append(chosen_item)
        # Display what item the player bought
        purchase_complete = font.render(f'You have purchased {chosen_item}', True, white)
        #Print purchase message
        screen.blit(purchase_complete, (750, 100))
        run1 = False
    return
    
def display_money():
    """Display the current amount of money"""
    # Create text object for the money value
    current_money = font.render(f'{tears} tears', True, white)
    # draw text
    screen.blit(current_money, (1050, 470))

#dictionary of numbered trivia topics to choose from
trivia_topics = {
    '1': 'Science',
    '2': 'History',
    '3': 'English',
    '4': 'Technology',
    '5': 'Health',
    '6': 'Math'
}
#dictionary of all the topics and their questions for trivia minigame
trivia_questions = {
    'Science': {'Easy': "What is Newton's Second Law?", 'Medium': "What is absolute zero in Celsius?", "Hard": 'Which of these is the Gibbs Free Energy equation?'},
    'History': {'Easy': 'Which country was not in World War 1?', 'Medium': "Who was the first US president to be impeached?", 'Hard': 'Who was the 5th President of the United States?'},
    'English': {"Easy": "Which of these was not written by Shakespeare?", "Medium": "Which of these was not written by Ernest Hemingway?", 'Hard': 'Who murdered Jay Gatsby in The Great Gatsby?'},
    'Technology': {"Easy": 'What does RAM stand for?', "Medium": 'What type of line is used to indicate symmetry?', "Hard": 'Which is not a type of gear?'},
    'Health': {'Easy': 'What does PPE stand for?', "Medium": "What's used to stop external bleeding?", "Hard": 'What is the depth of compression for infant CPR?'},
    'Math': {"Easy": "What is the formula for a parabola?", "Medium": "What is 0/0?", "Hard": 'What is the integral of dx/x?'}
}

def trivia_start():
    """Displays and initializes a trivia mini game for players to earn more money"""
    global picked_yet
    global difficulty
    global sub_picked
    global chosen_subject
    trivia_directions = font.render('Answer questions to earn more tears!', True, white)
    screen.blit(trivia_directions, (750, 50))
    y_triv = 200
    for number, subject in trivia_topics.items():
        trivia_options = font.render(f'{number}: {subject}', True, white)
        screen.blit(trivia_options, (750, y_triv))
        y_triv += 25
    
    cont = font.render("Once you've chosen, press enter", True, white)
    screen.blit(cont, (750, 400))
    if picked_yet == False:
        difficulty = ''
        pick_difficulty = font.render('Choose difficulty level: Easy (E), Medium (M), or Hard (H)', True, white)
        screen.blit(pick_difficulty, (750, 80))
        if keys[pygame.K_e]:
            difficulty = 'Easy'
            picked_yet = True
        elif keys[pygame.K_m]:
            difficulty = 'Medium'
            picked_yet = True
        elif keys[pygame.K_h]:
            difficulty = 'Hard'
            picked_yet = True
        if difficulty == '':
            return
    else:
        chosen_difficulty = font.render(f'Difficulty Level: {difficulty}', True, white)
        screen.blit(chosen_difficulty, (750, 80))

    if sub_picked == False:
        select_prompt = font.render('Pick your question.', True, white)
        screen.blit(select_prompt, (750, 150))
        chosen_subject = ''
        if keys[pygame.K_1]:
            chosen_subject = trivia_topics['1']
            sub_picked = True
        elif keys[pygame.K_2]:
            chosen_subject = trivia_topics['2']
            sub_picked = True
        elif keys[pygame.K_3]:
            chosen_subject = trivia_topics['3']
            sub_picked = True
        elif keys[pygame.K_4]:
            chosen_subject = trivia_topics['4']
            sub_picked = True
        elif keys[pygame.K_5]:
            chosen_subject = trivia_topics['5']
            sub_picked = True
        elif keys[pygame.K_6]:
            chosen_subject = trivia_topics['6']
            sub_picked = True
        if chosen_subject == '':
            return
    else:
        chosen_sub_text = font.render(f'You chose {chosen_subject}', True, white)
        screen.blit(chosen_sub_text, (750, 150))
    return

def display_question():
    """Display question and answer choices for trivia mini game"""
    global difficulty
    global chosen_subject
    chosen_question = trivia_questions[chosen_subject][difficulty]
    question = font.render(chosen_question, True, white)
    screen.blit(question, (750, 200))
    return


#START OF GAME CODE
scene = ''


# Main loop for game
while True:
    #Defines a variable relating to retrieving information about which keys are being pressed.
    keys = pygame.key.get_pressed()
    #if right arrow key is clicked, the shop opens.
    if keys[pygame.K_RIGHT]:
        scene = 'shop'
        run1 = True
    #if space is pressed, the prompt screen clears text by drawing black over it
    if keys[pygame.K_SPACE]:
        scene = 'clear'
    # Triggers the purchase screen after item is selected in the shop.
    if keys[pygame.K_RETURN] and scene == 'shop':
        scene = 'purchased'
    # Opens the trivia minigame to earn more money
    if keys[pygame.K_t]:
        scene = 'start trivia'
        sub_picked = False
        picked_yet = False
    # Prints question and answers if a question is chosen from the trivia page
    if keys[pygame.K_RETURN] and scene == 'start trivia':
        scene = 'question'
    for event in pygame.event.get():
        #check if current event is a quit event
        if event.type == pygame.QUIT:
            #quit program if the event is quit
            sys.exit()
    #draws background
    draw_back()
    #Welcomes the player to the game and explains some commands.
    if scene == '':
        welcome()
    #Opens the shop for the player to browse.
    if scene == 'shop':
        open_shop()
    # Activates purchase confirmation and updates money after something is bought.
    if scene == 'purchased':
        purchase()
    # Clears the text box on the right.
    if scene == 'clear':
        #draws over the sidebar
        pygame.draw.rect(screen, black, (sidebar["x"], sidebar["y"], sidebar["width"], sidebar["height"]))
    #starts trivia minigame
    if scene == 'start trivia':
        trivia_start()
    #gives player the trivia question and answers
    #if scene == 'question':
        #display_question()
    # Keep track of and display the amount of money available
    display_money()
    # Update display
    pygame.display.flip()