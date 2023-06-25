# Import all the packages needed for the game
import os
from typing import KeysView
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Removes pygame welcome message
import pygame
import random
import time
import sys

# Creates an FPS System for pygame and creates a speed variable used later for character movement
FPS=60
clock=pygame.time.Clock()
vel = 4

#test
all_fonts = [['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambria', 'cambriamath', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhenghei', 'microsoftjhengheiui', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyahei', 'microsoftyaheiui', 'microsoftyibaiti', 'mingliuextb', 'pmingliuextb', 'mingliuhkscsextb', 'mongolianbaiti', 'msgothic', 'msuigothic', 'mspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'sansserifcollection', 'segoefluenticons', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'segoeuivariable', 'simsun', 'nsimsun', 'simsunextb', 'sitkatext', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothic', 'yugothicuisemibold', 'yugothicui', 'yugothicmedium', 'yugothicuiregular', 'yugothicregular', 'yugothicuisemilight', 'holomdl2assets', 'agencyfb', 'algerian', 'bookantiqua', 'arialrounded', 'baskervilleoldface', 'bauhaus93', 'bell', 'bernardcondensed', 'bodoni', 'bodoniblack', 'bodonicondensed', 'bodonipostercompressed', 'bookmanoldstyle', 'bradleyhanditc', 'britannic', 'berlinsansfb', 'berlinsansfbdemi', 'broadway', 'brushscript', 'bookshelfsymbol7', 'californianfb', 'calisto', 'castellar', 'centuryschoolbook', 'centaur', 'century', 'chiller', 'colonna', 'cooperblack', 'copperplategothic', 'curlz', 'dubai', 'dubaimedium', 'dubairegular', 'elephant', 'engravers', 'erasitc', 'erasdemiitc', 'erasmediumitc', 'felixtitling', 'forte', 'franklingothicbook', 'franklingothicdemi', 'franklingothicdemicond', 'franklingothicheavy', 'franklingothicmediumcond', 'freestylescript', 'frenchscript', 'footlight', 'garamond', 'gigi', 'gillsans', 'gillsanscondensed', 'gillsansultracondensed', 'gillsansultra', 'gloucesterextracondensed', 'gillsansextcondensed', 'centurygothic', 'goudyoldstyle', 'goudystout', 'harlowsolid', 'harrington', 'haettenschweiler', 'hightowertext', 'imprintshadow', 'informalroman', 'blackadderitc', 'edwardianscriptitc', 'kristenitc', 'jokerman', 'juiceitc', 'kunstlerscript', 'widelatin', 'lucidabright', 'lucidacalligraphy', 'leelawadee', 'lucidafaxregular', 'lucidafax', 'lucidahandwriting', 'lucidasansregular', 'lucidasansroman', 'lucidasanstypewriterregular', 'lucidasanstypewriter', 'lucidasanstypewriteroblique', 'magneto', 'maiandragd', 'maturascriptcapitals', 'mistral', 'modernno20', 'microsoftuighur', 'monotypecorsiva', 'extra', 'niagaraengraved', 'niagarasolid', 'ocraextended', 'oldenglishtext', 'onyx', 'msoutlook', 'palacescript', 'papyrus', 'parchment', 'perpetua', 'perpetuatitling', 'playbill', 'poorrichard', 'pristina', 'rage', 'ravie', 'msreferencesansserif', 'msreferencespecialty', 'rockwellcondensed', 'rockwell', 'rockwellextra', 'script', 'showcardgothic', 'snapitc', 'stencil', 'twcen', 'twcencondensed', 'twcencondensedextra', 'tempussansitc', 'vinerhanditc', 'vivaldi', 'vladimirscript', 'wingdings2', 'wingdings3', 'roboto', 'cascadiacoderegular', 'cascadiamonoregular']]

for font in all_fonts:
    pass

# Initialises features for pygame, and creates a pygame window with a caption/title
pygame.init()
pygame.font.init()
Resolution = (1080,720)
WIN = pygame.display.set_mode(Resolution)
Caption = pygame.display.set_caption("RPG Game V1.0")
Logo = pygame.image.load("Assets/Main_Menu/Icon.png")
pygame.display.set_icon(Logo)

Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
jumping = False

# Creates a scene handler which the main drawing function will use to manage what is currently displayed on the screen
scene = 1

# Variables for the health system
health = 5
old_health_time = 0
curr_health_time = 0


# Stores the width and height of the pygame window in variables
Screen_Width = WIN.get_width()
Screen_Height = WIN.get_height()

# Define some colours
class colours:
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    grey = (128,128,128)
    blue = (0,0,255)
    yellow = (255,255,0)
    cyan = (0,255,255)
    magenta = (255,0,255)
    orange = (255,165,0)
    

# Loads all the images needed for the game, and changes the size of them to fit the game   

