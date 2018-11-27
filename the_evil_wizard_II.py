# The Evil Wizard II The Wrath of Drastone
# venombash@gmail.com
#
# The sequel to The Evil Wizard
# https://github.com/venombash/The-Evil-Wizard

player = ""# the name of the player
health = 0# players health
armor = 0# players armor
hd = 0# the players hit die
race = ""# the players race
Class = ""# the players class
lang = []# the languages the player can speak
enemies = [""]# the enemies in a given battle
enemy_health = 0# the enemies health
enemy_armor = 0# the enemies armor
enemy_hd = 0# the enemies hit die
gp = 0# the players gold pieces
sp = 0# the players silver pieces
bp = 0# the players bronze pieces
inventory = []# the players inventory
hunger = 0# the players hunger
num_enemies = 0# the number of enemies the player has to fight
talon_alive = True# Talon is alive at the start of the game

def menu():
    global player, health, armor, hd, race, Class, lang
    
    MENU = """
0 - Exit
1 - Name your player
2 - Choose race
3 - Choose class
4 - Start your adventure!
"""
    
    print(MENU)# prints the menu
    
    choice = input()
    
    if choice == "0":
        callExit()
    elif choice == "1":
        i = input("Name: ")
        player = i
    elif choice == "2":
        RACES = """
1 - Human, 6 HP, 10 Armor, Languages: Basic
2 - Dwarf, 8 HP, 15 Armor, Languages: Basic, Dwarfish
3 - Elf, 6 HP, 10 Armor, Languages: Basic, Elvish, Ald Tang
4 - Halfling, 4 HP, 5 Armor, Languages: Basic, Pleasant
"""

        print(RACES)
        i = input("Race: ")
        if i == "1":
            race = "Human"
            hp = 6
            armor = 10
            lang.append("Basic")
        elif i == "2":
            race = "Dwarf"
            hp = 8
            armor = 15
            lang.append("Basic")
            lang.append("Dwarfish")
        elif i == "3":
            race = "Elf"
            hp = 6
            armor = 10
            lang.append("Basic")
            lang.append("Elvish")
            lang.append("Ald Tang")
        elif i == "4":
            race = "Halfling"
            hp = 4
            armor = 5
            lang.append("Basic")
            lang.append("Pleasant")
        else:
            print("Please choose one of the above")# the player has entered some unknown option
    elif choice == "3":
        CLASSES = """
1 - Warrior, 6 HD
2 - Priest, 6 HD
3 - Hunter, 8 HD
4 - Rouge, 10 HD
5 - (NEW!) Cleric, 12 HD
"""
        
        print(CLASSES)
        i = input("Class: ")
        
        if i == "1":
            Class = "Warrior"
            hd = 6
        elif i == "2":
            Class = "Priest"
            hd = 6
        elif i == "3":
            Class = "Hunter"
            hd = 8
        elif i == "4":
            Class = "Rouge"
            hd = 10
        elif i == "5":
            Class = "Cleric"
            hd = 12
        else:
            print("Please choose one of the options above")
    elif choice == "4":
        if player != "" and Class != "" and race != "":
            scene1()
        else:
            print("Not done creating your player")
    else:
        print("Please enter one of the options above")
        
def scene1():
    SCENE = """
\"That's drastone?\" you ask. \"As in the guy we've been looking for?\"
\"Aye,\" Talon said. \"I could bet money on it.\"
\"But there's nothing we can do about it,\" you say shaking your head.
\"Now now. What kind of attitude is that!\" Talon picks up a bone from the
floor.
\"I don't like this place and I don't think I'm sticking around.\"
As you watch he opens his mouth and breathes fire onto the bone melting
it. Next he puts it into the key hole. After a couple minutes, he turns it
and unlocks the door.
\"Lead the way,\" he says.
"""

    print(SCENE)
    playerTurn('dungeon')
    
