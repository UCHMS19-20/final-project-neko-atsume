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
        if run1 == True:
            if tears < prices[chosen_item]:
                #calculates how much more money you need to buy the item
                difference = prices[chosen_item] - tears
                broke = font.render(f'Sorry, you are short {difference} tears.', True, white)
                screen.blit(broke, (750, 100))
                return
            elif tears >= prices[chosen_item]:
                #update money 
                tears -= prices[chosen_item]
                #add bought item to your inventory
                inventory.append(chosen_item)
                #Prevents code from updating tears and inventory for every iteration
                run1 = False
        # Display what item the player bought
        purchase_complete = font.render(f'You have purchased {chosen_item}', True, white)
        #Print purchase message
        screen.blit(purchase_complete, (750, 100))
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
    '3': 'Health',
    '4': 'Math'
}
#dictionary of all the topics and their questions for trivia minigame
trivia_questions = {
    'Science': {'Easy': "What is Newton's Second Law?", 'Medium': "What is absolute zero in Celsius?", "Hard": 'Which of these is the Gibbs Free Energy equation?'},
    'History': {'Easy': 'Which country was not in World War 1?', 'Medium': "Who was the first US president to be impeached?", 'Hard': 'Who was the 5th President of the United States?'},
    'Health': {'Easy': 'What does PPE stand for?', "Medium": "What's used to stop external bleeding?", "Hard": 'What is the depth of compression for infant CPR?'},
    'Math': {"Easy": "What is the formula for a parabola?", "Medium": "What is 0/0?", "Hard": 'What is the integral of dx/x?'}
}

#dictionaries of answer choices for the trivia questions
science_easy = {'A. Inertia': 'wrong', 'B. F=ma': 'correct', 'C. Equal/opposite forces': 'wrong', 'D. Conservation of energy': 'wrong'}
science_med = {'A. 273': 'correct', 'B. 298': 'wrong', 'C. 225': 'wrong', 'D. 330': 'wrong'}
science_hard = {'A. q=mcT': 'wrong', 'B. PV=nRT': 'wrong', 'C. v=dx/dt': 'wrong', 'D. G= H-TS': 'correct'}
history_easy = {'A. USA': 'wrong', 'B. Germany': 'wrong', 'C. Spain': 'correct', 'D. Austro-Hungary': 'wrong'}
history_med = {'A. Richard Nixon': 'wrong', 'B. Andrew Johnson': 'correct', 'C. Bill Clinton': 'wrong', 'Donald Trump': 'wrong'}
history_hard = {'A. John Quincy Adams': 'wrong', 'B. James Madison': 'wrong', 'C. Martin Van Buren': 'wrong', 'D. James Monroe': 'correct'}
health_easy = {'A. Personal Protective Equipment': 'correct', 'B. Private Protective Equipment': 'wrong', 'C. Private Political Endorsement': 'wrong', 'D. Pressure Point Equilibrium': 'wrong'}
health_med = {'A. Ice': 'wrong', 'B. Tourniquet': 'correct', 'C. Splint': 'wrong', 'D. CPR': 'wrong'}
health_hard = {'A. 2 inches': 'wrong', 'B. 1.5 inches': 'correct', 'C. 1 inch': 'wrong', 'D. As far as you can go': 'wrong'}
math_easy = {'A. |x|': 'wrong', 'B. x': 'wrong', 'C. ln(x)': 'wrong', 'D. x^2': 'correct'}
math_med = {'A. Undefined': 'wrong', 'B. Indeterminate': 'correct', 'C. 1': 'wrong', 'D. dx': 'wrong'}
math_hard = {'A. 1/x': 'wrong', 'B. 1': 'wrong', 'C. e^x': 'wrong', 'D. ln(x)': 'correct'}


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
        if chosen_subject == '':
            return
    else:
        chosen_sub_text = font.render(f'You chose {chosen_subject}', True, white)
        screen.blit(chosen_sub_text, (750, 150))
    return


def print_answers(list):
    """Print answer choices for the player to choose from"""
    global difficulty
    global chosen_subject
    y_ans = 200
    for ans_choice in list:
        listed_ans = font.render(f'{ans_choice}', True, white)
        screen.blit(listed_ans, (825, y_ans))
        y_ans += 25
    return