background_image = pygame.image.load("Assets/Main_Menu/background_image.png")

Plus = pygame.image.load("Assets/Main_Menu/PLUS.png")
Plus = pygame.transform.scale(Plus, (80,80))

Minus = pygame.image.load("Assets/Main_Menu/MINUS.png")
Minus = pygame.transform.scale(Minus, (80,80))

Main_Game_Background = pygame.image.load("Assets/Main_Game/Main_Scene_Background.png")

Vender_Sprite = pygame.image.load("Assets/Main_Game/Vender_Sprite.png")
Vender_Sprite = pygame.transform.scale(Vender_Sprite, (65,100))

Main_character = pygame.image.load("Assets/Main_Game/Main_IDLE.png")
Main_character = pygame.transform.scale(Main_character, (58,90))

# Loads the images used for buttons
Play_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Play_Button = pygame.transform.scale(Play_Button, (350,100))

Options_Button = pygame.image.load("Assets/Main_Menu/Options_Button.png")
Options_Button = pygame.transform.scale(Options_Button, (350,100))

Quit_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Quit_Button = pygame.transform.scale(Quit_Button, (350,100))

Controls_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Controls_Button = pygame.transform.scale(Controls_Button, (400,100))

Back_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Back_Button = pygame.transform.scale(Back_Button, (350,100))

Resume_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Resume_Button = pygame.transform.scale(Resume_Button, (350,100))

Audio_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Audio_Button = pygame.transform.scale(Audio_Button, (350,100))

Volume_UP_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Volume_UP_Button = pygame.transform.scale(Volume_UP_Button, (90,90))

Volume_DOWN_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Volume_DOWN_Button = pygame.transform.scale(Volume_DOWN_Button, (90,90))

# Loads images for a health system
Full_Health = pygame.image.load("Assets/Health-Bar/Full-Bar.png")
Full_Health = pygame.transform.scale(Full_Health, (350,50))

Four_Health = pygame.image.load("Assets/Health-Bar/4-5.png")
Four_Health = pygame.transform.scale(Four_Health, (350,50))

Three_Health = pygame.image.load("Assets/Health-Bar/3-5.png")
Three_Health = pygame.transform.scale(Three_Health, (350,50))

Two_Health = pygame.image.load("Assets/Health-Bar/2-5.png")
Two_Health = pygame.transform.scale(Two_Health, (350,50))

One_Health = pygame.image.load("Assets/Health-Bar/1-5.png")
One_Health = pygame.transform.scale(One_Health, (350,50))

Zero_Health = pygame.image.load("Assets/Health-Bar/0-5.png")
Zero_Health = pygame.transform.scale(Zero_Health, (350,50))

Heart = pygame.image.load("Assets/Health-Bar/Heart.png")
Heart = pygame.transform.scale(Heart, (45,45))

# Draw text on the buttons by creating a font then creating a function to draw the text on the buttons

def draw_text(text,text_col,x,y,font_size):
        text_font = pygame.font.SysFont("arialblack", font_size)
        img = text_font.render(text,True,text_col)
        WIN.blit(img,(x,y))

def calibri_font(text,text_col,x,y,font_size):
        text_font = pygame.font.SysFont("calibri", font_size)
        img = text_font.render(text,True,text_col)
        WIN.blit(img,(x,y))

# Define some coordinates used for object locations
class coordinates:
    m_x = 50
    m_y = 399

# Bubble sort Function
def bubble_sort():
    test = [5,7,3,10,8]
    for i in test:
        if test[i] > test[i+1]:
            pass

# Functions used to draw things on the screen
def home_screen_drawing():
    WIN.fill(colours.orange)
    WIN.blit(background_image, (0,0))
    WIN.blit(Play_Button, (365,105))
    WIN.blit(Options_Button, (365,310))
    WIN.blit(Quit_Button, (365,515))
    draw_text("PLAY", (0,0,0), 450, 110,60)
    draw_text("OPTIONS", (0,0,0), 390 , 310,60)
    draw_text("QUIT", (0,0,0), 450, 515,60)

def options_screen_drawing():
    WIN.blit(background_image, (0,0))
    WIN.blit(Audio_Button, (365,105))
    WIN.blit(Controls_Button, (340,310))
    WIN.blit(Back_Button, (365,515))
    draw_text("AUDIO", (0,0,0), 430, 110,60)
    draw_text("CONTROLS", (0,0,0), 355 , 313,60)
    draw_text("BACK", (0,0,0), 445, 515,60)

def pause_screen_drawing():
    WIN.blit(background_image, (0,0))
    WIN.blit(Resume_Button, (365,105))
    WIN.blit(Options_Button, (365,310))
    WIN.blit(Quit_Button, (365,515))
    draw_text("RESUME", (0,0,0), 400, 110,60)
    draw_text("OPTIONS", (0,0,0), 390 , 310,60)
    draw_text("QUIT", (0,0,0), 450, 515,60)

