#indentation function practice
from shutil import move


def print_values():
    for i in range(1, 21):
        print(i)

print_values()

#few more examples of indentation
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
        else:
            print("Not yet")    

my_function()

#while loop practice 4 examples

# Example 1
i = 1
while i <= 20:
    print(i)

# Example 2
i = 1
while i <= 20:
    if i == 20:
        print("You got it")
    else:
        print("Not yet")
    i += 1

# Example 3
i = 1
while i <= 20:
    print(i)
    if i == 20:
        break

# Example 4
i = 1
while i <= 20:
    if i == 20:
        print("You got it")
    else:
        print("Not yet")
    i += 1



#hurdle 1 practice
# Example 1
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
        else:
            print("Not yet")
# Example 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move():
    pass
def turn_left():
    pass
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()
#escaping the maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def escape_maze():
    while not at_goal():
        if wall_in_front():
            turn_left()
        else:
            move()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()      

        