def playerTurn(location):
    
    if location == "dungeon":
        SCENE = """
As you sneak out you see a guard."""
        
        print(SCENE)
        
        options = """
0 - Exit
1 - Kill him
2 - Try to sneak past him
"""
        print(options)
        
        choice = input()
        
        if choice == "1":
            scene2(1)
        elif choice == "2":
            scene2(2)
        elif choice == "0":
            callExit()
            
    elif location == "courtyard":
        SCENE = """
And then you realize you're surronded."""
        print(SCENE)
        
        options = """
0 - Exit
1 - Run back down the corridor
2 - Fight
"""
        print(options)
        choice = input()
        
        if choice == "1":
            scene3(1)
        elif choice == "2":
            battle('orcs', 4)
            scene3(2)
        elif choice == "0":
            callExit()
            
    elif location == "talon_dead":
        
        options = """
0 - Exit
1 - Try to revive him(Cleric)
2 - Leave him
"""
        print(options)
        choice = input()
        
        if choice == "1":
            revive('talon')
        elif choice == "2":
            scene4(1)
        elif choice == "0":
            callExit()
            
    elif location == "drama":
        
        options = """
0 - Exit
1 - Try to break through the gates
2 - Give up
"""
        print(options)
        choice = input()
        
        if choice == "1":
            scene5(1)
        elif choice == "2":
            scene5(2)
        elif choice == "0":
            callExit()
            
    elif location == "talon_alive":
        
        options = """
0 - Exit
1 - Try to break through the gates
2 - Give up
"""

        print(options)
        choice = input()
        
        if choice == "1":
            scene5(1)
        elif choice == "2":
            scene5(2)
        elif choice == "0":
            callExit()
            
    elif location == "gates":
        
        options = """
0 - Exit
1 - Ambush the gate
2 - Try to sneak past
"""
        print(options)
        choice = input()
        
        if choice == "1":
            scene6(1)
        elif choice == "2":
            scene6(2)
        elif choice == "0":
            callExit()
            
    elif location == "drastone":
        
        options = """
0 - Exit
1 - Cut off his head
2 - Let him take you
"""
        print(options)
        choice = input()
        
        if choice == "1":
            scene7(1)
        elif choice == "2":
            scene7(2)
        elif choice == "0":
            callExit()
            
def callExit():
    import sys
    sys.exit()
    
def scene2(scene):
    
    if scene == 1:
        SCENE = """
You sneak up slowly on the guard then slam his head into the wall.
He falls to the ground, still. Just to be sure he was dead you slit
his throat. You walk down the corridor into a courtyard.
"""
        print(SCENE)
        playerTurn('courtyard')
        
    elif scene == 2:
        SCENE = """
As you sneak around the guard, you breath a sigh of relif. You think 
you might make it. As you look behind you, you trip and let out a gasp.
The guard turns and plants three arrows directly in your chest."""
        print(SCENE)
        endGame()
        
def endGame():
    import time
    
    print("Game Over.")
    time.sleep(10)
    callExit()
    
def scene3(scene):
    
    if scene == 1:
        SCENE = """
As you run back down the corridor you come face to face with a pack of
orcs. Before you can turn around, an orc drives a sword directly through
your chest.
"""
        print(SCENE)
        endGame()
        
    elif scene == 2:
        print("You won the battle.")
        SCENE = """
As Talon raises his blade to behead another orc a great light shines
from the ground. It cracks open and Drastone comes out. He raises his
sword and plunges it deep into Talon's heart.
\"No!\" you cry. Flinging yourself at him. He waves his hand and throws
you aside. You hit the wall hard.
\"Lock up the gate,\" Drastone says. \"Don't let him leave.\"
As the orcs run to lock the gate and Drastone vanishes into thin air
you go over to Talon.
"""
    print(SCENE)
    playerTurn('talon_dead')
        
def battle(enemy_type, enemy_num):
    global enemy_health, enemy_armor, hd
    
    enemy_health = 5
    enemy_armor = 5
    
    if enemy_type == "orcs":
        for i in range(enemy_num):
            enemies.insert(0, 'orc')
        import random
        player_roll = random.randint(1, hd)
        print("Player rolled a %d" % (player_roll))
        checkDead('enemy', player_roll)
        enemy_roll = random.randint(1, 6)
        print("%s rolled a %s" % (enemy_type, enemy_roll))
        checkDead('player', enemy_roll)
        
def checkDead(who, roll):
    global armor, enemy_armor, enemy_health, health, num_enemies
    
    if who == "enemy":
        if enemy_armor <= 0 and enemy_health > 0:
            enemy_health -= roll
        else:
            enemy_armor -= roll
            
    elif who == "player":
        if armor <= 0 and health > 0:
            return ''
        else:
            return ''
            
def revive(person):
    global Class, talon_alive
    
    if person == "talon":
        if Class == "Cleric":
            import random
            r = random.randint(1, 2)
            if r == 1:
                print("You have revived Talon!")
                talon_alive = True
                playerTurn('talon_alive')
            else:
                print("You couldn't revive Talon.")
                talon_alive = False
                scene4(1)
        else:
            print("You are not a Cleric")
            
