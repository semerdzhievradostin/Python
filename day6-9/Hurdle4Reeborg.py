def turn_right():
    turn_left()
    turn_left()
    turn_left()

    new_func()

def new_func():
    while not at_goal():
        if wall_in_front():
            turn_left()
        while front_is_clear() and wall_on_right():
            move()
            if right_is_clear():
                turn_right()
                move()
            if not wall_on_right():
                turn_right()
                move()

new_func(turn_right)