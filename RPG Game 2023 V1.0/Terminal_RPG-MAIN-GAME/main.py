# Role playing game
# Original J.Timmins 2018
# Updated W.Carr 2023
# Modified By T.Turner 2023

#---------------------------Import modules--------------------------------------

import random # Used to generate random numbers
from time import sleep # Used to add pauses in the game
import sys # Used for system commands such as exit()
from sys import exit
import json # Used for data handling

#---------------------------Variables------------------------------------------

# Lists used for the print statements to make the game more interesting and varied.
rooms = ["S1","S2","C3","C4","S5","E6","S7","S8","S9","S10","E2","N10",]
time = ["Morning","Afternoon","Evening","Night"]
Day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
attacks = ["Baffle","Elude","Missile","Trick","Lightning"]


# PAUSE is a constant variable which means it doesnt and can not be changed by the program.
# Defines the variables which are used later in the game
PAUSE = 1.3
lives = 10
turns = 0
your_score = 0
coins = 0
RNG_Chance = 6
your_attack_name = ""
number = 100
fight = False
pause_menu = True
Main_Game = False
GOD_MODE = False
username_list = []

#---------------------------Data Handling------------------------------------------

# Opens the json file in reading mode and loads the data into the config variable.
with open('config.json','r', encoding = 'UTF-8') as config_file:
    config = json.load(config_file)
    
# Pulls the usernames from the config file and appends them to the username_list.
for i in config:
    username_list.append(i)
    

#---------------------------Functions------------------------------------------
        
# Ingame shop where the user can purchase items with the coins earned from battles.
def shop(coins, RNG_Chance, Main_Game):
    
    # Makes a variable defined outside the function accessible inside the function.
    global GOD_MODE,number
    
    # Asks the user to input data and converts it to upper case to avoid erros/typos.
    shop_choice = input("Would you like to visit the shop? (y/n): ").upper()
    if shop_choice == "Y":
        
        # Menu GUI
        print("\n")
        print("Welcome to the shop, you have",coins,"coins!")
        print("\n")
        print("<-----ITEMS----->")
        print("\n")
        
        purchases = ["1: 10% damage boost - 40 coins","2: 20% damage boost - 70 coins","3: 30% damage boost - 100 coins",
                     "4: 40% damage boost - 150 coins","5: 50% damage boost - 170 coins","6: 5% chance of finding a secret character - 500 coins","7: God Mode - 1000 coins","8: Exit"]
        # Goes through each item in the list and prints it using an iteration loop.
        for i in purchases:
            print(i)
        print("\n")
        # Asks the user to input what they want to buy.
        purchase_choice = int(input("Enter an option to purchase: "))
        
        if purchase_choice == 1 and coins >= 40:
            # The RNG_Chance varaible is used to increase the chance of the user winning a battle.
            RNG_Chance += 0.6
            coins -= 40
            print("You have successfully purchased a 10% damage boost!")
            print("You now have:",coins,"coins! ")
        
        elif purchase_choice == 2 and coins >= 70:
            RNG_Chance += 1.2
            coins -= 70
            print("You have successfully purchased a 20% damage boost!")
            print("You now have:",coins,"coins! ")
        
        elif purchase_choice == 3 and coins >= 100:
            RNG_Chance += 1.8
            coins -= 100
            print("You have successfully purchased a 30% damage boost!")
            print("You now have:",coins,"coins! ")
        
        elif purchase_choice == 4 and coins >= 150:
            RNG_Chance += 2.4
            coins -= 150
            print("You have successfully purchased a 40% damage boost!")
            print("You now have:",coins,"coins! ")
        
        elif purchase_choice == 5 and coins >= 170:
            RNG_Chance += 3
            coins -= 170
            print("You have successfully purchased a 50% damage boost!")
            print("You now have:",coins,"coins! ")
            
        elif purchase_choice == 6 and coins >= 500:
            coins -= 500
            number = 95
            print("You have successfully purchased a 5% to find the secret character!")
            print("You now have:",coins,"coins! ")
            
        elif purchase_choice == 7 and coins >= 1000:
            coins -= 1000
            print("You have successfully purchased GOD MODE!")
            print("You now have:",coins,"coins! ")
            # God mode allows the user to win every battle.
            GOD_MODE = True
        elif purchase_choice == 8:
            Main_Game = True
        
        else:
            print("You do not have enough coins!")
            Main_Game = True
        
    else:
        pass
            
        # Returns RNG_Chance back to the main game so it can be used in the battle function.
        return RNG_Chance
    
