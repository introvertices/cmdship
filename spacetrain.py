import random
import os
import time
import keyboard
from threading import Thread

# Star modifiers
blank_chance = 25
field_length = 80
char_choices=[".","*","'",",","`"] + ([" "] * blank_chance)

# Key tracking for debug
key_pressed = ""

# Ship gfx and setup
ship_length = " " * 8
ship_wing_1 = "   |\   "
ship_wing_2 = "   |/   "
ship_design = "\033[1;33;48m>\033[1;31;48m>\033[1;30;48m#\033[0;30;46m|o|\033[0;37;44m|>"
ship_location = [ship_length,ship_wing_1,ship_design,ship_wing_2,ship_length,ship_length,ship_length,ship_length,ship_length,ship_length,ship_length]
ship_index = 2
ship_range = len(ship_location) - 2


# CLEARS THE SCREEN
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Keyboard stuff
def on_press():
    global key_pressed
    global ship_location
    global ship_index

    if keyboard.is_pressed('w') and ship_index <= ship_range and ship_index >1:
        key_pressed = "w"
        ship_index -=1

        #ship placement
        ship_location[ship_index] = ship_design
        ship_location[ship_index-1] = ship_wing_1
        ship_location[ship_index+1] = ship_wing_2
        ship_location[ship_index+2] = ship_length
    elif keyboard.is_pressed('s') and ship_index >=1 and ship_index < ship_range:
        key_pressed = "s"
        ship_index +=1

        #ship placement
        ship_location[ship_index] = ship_design
        ship_location[ship_index-1] = ship_wing_1
        ship_location[ship_index+1] = ship_wing_2
        ship_location[ship_index-2] = ship_length




def list_looping(field_1,field_2,field_3,field_4,amt):
    # get keypresses
    on_press()

    # Print gfx
    print("\033[0;37;40m", ship_location[0],"\033[0;37;40m", *field_1)
    print("\033[0;37;40m", ship_location[1],"\033[0;37;40m", *field_2)
    print("\033[0;37;40m", ship_location[2],"\033[0;37;40m", *field_3)
    print("\033[0;37;40m", ship_location[3],"\033[0;37;40m", *field_4)
    print("\033[0;37;40m", ship_location[4],"\033[0;37;40m", *field_1)
    print("\033[0;37;40m", ship_location[5],"\033[0;37;40m", *field_3)
    print("\033[0;37;40m", ship_location[6],"\033[0;37;40m", *field_2)
    print("\033[0;37;40m", ship_location[7],"\033[0;37;40m", *field_1)
    print("\033[0;37;40m", ship_location[8],"\033[0;37;40m", *field_4)
    print("\033[0;37;40m", ship_location[9],"\033[0;37;40m", *field_2)
    print("\033[0;37;40m", ship_location[10],"\033[0;37;40m", *field_3)


    # Remove and add stars
    field_1.pop(0)
    field_2.pop(0)
    field_3.pop(0)
    field_4.pop(0)

    field_1.append(random.choice(char_choices))
    field_2.append(random.choice(char_choices))
    field_3.append(random.choice(char_choices))
    field_4.append(random.choice(char_choices))

    # Get keypresses
    on_press()

    # Keep going unless loop has hit the specified number of runs
    amt -= 1
    if amt > 0:
        time.sleep(0.1)
        clear()
        list_looping(field_1,field_2,field_3,field_4,amt)




def main():
    # Set up thread to capture keys asynchronously
    thread = Thread(target = on_press)
    thread.start()

    field_1 = []
    field_2 = []
    field_3 = []
    field_4 = []

    for i in range(field_length):
        field_1.append(random.choice(char_choices))
        field_2.append(random.choice(char_choices))
        field_3.append(random.choice(char_choices))
        field_4.append(random.choice(char_choices))
    


    list_looping(field_1,field_2,field_3,field_4,500)
    







if __name__ == "__main__":
    main()