def main_game_drawing():
   
    global scene
    # First scene of the program
    if scene == 1:
        WIN.fill(colours.black)
        pygame.display.update()
        pygame.time.delay(1000)
        
        draw_text("It is a dark time.", (255,255,255), 370, 110 ,30)
        pygame.display.update()
        pygame.time.delay(1000)
        
        draw_text("You wander through the desserted lands of Thornhollow.", (255,255,255), 90, 220,30)
        pygame.display.update()
        pygame.time.delay(1000)
        
        draw_text("Dark creatures stalk the land.", (255,255,255), 270, 330,30)
        pygame.display.update()
        pygame.time.delay(1000)
        
        draw_text("You challenge them...", (255,255,255), 330, 440,30)
        pygame.display.update()
        pygame.time.delay(1000)

        scene = 2
        
    # Second scene of the program
    elif scene == 2:
        
        WIN.blit(Main_Game_Background, (0,0))
        WIN.blit(Vender_Sprite, (850,389))
        #pygame.display.update()
        character_controller()
        WIN.blit(Main_character, (coordinates.m_x,coordinates.m_y))
        is_Vender = False
        if coordinates.m_x > 770 and coordinates.m_x < 950 and is_Vender == False:
            calibri_font("Interact 'E'",(0,0,0),835,350,26)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            is_Vender = True
        
        pygame.display.update()

# undertale style
        
    
def audio_screen_drawing():
    WIN.blit(background_image, (0,0))
    WIN.blit(Back_Button, (365,515))
    WIN.blit(Volume_UP_Button, (700,240))
    WIN.blit(Volume_DOWN_Button, (300,240))
    WIN.blit(Plus, (705,244))
    WIN.blit(Minus, (305,244))
    draw_text("BACK", (0,0,0), 445, 515,60)
    draw_text("VOLUME", (0,0,0), 400, 240,60)
    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if Volume_UP_Button.get_rect(topleft=(700,240)).collidepoint(mouse):
        increse_audio()
    if Volume_DOWN_Button.get_rect(topleft=(305,240)).collidepoint(mouse):
        decrese_audio()

def controls_screen_drawing():
    WIN.blit(background_image, (0,0))
    WIN.blit(Back_Button, (365,515))
    draw_text("BACK", (0,0,0), 445, 515,60)
    draw_text("UP - W", (0,0,0), 250 , 75,40)
    draw_text("LEFT - A", (0,0,0), 250 , 125,40)
    draw_text("DOWN - S", (0,0,0), 250 , 175,40)
    draw_text("RIGHT - D", (0,0,0), 250 , 225,40)
    draw_text("CAST SPELL - Q", (0,0,0), 250 , 275,40)
    


# Checks if the ESCAPE key is pressed to then display a pause screen
def PAUSE_MENU():
    global WINDOW_STATE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        WINDOW_STATE="Pause_screen" 
        pygame.display.update()
    
class Drawings:
    """This class is used for drawing all the images and text on the screen"""
    def home_screen():
        """This method is used for drawing the home screen"""
        pass
    def options_screen():
        pass
    def play_screen():
        pass
    def audio_screen():
        pass
    def controls_screen():
        pass
    
        
# Creates a basic character controller
def character_controller():
    global jumping
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and coordinates.m_x > 0:
        coordinates.m_x -= vel
    if keys[pygame.K_d] and coordinates.m_x < 1025:
        coordinates.m_x += vel
    
    if keys[pygame.K_SPACE]:
        jumping=True
        
# Loads the sound from the Assets library and loops/plays it in a sub program
my_sound = pygame.mixer.Sound("Assets/Main_Menu/Backing Clipped.mp3")
def audio():
    global my_sound
    my_sound.play(loops=-1) # Loops the audio 
    my_sound.set_volume(0.5)# Sets the volume of the audio

# Function to increse audio
def increse_audio():
    global my_sound
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            my_sound.set_volume(my_sound.get_volume()+0.05)
            
# Function to decrease audio
def decrese_audio():
    global my_sound
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            my_sound.set_volume(my_sound.get_volume()-0.05)
               
# Creates a health system which may oro not be used in the game
def Health_System():
    global health
    global old_health_time
    global curr_health_time
    curr_health_time = time.time()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        if curr_health_time - old_health_time > 5:
            print("debug key f was pressed")
            old_health_time = time.time()
            health -= 1
    

# Checks if and when the mouse is clicked where it is on the screen and how it should respond to it
def Has_mouse_clicked(Button: pygame.Surface, button_x: int, button_y: int):
    mouse_pos = pygame.mouse.get_pos()
    if Button.get_rect(topleft=(button_x,button_y)).collidepoint(mouse_pos):
        return True
    else:
        return False
    