# This bubble sort function orders the scores in the config file from highest to lowest and then prints them.
def leaderboard_bubble_sort():
    for i in range(len(config)):
        for amount in range(len(config) - i - 1):
            # This checks whether or not the score variable, which is differernt for each user, is higher than the next one. If so it swaps them.
            if config[username_list[amount]]["score"] < config[username_list[amount + 1]]["score"]:
                config[username_list[amount]], config[username_list[amount + 1]] = config[username_list[amount + 1]], config[username_list[amount]]
           
    print("\n")
    print("<----LEADERBOARD---->")
    print("\n")
    for name in config:
        print(name + ":" + str(config[name]["username"]) + " has a score of, " + str(config[name]["score"])+"!")  
        
    print("\n")
    # This prints the user with the highest score.
    print(config[username_list[0]]["username"] + " has the BEST score!")
    print("\n")
    
# Creates a class where the functions are stored, containing the ASCII art for the game.
class ASCII_Objects:
    
    def mr_smith():
        print(" Enemy           You")
        print("   ↓              ↓")
        print("")
        print(" (_oo>)")
        print("   |")
        print("   |              O")
        print("  /|\==)----     \|")
        print("   |              |")       
        print("   LL            ⅃⅃")
        
    def teacher():
        print(" Enemy      You")
        print("   ↓         ↓")
        print("")
        print(" _\|/^")
        print(" (_oo>)")
        print("   |")
        print("   |  /      O")
        print("  /|\/      \|")
        print("   |         |")       
        print("   LL       ⅃⅃")
        
    # Secret character with a low chance of spawning.
    def glitch():
        print("##Glitch##     You")
        print("    ↓           ↓")
        print("")
        print("  \.-./         O     ")
        print("  [o.o]     \. .|    ")
        print("  |###|         |     ")
        print("  |___|         |     ")
        print("./_____\.      ⅃⅃      ") 
        print("\n")     
    
#---------------------------Main game----------------------------------------

# Creates an interactable menu by using the input() fucntion.
print("<------Main Menu------>")
print("\n")
print("1: <-----PLAY----->")
print("2: <----OPTIONS---->")
print("3: <-----QUIT----->")
print("\n")
choice = int(input("Enter an option: "))

# If the user  enters 1, it will set the Main_Game boolean to True, which will allow the game to run.
if choice == 1:
    Main_Game = True
# I the user enters 2, then it will display an options menu, using print statements.  
elif choice == 2:
    print("\n")
    print("<----OPTIONS---->")
    print("1: Disable Pause Menu after each round")
    print("2: Leaderboard")
    print("3: To be added...")
    print("\n")
    
    options_choice = int(input("Enter an option: "))
    # If the user wants to disable the pause menu, then it will set the pause_menu boolean to False. Later on in the code this variable needs to be set to True for the
    # pause menu to run.
    if options_choice == 1:
        pause_menu = False
        Main_Game = True
    elif options_choice == 2:
        leaderboard_bubble_sort()
        # This allows the user to choose when to let the game run again so the user has time to read the leaderboard.
        leaderboard_choice = input("Would you like to return to the main game? (y/n): ").upper()
        if leaderboard_choice == "Y":
            Main_Game = True
        else:
            exit(0)  

        
    elif options_choice == 3:
        Main_Game = True
        