def display_question():
    """Display question and answer choices for trivia mini game"""
    global difficulty
    global chosen_subject
    chosen_question = trivia_questions[chosen_subject][difficulty]
    question = font.render(chosen_question, True, white)
    screen.blit(question, (750, 100))
    # depending on which question was chosen, it will display the answer choices
    ans_dict = science_easy
    if chosen_question == trivia_questions['Science']['Easy']:
        print_answers(science_easy)
        # defines which dictionary the answers come from
        ans_dict = science_easy
    elif chosen_question == trivia_questions['Science']['Medium']:
        print_answers(science_med)
        ans_dict = science_med
    elif chosen_question == trivia_questions['Science']['Hard']:
        print_answers(science_hard)
        ans_dict = science_hard
    elif chosen_question == trivia_questions['History']['Easy']:
        print_answers(history_easy)
        ans_dict = history_easy
    elif chosen_question == trivia_questions['History']['Medium']:
        print_answers(history_med)
        ans_dict = history_med
    elif chosen_question == trivia_questions['History']['Hard']:
        print_answers(history_hard)
        ans_dict = history_hard
    elif chosen_question == trivia_questions['Health']['Easy']:
        print_answers(health_easy)
        ans_dict = health_easy
    elif chosen_question == trivia_questions['Health']['Medium']:
        print_answers(health_med)
        ans_dict = health_med
    elif chosen_question == trivia_questions['Health']['Hard']:
        print_answers(health_hard)
        ans_dict = health_hard
    elif chosen_question == trivia_questions['Math']['Easy']:
        print_answers(math_easy)
        ans_dict = math_easy
    elif chosen_question == trivia_questions['Math']['Medium']:
        print_answers(math_med)
        ans_dict = math_med
    elif chosen_question == trivia_questions['Math']['Hard']:
        print_answers(math_hard)
        ans_dict = math_hard
    return ans_dict

def your_answer():
    """Displays which answer the player picked"""
    global picked_an_ans
    global letter
    global ans_chosen
    cont = font.render("Once you've chosen, press RIGHT ARROW KEY", True, white)
    screen.blit(cont, (800, 400))
    if picked_an_ans == False:
        letter = ''
        ans_chosen = ''
        if keys[pygame.K_a]:
            letter = 'A'
            # defines which option the player chose from the dictionary
            ans_chosen = list(display_question())[0]
            picked_an_ans = True
        if keys[pygame.K_b]:
            letter = 'B'
            ans_chosen = list(display_question())[1]
            picked_an_ans = True
        if keys[pygame.K_c]:        
            letter = 'C'
            ans_chosen = list(display_question())[2]
            picked_an_ans = True
        if keys[pygame.K_d]:
            letter = 'D'
            ans_chosen = list(display_question())[3]
            picked_an_ans = True
    else:
        display_your_ans = font.render(f'You answered: {letter}', True, white)
        screen.blit(display_your_ans, (800, 350))
    return ans_chosen

def validate_answer():
    """Check if the player's trivia answer was correct and display corresponding message."""
    global ans_chosen
    global ans_dict
    global difficulty
    global tears
    global run1_trivia
    # define the dictionary that corresponds with the chosen question
    ans_dict = display_question()

    #default tears earned for correct answer is 50 (easy)
    tears_earned = 50
    # for medium difficulty, 100 tears earned
    if difficulty == 'Medium':
        tears_earned = 100
    # for hard difficulty, 200 tears earned
    elif difficulty == 'Hard':
        tears_earned = 200
    
    # check and display whether or not the answer was correct
    if ans_dict[ans_chosen] == 'correct':
        correct_ans = font.render(f'You answered correctly! +{tears_earned} tears', True, white)
        screen.blit(correct_ans, (800, 350))
        # only add tears once
        if run1_trivia == True:
            tears += tears_earned
            run1_trivia = False
    else:
        correct_ans = font.render('Your answer was incorrect.', True, white)
        screen.blit(correct_ans, (800,350))
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
        picked_an_ans = False
    if keys[pygame.K_RIGHT] and scene == 'question':
        scene = 'answered'
        run1_trivia = True
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
    if scene == 'question':
        display_question()
        your_answer()
    #checks the player's trivia answer and updates money if correct
    if scene == 'answered':
        validate_answer()
    # Keep track of and display the amount of money available
    display_money()
    # Update display
    pygame.display.flip()