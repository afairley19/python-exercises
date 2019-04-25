from sys import exit

def start_game():
    print("You are taking a lone walk through the forest.")
    print("You find it strange that there is complete silence. Not even a bird can be heard.")
    print("You suddenly notice a path to your left that diverges from the main trail.")
    print("It is partially obscured by overgrowth, but you think it is walkable.")
    print("Do you EXLPORE the new path or CONTINUE on the main trail?")

    choice = input("> ")

    if "explore" in choice:
        left_trail()
    elif "continue" in choice:
        main_trail()
    else:
        dead("You turn around to head back, but walk the trail for eternity.")

def main_trail():
    print("You continue on the main path.")
    print("You are about to turn back when a giant toad hops onto the trail.")
    print("You are distracted and fall. The toad hops over and sits very close to your face.")
    name = input("The toad asks: What is your name? ")
    print("Hello, " + name + " I will free you from this forest if you can answer my riddle.")
    print("Do you want to play? Y/N")

    choice = input("> ")

    if choice == "Y":
        riddle1()
    elif choice == "N":
        left_trail()
    else:
        dead("You are doomed to wander the forest for eternity.")


def left_trail():
    print("You walk along the path for several hours, lost in thought.")
    print("You realize you have lost track of time and stop. When you look down there is a circle of mushrooms in front of you.")
    print("Do you PROCEED through the new path or head BACK to the main trail?")
    
    direction = input("> ")

    if "proceed" in direction:
        proceed_trail()
    else:
        print("You walk back the way you came.")
        main_trail()

def proceed_trail():
    print("You notice there is poison ivy surrounding the trail.")
    print("To avoid the plant, you step into the mushroom ring to continue through the trail.")
    print("Once your feet touch the ground, everything goes black and air rushes around you.")
    print("You start to panic, when suddenly it stops. You open your eyes and see that you are in a cave.")
    print("A white rabbit appears.")

    name = input("The rabbit asks: What is your name? ")
    print("Hello, " + name + " I will grant you your greatest wish if you can answer my riddle.")
    wish = input("What is your greatest wish, " + name + "? ")
    print("Do you want to play? Y/N")

    choice = input("> ")

    if choice == "Y":
        print("You will be granted " + wish + " if you are correct.")
        riddle2()
    elif choice == "N":
        print("You are whisked back to the main trail.")
        main_trail()
    else:
        dead("You are doomed to wander in the dark cave for eternity.")

def dead(why):
    print(why, "It is lonely and dark.")
    exit(0)

def riddle1():
    print("The more you take, the more you leave behind. What is it?")

    answer1 = input("> ")

    if answer1 == "footsteps":
        print("You are correct! You are freed from the forest.")
        exit(0)
    else:
        dead("Incorrect! Millions of frogs hop onto the trail and carry you into the forest.")

def riddle2():
    print("What must break before you can use it?")

    answer2 = input("> ")

    if answer2 == "egg":
        print("You are correct! I grant you your wish and free you from the forest!")
        exit(0)
    else:
        print("Incorrect! You are whisked back to the main trail.")
        main_trail()


start_game()