elif choice == 3:
    # Uses sys to exit the program.
    exit(0)

else:
    print("Invalid Option!")

# Main Game loop, this is where the game runs.
if Main_Game == True:
    
    # This game uses a username to make the game more personal and enjoyable.
    username = str(input("Enter your username: "))
    print("\n")
    print("Welcome, " + username + "!")
   
    # This creates an iteration loop which will repeat while the loop is True, this while loop never stops running because the loop is forever set to True.
    while True:

        turns += 1
        glitch_chance = random.randint(0,number)
        
        # If the score variable is less than 3 it will create a random number from 0 to 2 in the spawn variable then the same for less than 5. 
        # randint can be broken down into 'random integer' which can be used to generate this random number.
        # Randomly genreates an amount of coins to give to the user if they win. It is different depending on the score to allow for a more gradual progression.
        if your_score < 3:
            spawn = random.randint(0,3)
            random_coins = random.randint(0,12)
        elif your_score < 5:
            spawn = random.randint(0,4)
            random_coins = random.randint(0,8)
        else:
            spawn = random.randint(0,6)
            random_coins = random.randint(0,4)
            
        # Checks whether or not the randomly generated number is the same as the glitch chance, if it is then it will set the spawn variable to 7, which is "glitch" in the teacherList.
        if glitch_chance == 10:
            spawn = 7

        # Depending on the spawn variable, it will set the opponent variable to a different name in the teacherList.
        teacherList = ["Mr Smith","Mr Cammack","Mr Birchall","Mr Soulsby","Mr Carr","Mrs Brennan","Lord Timmins of Mobberley","Glitch"]
        opponent = teacherList[spawn]
        
        print("\n")# creates a new line
        print("Turn: " + str(turns))# turns the turn variable into a string then prints it in the format Turn: x
        print("Score: " + str(your_score))# turn the your_score variable into a variable then displays it in the format Score: x and prints it
        print("Coins: " + str(coins))
        print("\n")
        sleep(PAUSE)# Uses time module to make the program wait for a second
        print("It is a dark time for students")# prints a statement
        print("It is the,",random.choice(time))
        print("The day is,",random.choice(Day))
        sleep(PAUSE)# Uses time module to make the program wait for a second
        print("You wander nervously through the hallowed halls of")# prints a statement
        print("Altrincham Grammar School for Boys")# prints a statement
        sleep(PAUSE)# Uses time module to make the program wait for a second
        print("Dark creatures stalk the corridors")# prints a statement
        print()
        sleep(PAUSE)# Uses time module to make the program wait for a second
        print("Out of the shadow of,",random.choice(rooms),"steps...")# prints a statement
        sleep(PAUSE)# Uses time module to make the program wait for a second
        print(opponent+"!")# Grabs the opponent variable and prints it with an exclamation mark after it
        sleep(PAUSE)# Uses time module to make the program wait for a second
        print("\n")# creates a new line
        
        # Prints out an ASCII character by calling the appropriate function from the ASCII_Objects class.
        if opponent == "Mr Smith":
            ASCII_Objects.mr_smith()
        elif opponent == "Glitch":
            ASCII_Objects.glitch()
        else:  
            ASCII_Objects.teacher()
        
        # Creates 3 random attacks from the attacks list and stores them in the attack_list list.
        attack_list = []
        for i in range(3):
            attack_list.append(random.choice(attacks))
         
        # The while loop checks if any of the attacks are the same, if they are then it will clear the attack_list and generate 3 new attacks.   
        while attack_list[0] == attack_list[1] or attack_list[0] == attack_list[2] or attack_list[1] == attack_list[2]:
            attack_list.clear()
            for i in range(3):
                attack_list.append(random.choice(attacks))
            
        # Prints out the attacks.
        print("1: <-----",attack_list[0],"----->")
        print("2: <-----",attack_list[1],"----->")
        print("3: <-----",attack_list[2],"----->")
        print("4: <-----Run----->")
        print("\n")
        
  
        
        choice = input("> ")# Asks the user for an input in the variable choice and stores it.
        
        if choice == "1":
            your_attack = (random.randint(1,RNG_Chance))
            your_attack_name = attack_list[0]
            fight = True
        elif choice == "2":
            your_attack = (random.randint(1,RNG_Chance))
            your_attack_name = attack_list[1]
            fight = True
        elif choice == "3":
            your_attack = (random.randint(1,RNG_Chance))
            your_attack_name = attack_list[2]
            fight = True
        # If the user chooses to run the fight variable will be set to False which means that it will print the running away statements.
        elif choice == "4":
            fight = False

        # Depending on the previous choice the user made, the game will make a decision to either run the fight code or the run away code, this gets decided by the boolean variable
        # fight.
        if fight == False:
            
            print("You run away, a wise choice")
            sleep(PAUSE)
            lives -= 1
            print("You now have " + str(lives) + " lives left!")
            
            if lives == 0:
                print("\n")
                print("You have no lives left!")
                sleep(PAUSE)
                print("Game Over!")
                exit(0)
            
        elif fight == True:
            print("Be prepared to meet your doom,",username,"...")
            sleep(PAUSE)
            # Pauses the program for 1 second using the sleep function
    
            opponent_attack = random.randint(0,2) + spawn

            # Checks whether or nto the user has GOD_MODE enabled.
            if GOD_MODE == True:
                your_attack = 100000
                
            # If your_attack variable is greater than the opponent_attack variable it runs a program.
            if your_attack > opponent_attack:
                print(username,"does,",your_attack_name,",on",opponent,"!")# prints an attack message
                print("\n")
                print("You fight...")
                sleep(2.5) # Uses pauses to add suspense to the game.
                print("You win!")
                sleep(PAUSE)
                print(opponent + " is defeated!")# Prints the person you were againsted(opponent) is defeated.
                # Adds a random amount of coins defined earlier to the total coins variable.
                coins += random_coins
                
                # If the user wins against Glitch you get lots more coins, 250.
                if opponent == "Glitch":
                    coins += 250
                your_score += (spawn+1)
                print("You have " + str(lives) + " lives left!")
                
            else:
                print(username,"does,",your_attack_name,",on",opponent,"!")# prints an attack message
                print("\n")
                print("You fight...")
                sleep(2.5) # Adds a pause to add suspense to the game.
                print("You lose!")
                sleep(PAUSE)
                lives -= 1
                print("You have " + str(lives) + " lives left!")
                
                # If the user runs out of lives then the game will end.
                if lives == 0:
                    print("\n")
                    print("You have no lives left!")
                    sleep(PAUSE)
                    print("Game Over!")
                    exit(0)

              
        if pause_menu == True:
            print("\n")
            print("<-----Pause Menu----->")
            print("1: Continue")
            print("2: Shop")
            print("3: Leaderboard")
            print("4: Exit")
            print("\n")
            pause_menu_choice = int(input("Enter an option: "))
        
            if pause_menu_choice == 3:
                leaderboard_bubble_sort()
                # This allows the user to choose when to let the game run again so the user has time to read the leaderboard.
                leaderboard_choice = input("Would you like to return to the main game? (y/n): ").upper()
                if leaderboard_choice == "Y":
                    Main_Game = True
                else:
                    exit(0)  
                    
            # If the user selects the exit option it will use a function from the library, sys, to exit the program.
            elif pause_menu_choice == 4:
                exit(0)
           
            # Checks whether or not the user has selected to view the shop GUI and whether or not the user has disabled this menu in options.
            if pause_menu == True and pause_menu_choice == 2:
                # This function uses a variable so it is easier to return back into the main game.
                a = shop(coins,RNG_Chance,Main_Game)
                #print(GOD_MODE) # Debug code
                
# If any data is in the wrong formating the game will print an error message and exit the program.
else:
    print("Invalid Option!")