def scene4(scene):
    if scene == 1:
        SCENE = """
Tears stream down your face as you turn away from his blank eyes. You
seem lost yet you must make your choice.
"""
        print(SCENE)
        playerTurn('drama')
        
def scene5(scene):
    
    if scene == 1:
        if talon_alive == True:
            SCENE = """
As Talon gets to his feet, you pick up a fallen orc's sword.
\"We have to break through the gates,\" you tell him.
He looks at you a moment,
\"You sure you want to do this?\" he asks.
You look back,
\"Yes.\"
Talon grins.
\"Then let's get to it!\"
"""
            print(SCENE)
            playerTurn('gates')
        else:
            SCENE = """
You turn and begin to walk toward the gates. It was time to avenge Talon,
and everyone Drastone has ever killed.
"""
            print(SCENE)
            playerTurn('gates')
            
    elif scene == 2:
        if talon_alive == True:
            SCENE = """
Talon picks up a sword and starts to head up to the gates. He turns and
looks at you,
\"You comin' kid?\"
You look up.
\"I can't Talon,\" you say.
He gazes at you with sad eyes.
\"That's your choice lad,\" he says quietly.
When you turn he's gone.
"""
            print(SCENE)
            endGame()
        else:
            SCENE = """
As you sit there, grief overtakes you. The blade shines as you stab
it through your chest.
"""
            print(SCENE)
            endGame()
            
def scene6(scene):
    
    if scene == 1:
        if talon_alive == True:
            SCENE = """
As you and Talon storm across the open ground toward the gate, cutting
down any orcs that are in your way, you hear a whoosh and dull thud
of an arrow. You look down at your chest, slightly suprised that
there is blood dripping down from the wound.
"""
            print(SCENE)
            endGame()
        else:
            SCENE = """
As you storm across the open ground toward the gate, cutting down any
orcs that are in your way, you hear a whoosh and dull thud of an arrow.
You look down at your chest, slightly suprised that there is blood
dripping from the wound.
"""
            print(SCENE)
            endGame()
    elif scene == 2:
        if talon_alive == True:
            SCENE = """
You move forward, with quick stelth, and motion to Talon to follow. When
you almost reach the end, Drastone comes out of the earth and grabs you
and Talon by your necks.
\"Take them to the dungeon.\"
"""
            print(SCENE)
            playerTurn('drastone')
        else:
            SCENE = """
You move forward, with quick stelth. When you almost reach the end, Drastone
comes out of the earth and grabs you by your neck.
\"Take him to the dungeon.\"
"""
            playerTurn('drastone')
            
def scene7(scene):
    
    if scene == 1:
        if talon_alive == True:
            SCENE = """
\"Talon! Duck!\" you scream as you swipe the sword through Drastone's
neck. There was a flash of steel and blood, and he drops you from his
limp hands. You toss Talon a dagger and charge into battle. Drastone's
death motivating you.
"""
            print(SCENE)
            scene8('good', True)
        else:
            SCENE = """
There was a flash of steel and blood as you swipe your sword through 
Drastone's neck, and he drops you from his limp hands. You charge
into battle. Drastone's death motivating you.
"""
            print(SCENE)
            scene8('good', False)
    
    elif scene == 2:
        if talon_alive == True:
            SCENE = """
\"This is the end lad.\"
You look over at Talon, and see a defeated man, hanging limply from
Drastone's massive hands like a man sent to the gallows.
\"Sorry,\" he says as Drastone plunges his claws into your chests.
"""
            print(SCENE)
            endGame()
        else:
            SCENE = """
You sigh as you look at Drastone.
\"You will be defeated eventually,\" you say.
\"We'll see,\" he says as he rips your head off.
"""
            print(SCENE)
            endGame()
            
def scene8(scene_type, talon):
    
    if scene_type == "good":
        if talon == True:
            SCENE = """
\n\t\t30 years later\n\n
You look at your child as it prepares to walk out the door, preparing
to go to Lathos for his first inthrallment.
\"Work hard son.\"
He grins at you.
\"You got it dad.\"
"""
            print(SCENE)
            goodbye()
            
def goodbye():
    i = """
\n\nThanks for playing The Evil Wizard II Wrath of Drastone!
Don't forget to play The Evil Wizard III Shadow of Death!

comment at venombash@gmail.com

Thanks for playing!
"""
    print(i)
    input("\n\nPress the enter key to exit.")
    callExit()
        
        
if __name__ == "__main__":
    while True:
        menu()
