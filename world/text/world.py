import import_helper
import sys

if len(sys.argv) > 1:
    if len(sys.argv) > 2:
        obstacles = import_helper.dynamic_import(f"maze.{sys.argv[2]}")
        
    else:
        obstacles = import_helper.dynamic_import("maze.obstacles")

else:
    import maze.obstacles as obstacles

VALID_COMMANDS = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay', 'replay range']
VALID_MOVEMENT = ['forward', 'back','sprint', 'replay']
COMPASS = ['N', 'E', 'S', 'W']
VALID_REPLAY_COMMANDS = ['silent', 'reversed', 'reversed silent']


def maze_runner():
    
    return
    
    

def generate_obstacles():
    coods, blueprint = obstacles.get_obstacles()
    
    if coods != []:
        print("There are some obstacles:")
        for i in range(len(coods)):
            x,y = coods[i]
            print(f"- At position {x},{y} (to {x+4},{y+4})")
            
    return coods, blueprint


def change_direction(index):
    """ Checks current direction, then sets new direction based on index given. """
    if index not in range(-3,4): index = 0
    return COMPASS[index]


def update_y_positive_axis(name,number_of_steps, x,y):
    """ Updates value of y. """
    check_y = y + number_of_steps
    if check_coordinates_in_range(x, check_y):
        if obstacles.is_position_blocked(x,check_y) and \
            obstacles.is_path_blocked(x,y,x,check_y):
            print(f"{name}: Sorry, there is an obstacle in the way.")
            return y

        else:
            return y + number_of_steps
        
    else:
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        return y


def update_y_negative_axis(name,number_of_steps, x,y):
    """ Updates value of y. """
    if check_coordinates_in_range(x, y-number_of_steps):
        if obstacles.is_position_blocked(x,y - number_of_steps) or \
            obstacles.is_path_blocked(x,y,x,y - number_of_steps):
            print(f"{name}: Sorry, there is an obstacle in the way.")
            return y

        else:
            return y - number_of_steps

    else:
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        return y


def update_x_positive_axis(name,number_of_steps, x,y):
    """ Updates value of x. """
    if check_coordinates_in_range(x+number_of_steps,y):
        if obstacles.is_position_blocked(x + number_of_steps,y) and \
            obstacles.is_path_blocked(x,y,x + number_of_steps,y):
            print(f"{name}: Sorry, there is an obstacle in the way.")
            return x

        else:
            return x + number_of_steps
        
    else:
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        return x


def update_x_negative_axis(name,number_of_steps, x,y):
    """ Updates value of x. """
    if check_coordinates_in_range(x - number_of_steps,y):
        if obstacles.is_position_blocked(x - number_of_steps,y) and \
            obstacles.is_path_blocked(x,y,x - number_of_steps,y):
            print(f"{name}: Sorry, there is an obstacle in the way.")
            return x

        else:
            return x - number_of_steps
    else:
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        return x



def check_coordinates_in_range(x,y):
    """ Checks if coordinates are in valid range. """
    if x in range(-100,101) and y in range(-200,201): return True
    return False


def default_coordinates(x,y):
    """ Creates default coordinates. """
    return x,y


def display_current_coordinates(x,y, name):
    """ Displays current coordinates of robot. """
    print(f" > {name} now at position ({x},{y}).")


def update_coordinates(x,y):
    """ Updates robots coordinates. """
    return x,y


def forward_command(direction,name,number_of_steps,silence,sprinting, x,y):
    """ Moves the robot forward depending on which direction it is facing. """
    default_x_y = default_coordinates(x,y)
    x1,y1 = default_x_y[0], default_x_y[1]
    out_of_range = False
    if (x1 == x) and (y1 < y + number_of_steps):
        if not check_coordinates_in_range(x, y + number_of_steps):
            out_of_range = True
    
    if (y1== y) and (x1 > x - number_of_steps):
        if not check_coordinates_in_range(x - number_of_steps, y):
            out_of_range = True
    
    if direction == 'E':
        x = update_x_positive_axis(name,number_of_steps,x,y)
    if direction == 'W':
        x = update_x_negative_axis(name,number_of_steps,x,y)
    if direction == 'N':
        y = update_y_positive_axis(name,number_of_steps,x,y)
    if direction == 'S':
        y = update_y_negative_axis(name,number_of_steps,x,y)
    
    
    if not silence:
        if out_of_range is False:
            print(f" > {name} moved forward by {number_of_steps} steps.")
        if not sprinting:
            display_current_coordinates(x,y, name)
    return x,y
    
    