WINDOW_STATE = "Home_screen"

# Main function where the main parts of the game are run
def main():
    
    global WINDOW_STATE, Y_VELOCITY, jumping
    # clock.tick(FPS)
    run=True
    audio()
    
    
    while run: # Main game loop
        
        for event in pygame.event.get(): # Creates an event handler which is constantly checking for a pygame event

            if event.type == pygame.QUIT:
                # Has the user closed the window?
                run = False
                pygame.quit()
                sys.exit()
            
            
            # Check is the user has pressed the mouse button/left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                # -------------> Home Screen <-----------------
                
                if WINDOW_STATE == "Home_screen":
                    
                    if Has_mouse_clicked(Play_Button, 365, 105):
                        
                        WINDOW_STATE="Play_screen"
                        WIN.fill(colours.black)

                    elif Has_mouse_clicked(Options_Button, 365, 310):
                        WINDOW_STATE="Options_screen"

                    elif Has_mouse_clicked(Quit_Button, 365, 515):
                        pygame.quit()
                        sys.exit()

                #-------------> Options Screen <-----------------

                elif WINDOW_STATE == "Options_screen":
                    if Has_mouse_clicked(Audio_Button, 365, 105):
                        WINDOW_STATE="Options_screen::Audio"

                    elif Has_mouse_clicked(Controls_Button, 365, 310):
                        WINDOW_STATE="Options_screen::Controls"

                    elif Has_mouse_clicked(Back_Button, 365, 515):
                        WINDOW_STATE="Home_screen"

                elif WINDOW_STATE == "Options_screen::Audio":
                    if Has_mouse_clicked(Back_Button, 365, 515):
                        print("Back Button Clicked")
                        WINDOW_STATE="Options_screen"

                elif WINDOW_STATE == "Options_screen::Controls":
                    if Has_mouse_clicked(Back_Button, 365, 515):
                        print("Back Button Clicked")
                        WINDOW_STATE="Options_screen"

                #-------------> Pause Screen <-----------------

                elif WINDOW_STATE == "Pause_screen":
                    if Has_mouse_clicked(Resume_Button, 365, 105):
                        WINDOW_STATE="Play_screen"

                    elif Has_mouse_clicked(Options_Button, 365, 310):
                       WINDOW_STATE="Pause_screen::Options"

                    elif Has_mouse_clicked(Quit_Button, 365, 515):
                        pygame.quit()
                        sys.exit()

                elif WINDOW_STATE == "Pause_screen::Options":
                    if Has_mouse_clicked(Audio_Button, 365, 105):
                        WINDOW_STATE="Pause_screen::Audio"

                    elif Has_mouse_clicked(Controls_Button, 365, 310):
                        WINDOW_STATE="Pause_screen::Controls"

                    elif Has_mouse_clicked(Back_Button, 365, 515):
                        WINDOW_STATE="Pause_screen"

                elif WINDOW_STATE == "Pause_screen::Audio": 
                    if Has_mouse_clicked(Back_Button, 365, 515):
                        WINDOW_STATE="Pause_screen"

                elif WINDOW_STATE == "Pause_screen::Controls":
                    if Has_mouse_clicked(Back_Button, 365, 515):
                        WINDOW_STATE="Pause_screen"
                
        
            #-------------> Drawing State <-----------------
            
        if WINDOW_STATE=="Home_screen":
            home_screen_drawing()
                
        elif WINDOW_STATE=="Play_screen":
            main_game_drawing()
        
        elif WINDOW_STATE=="Pause_screen":
            pause_screen_drawing()
                
                        
        elif WINDOW_STATE=="Options_screen" or WINDOW_STATE == "Pause_screen::Options":
            options_screen_drawing()
                

        elif WINDOW_STATE=="Options_screen::Audio" or WINDOW_STATE=="Pause_screen::Audio":
            audio_screen_drawing()
            
        elif WINDOW_STATE=="Options_screen::Controls" or WINDOW_STATE=="Pause_screen::Controls":
            controls_screen_drawing()
        
        
        if jumping:
            coordinates.m_y -= Y_GRAVITY
            Y_VELOCITY -= Y_GRAVITY
            
            if Y_VELOCITY < -JUMP_HEIGHT:
                jumping = False
                Y_VELOCITY = JUMP_HEIGHT
            WIN.blit(Main_character, (coordinates.m_x,coordinates.m_y))
        else:
            pass
            
        
        
            
        health = Health_System()
        PAUSE_MENU()
        
        pygame.display.update()
        clock.tick(FPS)
        
        
    pygame.quit() 

if __name__ == "__main__":# Calls the main function
    main()


# Credit:
# 
# Assets:
# https://github.com/baraltech/Menu-System-PyGame/tree/main/assets - Main Menu