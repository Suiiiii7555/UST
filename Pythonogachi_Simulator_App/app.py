import random
class Creature:
    """ A Simple Tomogachi Clone """
    def __init__(self, name):
        """ Initilization of attributes """
        self.name = name.title()

        ## ATTRIBUTES TO TRACK PLAYING THE GAME (0 - 10)
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        self.food = 2 # Represents food inventory
        self.is_sleeping = False #Represents if the creature is sleeping or not
        self.is_alive = True #Represents if thee creature is alive or not  

    def eat(self):
        """ Simulate eating each time you eat it takes one food from inventory
            In case of a bad meal then one point taken from hunger
        """
        ## First make sure if food is available
        if self.food < 0:
            self.food -=  1
            self.hunger -= random.randint(1, 4)
            print("Yum!",self.name,"ate a great meal!")
        else:
            print(self.name+"doesn't have any food! Better forage for some")
        # If the hunger is less than 0 set it to 0
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        """ Play a guessing game to lower the creatures boredom 
             If you win the game boredom decreases, loswer boredom even more
        """
        ## Simple guessing game
        value = random.randint(0, 2)
        print("\n",self.name,"wants to play a game")
        print(self.name,"is thinking of a number 0, 1, or 2.")
        guess = int(input("What is your guess 💭 : "))

        ## Lowering boredom attribute based on the user's guess
        if guess == value:
            print("😃")
            print("That is correct!!!")
            self.boredom -= 3
        else:
            print("👎")
            print("WRONG!",self.name,"was thinking of",str(value),".")
            self.boredom -= 1
        ## If boredom is less than zero set it back to zero
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        """ Simulate sleeping the only thing a player can do when the creature is sleeping is to wake it up
             However tiredness and boredom must decrease each time when slept
        """
        ## Put the creature to sleep
        self.is_sleeping == True
        self.boredom -= 2
        self.tiredness -= 3
        print("😴💤💤💤")

        ## Checking if tiredness and boredom are less than 0 if so then set it to 0
        if self.tiredness < 0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0

    def awake(self):
        """ Simulate randomly waking up of a creature """
        ## Creature has a one third chance to randomly wake up
        value = random.ranint(0,2)
        ## If creature wakes up set tiredness to 0 and make sleeping variable false
        if value == 0:
            print(self.name,"just woke up")
            self.is_sleeping = False
            self.tiredness = 0
        else:
            print(self.name,"won't wake up...")
            self.sleep()
        
    def clean(self):
        """ Simulate taking bath of creature to completely clean it """
        self.dirtiness = 0
        print(self.name,"has taken a bath and is clean!🧼")

    def forage(self):
        """ Simulate foraging for food this will increase the creature's food attribute however
            it will also increase their dirtiness as they go in search for food
        """
        ## Randomly found food between 0  to 4 pieces
        food_found = random.randint(0,4)
        self.food += food_found
        ## Increasinf the creatures dirtiness due to foraging
        self.dirtiness += 2
        print(self.name,"found",str(food_found),"number of food pieces")

    def show_values(self):
        """ Shows current information about the creature """
        ## Displaying creature attributes
        print("\nCreature name:",self.name,"" \
                "\nHunger (0 - 10):",str(self.hunger),
                "\nBoredom (0 - 10):",str(self.boredom),
                "\nTiredness (0 - 10):",str(self.tiredness),
                "\nDirtiness (0 - 10):",str(self.dirtiness))
        print("\n")
    
        print("Food Inventory:",str(self.food),"pieces")
        ## Shows current sleeping status
        if self.is_sleeping == True:
            print("Current Status : Sleeping😴")
        else:
            print("Current Status : Awake😊")

    def increment_values(self, difficulty):
        """ User must set an arbitrary difficulty. This will control how much damage you take each round. 
            Update the current values of the creature based on the difficulty selected. 
        """
        ## Increasing the hunger and dirtiness regardless if the creature is awake or sleeping
        self.hunger += random.randint(0,difficulty)
        self.dirtiness += random.randint(0, difficulty)
        ## If the creature is awake he should be growing tiredness and boredom
        if self.is_sleeping == False:
            self.boredom += random.randint(0, difficulty)
            self.tiredness += random.randint(0, difficulty)

    def kill(self):
        """ Check for all condition to kill or sleep the creature. """
        ## First two check will kill the creature and next two checks will put the creature to sleep
        if self.hunger >= 10:
            print(self.name,"as starved to death...💀")
            self.is_alive = False
        elif self.dirtiness >= 10:
            print(self.name,"suffered from infection and died...💀")
            self.is_alive = False
        elif self.boredom >= 10:
            self.boredom = 10
            print(self.name,"is bored. Falling asleep....😴")
            self.is_sleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print(self.name,"is super tired and falling asleep...😴")
            self.is_sleeping = True
        

## Helper functions outside the creature class

def show_menu(creature):
    """ Show the menu options for the player 
        If the creature is sleeping then the player can only wake up the creature by default
    """
    ## If the creature is sleeping only allow user to wake creature hard code the value for sneaky users
    if creature.is_sleeping:
        choice = input("\nPress 6 to try and wake up")
        choice = 6
    ## Creature is awake then give full functionality to user
    else:
        print("\nEnter (1) to eat\nEnter (2) to play\nEnter (3) to sleep\nEnter (4) to take a bath\nEnter (5) to forage for food")
        choice = input("What is your choice: ")
    
    return str(choice)

def call_action(creature, choice):
    """ Given the player's choice, call the appropriate class method."""
    if choice == str(1):
        creature.eat()
    elif choice == str(2):
        creature.play()
    elif choice == str(3):
        creature.sleep()
    elif choice == str(4):
        creature.clean()
    elif choice == str(5):
        creature.forage()
    elif choice == str(6):
        creature.awake()
    else:
        print("Sorry that is not a valid move!")

## THE MAIN CODE
print("💞 Welcome to Pythonagachi Simulator App 💞")

## Set difficulty level
difficulty = int(input("Please choose a difficulty level (0 - 5) : "))
if difficulty > 5:
    difficulty = 5     
elif difficulty < 1:
    difficulty = 1

## The overall main game loop
running = True
while running:
    ##Get user input to give creature a name
    name = input("Name your creature : ")
    player = Creature(name)

    rounds = 1
    ## The game loop that simulates individual round
    ## It runs until the creature is alive
    while player.is_alive:
        print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Round # :",str(rounds))
        ## Individual round should show values, get a players move and call the appropriate method
        player.show_values()
        round_move = show_menu(player)
        call_action(player, round_move)

        print("Round #",str(rounds),"Summary : ")
        ## Summarise the effects of current round 
        player.show_values()
        input("\nPress (Enter) to  continue...")

        ## Increment the values and check for death 
        player.increment_values(difficulty)
        player.kill()

        ## Round is over
        rounds+=1
    
    print("\nRIP 💀")
    print(player.name,"survived a total number of rounds of ",str(rounds - 1),"rounds")

    ## Ask if the user wants to play again or not 
    choice = input("Would you like to play again (Y/N) : ").lower()
    if choice != ("y"):
        running = False 
        print("Thank you for playing Pythonagachi !!")