def back_command(direction,name,number_of_steps,silence, sprinting,x,y):
    """ Moves the robot back depending on which direction it is facing. """
    default_x_y = default_coordinates(x,y)
    x1,y1 = default_x_y
    blocked = False
    
    if direction == 'E':
        x = update_x_negative_axis(name,number_of_steps,x,y)
    if direction == 'W':
        x = update_x_positive_axis(name,number_of_steps,x,y)
    if direction == 'N':
        y = update_y_negative_axis(name,number_of_steps,x,y)
    if direction == 'S':
        y = update_y_positive_axis(name,number_of_steps,x,y)

    if not silence:
        print(f" > {name} moved back by {number_of_steps} steps.")
        if not sprinting:
            display_current_coordinates(x,y, name)
    return x,y


def sprint_command(direction, name, number_of_steps, silence, x, y):
    """ Allows robot to sprint forward based on the direction it is facing. """
    if number_of_steps == 0: return x,y
    x,y = forward_command(direction,name,number_of_steps,silence,True,x,y)
    return sprint_command(direction, name, number_of_steps -1, silence,x, y)
    

def right_turn_command(index, name, x,y):
    """ Turns robot to the right. """
    print(f" > {name} turned right.")
    display_current_coordinates(x,y,name)
    return change_direction(index)
    
   
def left_turn_command(index, name, x,y):
    """ Turns robot to the left. """
    print(f" > {name} turned left.")
    display_current_coordinates(x,y,name)
    return change_direction(index)


def replay_command_basic(history, list_of_functions, current_direction,name,number_of_steps,x,y, silence, reverse):
    """ Replays commands. """
    if len(history) == 0: return
    if silence:
        flag = 'silently'
    if reverse:
        flag = 'in reverse'
    if reverse and silence:
        flag = 'in reverse silently'
        
    function_map = {command: function for command, function in zip(VALID_COMMANDS, list_of_functions)}
    command_count = 0
    
    if reverse:
        for instruction in history[::-1]:
            command, number_of_steps = instruction.split()
            if command in function_map:
                if command.startswith('f') or command.startswith('b'):
                    x,y = function_map[command](current_direction,name,int(number_of_steps), silence, False, x,y)
                else:
                    x,y = function_map[command](current_direction, name, number_of_steps, silence, x, y)
                command_count +=1
                
    if not reverse:
        for instruction in history:
            command, number_of_steps = instruction.split()
            if command in function_map:
                x,y = function_map[command](current_direction,name,int(number_of_steps), silence, False, x,y)
                command_count +=1
    
    if not silence and not reverse:
        print(f" > {name} replayed {command_count} commands.")  
    if silence and not reverse or reverse and not silence:
        print(f" > {name} replayed {command_count} commands {flag}.")
    if silence and reverse:
        print(f" > {name} replayed {command_count} commands {flag}.")
    
    display_current_coordinates(x,y, name)
    return x,y


def replay_command_range(history, list_of_functions, current_direction,name,number_of_steps,x,y, silence, reverse, n):
    """ Replays commands with specified range. """
    if len(history) == 0: return
    if silence:
        flag = 'silently'
    if reverse:
        flag = 'in reverse'
    if reverse and silence:
        flag = 'in reverse silently'
        
    if type(number_of_steps) != int:
        range_1, range_2 = n.split("-")
        
    function_map = {command: function for command, function in zip(VALID_COMMANDS, list_of_functions)}
    command_count = 0
    
    if reverse:
        for instruction in reversed(history[:n]):
            command, number_of_steps = instruction.split()
            if command in function_map:
                x,y = function_map[command](current_direction,name,int(number_of_steps), silence, False, x,y)
                command_count +=1
                
    if not reverse:
        if type(number_of_steps) != int:
            for instruction in history[-int(range_1):-int(range_2)]:
                command, number_of_steps = instruction.split()
                if command in function_map:
                    x,y = function_map[command](current_direction,name,int(number_of_steps), silence, False, x,y)
                    command_count +=1
        if type(number_of_steps) is int:
            for instruction in history[-n:]:
                command, number_of_steps = instruction.split()
                if command in function_map:
                    x,y = function_map[command](current_direction,name,int(number_of_steps), silence, False, x,y)
                    command_count +=1
    
    if not silence and not reverse:
        print(f" > {name} replayed {command_count} commands.")  
    if silence and not reverse or reverse and not silence:
        print(f" > {name} replayed {command_count} commands {flag}.")
    if silence and reverse:
        print(f" > {name} replayed {command_count} commands {flag}.")
    
    display_current_coordinates(x,y, name)
    return x,y