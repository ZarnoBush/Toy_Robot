import sys

if len(sys.argv) > 1:
    if sys.argv[1] == 'turtle':
        import world.turtle.world as world
        import world.obstacles as obstacles
        world.draw_game_boundaries()
        
    else:
        import world.obstacles as obstacles
        import world.text.world as world
        
else:
    import world.obstacles as obstacles
    import world.text.world as world


VALID_COMMANDS = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay', 'replay range']
VALID_MOVEMENT = ['forward', 'back','sprint', 'replay']
COMPASS = ['N', 'E', 'S', 'W']
VALID_REPLAY_COMMANDS = ['silent', 'reversed', 'reversed silent']


def robot_start():
    """This is the entry function, do not change"""
    run_commands()


def get_history():
    """ Creates empty list to use for storing commands. """
    return []


def store_in_history(command, history):
    """ Adds commands to history. """
    if validate_command(command) and not command.startswith('r') and not command.startswith('s'):
        if command not in history:
            history.append(command)
            

def name_the_robot():
    """ Sets name of robot. """
    name = input("What do you want to name your robot? ").upper().strip()
    if name != '':
        print(f"{name}: Hello kiddo!")
        return name
    return name_the_robot()
 

def get_command(name):
    """ Gets command from user. """ 
    command = input(f"{name}: What must I do next? ").strip()
    if not validate_command(command):
        print(f"{name}: Sorry, I did not understand '{command}'.")
        return get_command(name)
    length = len(command.split())
    return command_parse(command, length)


def validate_command(command):
    """ Validates command. """
    if ' ' in command:
        if len(command.split()) == 2:
            if (command.split()[0].lower() in VALID_MOVEMENT) and command.split()[-1].isdigit(): return True
            if (command.split()[0].lower() in VALID_COMMANDS and \
                (command.split()[-1].lower()) in VALID_REPLAY_COMMANDS) and \
                (len(command.split()) == 2): return True
            if (command.split()[0].lower() in VALID_MOVEMENT) and command.split()[1].split('-')[0].isdigit() and \
                command.split()[1].split('-')[1].isdigit(): return True
                
        if len(command.split()) == 3:   
            if (command.split()[0].lower() in VALID_COMMANDS and \
                (command.split()[-1].lower()) in VALID_REPLAY_COMMANDS) and \
                (command.split()[1].isdigit()): return True
            if (command.split()[0].lower() in VALID_COMMANDS) and \
                (' '.join(command.split()[1:]).lower() in VALID_REPLAY_COMMANDS): return True  
                         
        if len(command.split()) == 4:
            if (command.split()[0].lower() in VALID_COMMANDS) and \
                (' '.join(command.split()[2:]).lower() in VALID_REPLAY_COMMANDS) and \
                (command.split()[1].isdigit()): return True
                
    if ' ' not in command:         
        if command.lower() in VALID_COMMANDS and command.lower() not in VALID_MOVEMENT: return True
        if command.lower() == 'replay': return True
    return False


def command_parse(command, length):
    """ Takes in a movement command, splits it into a command and number of steps. """
    split_command = command.split()
    
    if length == 2:
        if (command.split()[0].lower() in VALID_MOVEMENT) and command.split()[-1].isdigit():
            command, number_of_steps = split_command
            return command.lower(), int(number_of_steps)
        if (split_command[0].lower() == 'replay') and \
           (split_command[1].split('-')[0].isdigit()) and (split_command[1].split('-')[1]):
            command, number_of_steps = split_command
            return command.lower(), number_of_steps
        
    if length == 3:
        if (command.split()[0].lower() in VALID_COMMANDS and \
            (command.split()[-1].lower()) in VALID_REPLAY_COMMANDS) and \
            (command.split()[1].isdigit()): 
                command = (' '.join(split_command[0:3:2]))
                number_of_steps = int(split_command[1])
                return command.lower(), int(number_of_steps)
        if (command.split()[0].lower() in VALID_COMMANDS) and \
            (' '.join(command.split()[1:]) in VALID_REPLAY_COMMANDS):
                return command.lower(), ''

    return command.lower(), ''


def help_command():
    """ Provides information about commands. """
    
    return """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - moves robot forward
BACK - moves robot back
RIGHT - turns robot right
LEFT - turns robot left"""



def off_command(name):
    """ Prints out shutting down. """
    print(f"{name}: Shutting down..")
    
def run_commands():
    """ Runs the commands for the robot. """
    list_of_functions = [off_command, help_command, world.forward_command, world.back_command, \
                        world.right_turn_command, world.left_turn_command , world.sprint_command, \
                        world.replay_command_basic, world.replay_command_range]

    index = 0
    x,y = 0,0
    updated_direction = 'N'
    history = get_history()
    full_command = ''
    name = name_the_robot()
    obstacles.reset_obs()
    if len(sys.argv) > 1 and sys.argv[1] == 'turtle':
        world.name_turtle(name)
    
    if obstacles.get_obstacles != []:
        world.generate_obstacles()

    while True:
        if index not in range(-3,4): index = 0
        
        command, number_of_steps = get_command(name)
        silence = False
        reverse = False
        
        if type(number_of_steps) is int:
            full_command = ' '.join([command, str(number_of_steps)])
        
        if command != 'replay':
            store_in_history(full_command, history)
        current_direction = updated_direction
        
        if command == 'off':
            off_command(name)
            return
        
        elif command == 'help':
            print(help_command())  
            
        elif command == 'forward':
            x,y = world.forward_command(current_direction,name,number_of_steps,silence,False,x,y)

        elif command == 'back':
            x,y = world.back_command(current_direction,name,number_of_steps,silence,False,x,y)

        elif (command) == 'right':
            index += 1
            updated_direction = world.right_turn_command(index, name, x,y)
            
        elif (command) == 'left':
            index -= 1
            updated_direction = world.left_turn_command(index, name, x,y)  
            
        elif (command) == 'sprint':
            x,y = world.sprint_command(current_direction, name,number_of_steps, silence, x,y)
            world.display_current_coordinates(x,y, name)
            
        elif command == 'replay' and history != []:
            if number_of_steps == '':
                x,y = world.replay_command_basic(history, list_of_functions, current_direction,name,number_of_steps,x,y, silence, reverse)
            if number_of_steps != '':
                x,y = world.replay_command_range(history, list_of_functions, current_direction,name,number_of_steps,x,y, silence, reverse, number_of_steps)
               
        elif command == 'replay silent' and history != []:
            silence = True
            if number_of_steps == '':
                x,y = world.replay_command_basic(history, list_of_functions, current_direction,name,number_of_steps,x,y, silence, reverse)
            if number_of_steps != '':
                x,y = world.replay_command_range(history, list_of_functions, current_direction,name,number_of_steps,x,y, silence, reverse, number_of_steps)

        elif command == 'replay reversed' and history != []:
            reverse = True
            if number_of_steps == '':
                x,y = world.replay_command_basic(history, list_of_functions, current_direction,name,number_of_steps,x,y, silence, reverse)
            if number_of_steps != '':
                x,y = world.replay_command_range(history, list_of_functions, current_direction,name,number_of_steps,x,y, silence, reverse, number_of_steps)
            
        elif command == 'replay reversed silent' and history != []:
            reverse = True
            silence = True
            if number_of_steps == '':
                x,y = world.replay_command_basic(history, list_of_functions, current_direction,name,number_of_steps,x,y, silence, reverse)
            if number_of_steps != '':
                x,y = world.replay_command_range(history, list_of_functions, current_direction,name,number_of_steps,x,y, silence, reverse, number_of_steps)



if __name__ == "__main__":
    robot_start()